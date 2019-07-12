import numpy as np
import cv2

im=cv2.imread('test.png')

points = [(160, 160), (136, 160), (150, 200), (200, 180), (120, 150), (145, 180)]
for point in points:
    cv2.circle(im,point,2,(0,0,255),2)
cv2.imshow('test',im)
cv2.waitKey(2*1000)
cv2.destroyAllWindows()

