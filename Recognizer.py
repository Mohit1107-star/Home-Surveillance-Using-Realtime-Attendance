import cv2 as cv
import numpy as np
import _sqlite3 as sqlite
from notify_run import Notify

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("Recognizer/Training Data.yml")


def recognizePerson(x, y, w, h, image, grayImage):
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    ID, confidence = recognizer.predict(grayImage[y:y + h, x:x + w])
    confidence = "%.2f" % confidence
    if float(confidence)<60:
        profile = getPersonProfile(ID)
        if profile != None:
            cv.putText(image, str(profile[1]) + " - " + str(confidence) + "%", (x, y + h), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
            cv.putText(image, str(profile[2]), (x, y + h + 30), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    else:
        print(confidence)
        notify = Notify()
        notify.send("Perimeter compromised... Sending Team Alpha for preliminary action...")

    return image


def getPersonProfile(ID):
    connection = sqlite.connect("PeopleData.db")
    command = "SELECT * FROM PeopleDetails WHERE ID = " + str(ID)
    cursor = connection.execute(command)
    profile = None
    for row in cursor:
        profile = row
    connection.close()

    return profile


