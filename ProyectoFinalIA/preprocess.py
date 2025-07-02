import cv2
import os

img = cv2.imread('dataset/train/images/04BQAE7MYu7VXe1wYGLM.jpg')
resized = cv2.resize(img, (224, 224))
normalized = resized / 255.0
cv2.imshow('Processed', resized)
cv2.waitKey(0)
