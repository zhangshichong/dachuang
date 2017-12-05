import cv2 as cv

cap = cv.VideoCapture(0)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 800)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 600)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.waitKey(20) == 27:
        break
cv.DestroyAllWindows()
