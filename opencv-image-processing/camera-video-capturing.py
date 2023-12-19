import cv2

# access the web cam, mention device in which it will capture thr frames (0) is 1st web cam
capture = cv2.VideoCapture(0)

while (True):
    # capture frame
    ret, frame = capture.read(0)

    # change the current image to qray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display teh frame
    cv2.imshow('image', gray)

    #  when you press on q key in keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
