import cv2
import os
import numpy as np
import faceDetection as fd

test_img = cv2.imread("facce/0/picture_2025-10-01_19-49-22.jpg")
face, gray = fd.faceDetection(test_img)

for(x,y,w,h) in face:
    cv2.rectangle(test_img,(x,y),(x+w, y+h),(0,0,255),thickness=5)

resized=cv2.resize(test_img,(1920,1080))

cv2.imshow("faccia trovata", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()