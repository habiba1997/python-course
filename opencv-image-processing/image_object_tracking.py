import cv2
import numpy as np

image = cv2.imread('./Archive/blue.jpg', 1)
# convert image from bgr color space to hue color space
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image', new_image)

#  hue, saturation, value of blue
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 252, 255])

# getting these values
blue = np.uint8([[[255, 0, 0]]])
hsv_value = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print (hsv_value)  # [[[120 255 255]]]

#  find any object with the color in range of lower to upper
mask = cv2.inRange(new_image, lower_blue, upper_blue)
cv2.imshow('mask', mask)

# operation and mask the image on image
# original image, image, mask
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
