import Recognizer
import cv2 as cv

isSecured = True

faceDetect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
camera = cv.VideoCapture(0)

while True or (isSecured == False):
    _, image = camera.read()
    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            image = Recognizer.recognizePerson(x, y, w, h, image, grayImage)

    cv.imshow("Face", image)

    key = cv.waitKey(1)
    if key == 27:
        break

camera.release()
cv.destroyAllWindows()