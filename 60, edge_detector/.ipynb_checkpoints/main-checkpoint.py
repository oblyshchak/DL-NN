import cv2
import numpy as np
from scipy import ndimage



image = cv2.imread('map.png')
print(image.shape)
image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.GaussianBlur(image_gray, (1, 1), 0)

gX = cv2.Sobel(image_gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(image_gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)
img_sobel = cv2.addWeighted(gX, 1, gY, 1, 0)


canny_image = cv2.Canny(image_gray, 110, 200)
# cv2.imshow('Sobel image', img_sobel)


image_2 = cv2.imread('map.png', 0).astype('float64')
image_2 /= 255.0
roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )

vertical = ndimage.convolve( image_2, roberts_cross_v )
horizontal = ndimage.convolve( image_2, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255

cv2.imshow('Roberts', edged_img)
# cv2.imshow('image', image)
# cv2.imshow('Canny image', canny_image)

cv2.waitKey(0)
