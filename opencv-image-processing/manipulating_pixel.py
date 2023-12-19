import cv2

image = cv2.imread('./Archive/lena.jpg', 1)
# slice image
a = image[0:100, 0:100]
#  assign this part to another place
image[100:200, 100:200] = a

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
