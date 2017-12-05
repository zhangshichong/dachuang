import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print ("camera error")

ret, image = cap.read()
cv2.imwrite('pic.jpg', image)

img_window = 'ImgCaptd'
img_window = cv2.namedWindow(img_window, cv2.WINDOW_NORMAL)
cv2.imshow(img_window, image)
