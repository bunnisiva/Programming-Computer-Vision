import numpy as np 
import cv2
#Create a Video Capture object:
capture = cv2.VideoCapture('./IMG_2933.MP4')
# Replay all the frames in the video
while True:
    has_frame,frame = capture.read()
    if not has_frame:
        print ('Reached end of the video')
        break
    cv2.imshow('frame_babies',frame)
    key = cv2.waitKey(50)
    if key ==27:
        print ('Pressed Esc')
        break
cv2.destroyAllWindows()
