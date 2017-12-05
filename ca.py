import cv2

cap = cv2.VideoCapture(0)

'''
ret, img = cap.read()
print ret
cv2.imshow("IMG", img)

cv2.imwrite("test.jpg", img)
'''
while True:
    ret, img = cap.read()
    cv2.imshow("img", img)
    cv2.imwrite("test.jpg", img)
    if cv2.waitKey(5) == 27:
        break


cap.release()
cv2.destroyAllWindows()
