import cv2
import numpy as np

#  flag value for when you want the image as a colored image 1 , 0 means black and white
image = cv2.imread('./Archive/train.jpeg', 0)
cv2.imshow('image', image)

# 1- image blurring
# is summing and getting mean of surrounding pixels and replace image value
# low pass filter
kernel = np.ones((5, 5), np.float32) / 25  # divide to get average value
# -1 depth , same depth as original
new_image = cv2.filter2D(image, -1, kernel)
cv2.imshow('filtered', new_image)  # now the image is blured but edges are blured as well

# avoid corners or edges to be blured
# 2- averaging => low pass filter
# ksize : kernal size
blur_averaging = cv2.blur(image, (5, 5))
cv2.imshow('averaged_image', new_image)

# 3- gaussian filtering
# 0 standard diviasion in x-axis
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('gaussian_image', gaussian_image)

cv2.waitKey(1000)
cv2.destroyAllWindows()
