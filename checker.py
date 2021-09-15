import os
import numpy as np
import cv2 as cv

my_collection = []

def parser():
  massive = [img for img in list(os.walk('insects/photos'))]
  massive = np.squeeze(massive[0][2])
  n = massive.shape[0]
  print(massive)
  for i in range(n):
    print('insects/photos/'+massive[i])
    img = cv.imread('insects/photos/'+massive[i])
    cv.imshow('img',img)
    cv.waitKey(1)
    my_collection.append(img)
parser()
my_collection = np.reshape(my_collection,(2,2,-1))
print(my_collection,np.shape(my_collection),sep='\n')
