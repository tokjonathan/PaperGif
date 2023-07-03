import os, uidService
import streamlit as st
from filepathClass import FilePath
import ffmpegService
uploaded_file = st.file_uploader('Upload a video to start')
st.text_input('noOfFrames', value=120, key='no_of_frames')


orderID = uidService.generateOrderID()
if uploaded_file is not None:
    st.write('Size of uploaded file : {}'.format(uploaded_file.type), 'Size of uploaded file : {}'.format(uploaded_file.size))
    
    container_type = ((uploaded_file.type).split('/'))[-1]

    FilePath.createNewFolder('tempMedia',orderID)
    with open(os.path.join("tempMedia", orderID, uploaded_file.name),"wb") as f: 
        f.write(uploaded_file.getbuffer())         
        
def testPara():
    par = st.session_state.no_of_frames
    print(par)

def testGenerateFrame():
    video_path = os.getcwd() + '/tempMedia/'+ orderID + '/' + uploaded_file.name 
    print(video_path)
    newFolder = os.getcwd() + '/vault'
    ffmpegService.generateFrames(video_path,10,768,432,newFolder,'.mp4',1)

if uploaded_file is not None:
    testGenerateFrame()