import cv2

#  flag value for when you want the image as a colored image 1 , 0 means black and white
image = cv2.imread('./Archive/lena.jpg', 0)
#  create a window to display the image
cv2.imshow('image', image)
# to make image stay, we need to delay, 10,000 => 10 seconds
cv2.waitKey(10000)
cv2.imwrite('lena.png', image)
#  destroy all windows created by the code
cv2.destroyAllWindows()
