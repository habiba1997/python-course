import cv2


def draw_circle(event, x, y, flag, param):
    # double lick event
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 100, (255, 0, 0), -1)


image = cv2.imread('./Archive/lena.jpg', 1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', image)
    #  27 = ecc key
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
