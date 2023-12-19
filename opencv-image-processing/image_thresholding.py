import cv2

# turning a grey scale image to a binary image
# if pixel value > a certaain thresholf value => assign some color
# else assign another color

# why thresholding?
# partition a foreground and background in a certain image
# isolating an object
image = cv2.imread('./Archive/gradient.png', 0)

# cv2.threshold(image, threshold_value, what_value_assigned_when_value_pass_threshold, type_of_thresholding)
ret, threshold_image = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('image', image)
cv2.imshow('threshold', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
