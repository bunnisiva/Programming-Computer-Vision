import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='../data/ed-van.jpg',help='Image path.')
params = parser.parse_args()
img = cv2.imread(params.path)
cv2.imshow("new",img)
cv2.waitKey()
