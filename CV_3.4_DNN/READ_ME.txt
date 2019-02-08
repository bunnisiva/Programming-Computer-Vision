Loading deep learning models using pytorch,caffe
in OpenCV 3.4.1 version with python 3.7 and torch version
0.4 . No cuda 
==============================================
Beware : older open CV 2.7 or below 3.3 donot support
DL pre trained models.
So create a new python env 
Install openCV3.4 using the below instructions .
I used conda , you can use pip install as well

You can install CV 3.4 by doing the following



conda list --show-channel-urls
conda install py-opencv
python -c 'import cv2'

to install pytorch 
conda install pytorch=0.4.1 -c pytorch