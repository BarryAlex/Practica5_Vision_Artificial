#Edwing Alexis Casillas Valencia.   19110113.   7E1.    Práctica 5 visión artificial
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('ACC_WP3.jpg',0)
img2=cv2.imread('ACC_WP3.jpg')
img_ori=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
name=['BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','MEAN','GAUSS','OTSU']

for i in range(8):
    plt.subplot(1,3,1)
    plt.imshow(img_ori)
    plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()

    plt.subplot(1,3,2)
    plt.imshow(img,'gray',vmin=0,vmax=255)
    plt.title('Original BN')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()

    plt.subplot(1,3,3)
    if(i==0):
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    elif(i==1):
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
    elif(i==2):
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
    elif(i==3):
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
    elif(i==4):
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
    elif(i==5):
        tresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)
    elif(i==6):
        tresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
    else:
        ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.imshow(thresh,'gray',vmin=0,vmax=255)
    plt.title(name[i])
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.show()
