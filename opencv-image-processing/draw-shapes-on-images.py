import cv2

image = cv2.imread('./Archive/lena.jpg', 1)
# image line start from 0,0 coordinate to 400,400 and the color is blue (255,0,0),  5 thickness
cv2.line(image, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.rectangle(image, (0, 0), (400, 400), (0, 255, 0), 5)
#  center, radius, -1 in thickness means filled
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)
font = cv2.FONT_ITALIC
cv2.putText(image, 'Hello there', (100, 100), font, 2, (255, 255, 255), cv2.LINE_AA)
cv2.imshow('image', image)
# 0 =. wait forever until I close it
cv2.waitKey(0)
cv2.destroyAllWindows()
