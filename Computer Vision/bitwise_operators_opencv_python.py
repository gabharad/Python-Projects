import cv2
import numpy as np

img1 = np.zeros((533,400,3), dtype= np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread('ellipses.jpg')
#print(img1.shape)
#print(img2.shape)

#bitAnd = cv2.bitwise_and(img2, img1)
#bitOr = cv2.bitwise_or(img2, img1)
bitNot = cv2.bitwise_not(img2, img1)
#bitXor = cv2.bitwise_xor(img2, img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('imgAnd', bitAnd)
#cv2.imshow('imgOr', bitOr)
cv2.imshow('imgNot', bitNot)
#cv2.imshow('imgXor', bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()