import numpy as np
import cv2

##img = cv2.imread('lena.jpg', 1)
img = np.zeros([512,512,3])
img = cv2.line(img, (1,1), (256,256), (100,0,0), 10)
img = cv2.arrowedLine(img, (0,256), (256,256), (0,100,0), 10)
img = cv2.circle(img, (310,310), 60, (0,0,100), 10)
img = cv2.rectangle(img, (100,100), (256,256), (100,100,100), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'GG WP', (100,300), font, 3, (50,150,250), 10)

cv2.imshow('img', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
