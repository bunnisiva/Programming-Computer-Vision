import cv2
capture = cv2.VideoCapture('./IMG_2933.MP4')
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print ('Frame count:',frame_count)
print('Position:',int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_,frame = capture.read()
cv2.imshow('frame0',frame)
# capture another frame 
capture.set(cv2.CAP_PROP_POS_FRAMES, 800)
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame1', frame)
#capture one more frame 
capture.set(cv2.CAP_PROP_POS_FRAMES,1000)
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame1000', frame)

cv2.waitKey()
cv2.destroyAllWindows()

