import cv2

# simple thresholding => 1 threshold value for entire image
#  adaptive thresholding => multiple threshold values for small portion of image
#  adaptive give better result in variable lightening conditions

image = cv2.imread('./Archive/sample.jpg', 0)

# cv2.AdaptiveThreshold(image, max_value, method, threshold_type, block_size, constant)
# image: a grey scale image
# max_value : value to be assigned after threshold
# method: mean or gaussian
# block_size: size of neighboring area (11 pixel)
# constant: value subtracted from mean
threshold_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 20)

cv2.imshow('image', image)
cv2.imshow('threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
