import streamlit as st
import makePrintable

#Layout Containers
st.set_page_config(layout='wide')
header = st.container()
details = st.container()
col1, col2 = st.columns((2,1))

#Arranging elements in containers
with header:
    st.title('Papergif Console')

with details:
    st.text('future development : put details here')


with col1 :
    video_container_type = ['mp4','mov','avi','wmv','avchd','mp3']
    uploaded_file = st.file_uploader('Upload a video to start', type=video_container_type)
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        print('This is it - ' + str(st.session_state.uploaded_file))    
        video = st.video(uploaded_file)

    #Crop Capability (future vers)
        # bytes_data = uploaded_file.getvalue()
        # probe = ffmpegService.setFFProbe(uploaded_file.name) 
        # duration = ffmpegService.getDuration(probe)
        
        # optionList = []
        # time_stamp = 0
        # while time_stamp < duration:
        #     min, sec = divmod(time_stamp, 60)
        #     time_notation = min + (sec/100)
        #     optionList.append(str(time_notation))
        #     time_stamp += 0.5
        
        # end_time = 0
        # min, sec = divmod(duration, 60)
        # end_time = '{}:{}'.format(min,sec)
        # if optionList[-1] != end_time:
        #     optionList.append(str(end_time))
        
        # start_time, end_time = st.select_slider(
        #     'Crop to desired length',
        #     options = optionList,
        #     value= (str(0.00), str(end_time)),
        #     on_change=
        #)

with col2:
    st.subheader('Parameters')
    orientation = st.selectbox('Video Orientation Type', options=('Landscape','Portrait'),index=0, key='orientation')
    no_of_frames = st.text_input('No. of frames', value=69, key='no_of_frames')
    frame_width = st.text_input('Frame Width', value=832, key='frame_width')
    frame_height = st.text_input('Frame Height', value=468, key='frame_height')
    quantity = st.text_input('Quantity', value=1, key='quantity')
    left_margin = st.text_input('Quantity', value = 400, key = 'left_margin')
    submitted = st.button('Generate')
    
    if submitted:
        makePrintable.makePrintables()

