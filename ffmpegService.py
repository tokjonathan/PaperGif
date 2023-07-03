import ffmpeg 

def setFFProbe(filename):
    try :
        probe = ffmpeg.probe(filename)
    except ffmpeg.Error as e:
        print('Error Log -- ',e)
    return probe
    

def getDuration(probe):
    try:
        time = float(probe['streams'][0]['duration'])
        time = int(time) #Rounded down to nearest int
        print('Video Duration : ', time, 's')
    except ffmpeg.Error as e:
        print('Error Log -- ',e)
    return time

def getInterval(videoDuration, noOfFrames):
    try:
        interval = videoDuration / noOfFrames
        print('Time Interval : ', interval, 's')
        return interval
    except ffmpeg.Error as e:
        print('Error Log -- ',e)


def generateFrames(filepath, specificTimeStamp, width, height, newFolderPath,i):
    (
    ffmpeg.input(filepath, ss= specificTimeStamp) #ss is seeking parameter
    .filter('scale', width, height)
    .output(newFolderPath + '/Frame'+ str(i)+ '.png', vframes = 1) 
    .global_args('-loglevel', 'error')
    .run()
    )  
    


    
    
    #folderpath [ 'folder_name/' ]
    #extType ['.jpg', '.png', '.svg']
    #width [ -1 ]. negative one means it scales relatively to height to maintain aspect ratio
    #timeInterval [ 122 ] muliply the interval with i to get timeInterval
        


#ReadMe : This contains FFMPEG functionality. Namely the ability to retrieve video's metadata
#          and the ability to create frames from the video