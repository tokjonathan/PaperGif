import ffmpegService, datetimeService, uidService, pageService, PDFService
from filepathClass import FilePath
import os, glob, time
import streamlit as st
start_time = time.time()

def makePrintables():
    orderID = uidService.generateOrderID()
    videoID = uidService.generateVideoID()

    #Create Folders for tempMedia
    FilePath.createNewFolder('tempMedia',orderID)
    tempMedia_orderID_folder = os.getcwd() + '/tempMedia' + '/' +orderID
    video = st.session_state.uploaded_file

    #Create Folder (vault) - vault -> orderID [frame,page,PDF]
    vault_folder_path  = 'vault/' + orderID
    FilePath.createNewFolder(vault_folder_path,'Frame')
    FilePath.createNewFolder(vault_folder_path, 'Page')
    FilePath.createNewFolder(vault_folder_path, 'PDF')

    # Get filename, file type
    container_type = '.' + ((video.type).split('/'))[-1] #video/mp4 from streamlit becomes '.' concat 'mp4'
    video_file = tempMedia_orderID_folder + '/' + videoID + container_type

    #Write File (rename to videoID)
    with open(os.path.join(tempMedia_orderID_folder,video.name),"wb") as f: 
        f.write(video.getbuffer())         
        os.rename((tempMedia_orderID_folder + '/' + video.name), tempMedia_orderID_folder + '/' + videoID + container_type)

    # Parameters
    noOfFrames = int(st.session_state.no_of_frames)
    frameWidth = int(st.session_state.frame_width)
    frameHeight = int(st.session_state.frame_height)
    orientation = st.session_state.orientation
    quantity = int(st.session_state.quantity)
    left_margin = int(st.session_state.left_margin)
    #Extra Parameters
    dateCreated = datetimeService.getDate()

    # Use FFMPEG to derive duration & intervals
    probe = ffmpegService.setFFProbe(video_file) # returns dictionary
    videoDuration = ffmpegService.getDuration(probe) 
    interval = ffmpegService.getInterval(videoDuration, noOfFrames)

    #Generate Frames
    i = 0
    listof_unedited_frames = []
    frame_folder_path = vault_folder_path + '/Frame'
    for i in range(noOfFrames):
        i += 1
        atThisTimeInterval  = i * interval
        ffmpegService.generateFrames(video_file, atThisTimeInterval, frameWidth, frameHeight, frame_folder_path, i)
        unedited_frame_filepath = frame_folder_path + '/Frame' + str(i) + '.png'
        listof_unedited_frames.append(unedited_frame_filepath)
    print('All Frames Created [1]')
    
    #Add Margin
    n = 0
    while n < len(listof_unedited_frames):
        im = listof_unedited_frames[n]
        pageService.Page.add_margin_to_all(im, 0, 0, 0, left_margin, color = (255,255,255))
        n += 1
    
    #Generate Pages
    A4_width = 2480
    A4_height = 3508
    pageObj = pageService.Page(A4_width, A4_height)
    frameObj = pageService.Frame((frameWidth + left_margin),frameHeight)
    filepathObj = FilePath(orderID) 
    pageService.bindFrames(pageObj, 0, filepathObj, frameObj, noOfFrames, 0)


    #Get count of each page in order
    file_count = 0
    for filepath in glob.iglob(os.getcwd() + '/' + vault_folder_path + '/Page/*' + '.png'):
        file_count += 1
        

    #Open all pages file in order
    imageList = []
    i = 1
    while i <= file_count:
        path = os.getcwd() + '/' + vault_folder_path + '/Page'+ '/page{}.png'.format(i)
        img = PDFService.openFile(path)
        imageList.append(img)
        i += 1

    # generate Pages into PDF format
    PDFService.generatePDF(imageList, filepathObj)
    print('-----PDF Generated---- \nThats All Folks.         [{}]'.format(orderID))
    print('Total time to process : ', time.time() - start_time)
    

