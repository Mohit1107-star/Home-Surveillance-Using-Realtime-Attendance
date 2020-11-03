import cv2 as cv
import numpy as np
import _sqlite3 as sqlite
from PIL import Image
import os

faceDetect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

camera = cv.VideoCapture(0)
recognizer = cv.face.LBPHFaceRecognizer_create()
path = "Data Set"


def createUserData(ID, name, age):
    connection = sqlite.connect("PeopleData.db")
    try:
        command = "SELECT * FROM PeopleDetails WHERE ID = " + str(ID)
        cursor = connection.execute(command)
        recordExists = 0
        for row in cursor:
            recordExists = 1

        if recordExists == 1:
            command = "UPDATE PeopleDetails SET Name = " + str(name) + " WHERE ID = " + str(ID)
    except:
        command = "INSERT INTO PeopleDetails(ID, Name, Age) Values(" + str(ID) + ", " + str(name) + ", " + str(age) + ")"
    connection.execute(command)
    connection.commit()
    connection.close()


def GetImagesAndIDs(path):
    imagesPath = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagesPath:
        faceImage = Image.open(imagePath)
        faceNP = np.array(faceImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('_')[1])
        faces.append(faceNP)
        IDs.append(ID)

        cv.imshow("Images Captured", faceNP)
        cv.waitKey(1)

    return np.array(IDs), faces

userID = input("Enter User ID: ")
userName = input("Enter User Name: ")
userAge = input("Enter User Age: ")
createUserData(userID, userName, userAge)
sampleNumber = 0

while True:
    _, image = camera.read()
    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayImage, 1.3, 5)

    for(x, y, w, h) in faces:
        sampleNumber += 1
        cv.imwrite("Data Set/User_" + str(userID) + "_" + str(sampleNumber) + ".jpg", grayImage[y:y+h, x:x+w])
        cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.waitKey(1)
    cv.imshow("Face", image)

    cv.waitKey(1)
    if(sampleNumber >= 500):
        break

IDs, faces = GetImagesAndIDs(path)
recognizer.train(faces, IDs)
recognizer.write("Recognizer/Training Data.yml")
cv.destroyAllWindows()

camera.release()
cv.destroyAllWindows()