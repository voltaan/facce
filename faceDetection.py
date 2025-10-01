import cv2
import os
import numpy as np


def faceDetection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_face = cv2.CascadeClassifier(r".\haar\haarcascade_frontalface_default.xml")
    face = haar_face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return face, gray


def training_data(directory):
    faces = []
    facesID = []

    for path, subdir, filename in os.walk(directory):
        for filename in filename:
            if filename.startsWith("."):
                print("Found dotfile, skipping...")
                continue
            id = os.path.basename(filename)
            image_path = os.path.join(path, filename)
            img_test = cv2.imread(image_path)
            if img_test is None:
                print("Error opening image")
                continue
            face, gray = faceDetection(img_test)
            if len(face) != 1:
                continue
            (x, y, w, h) = face[0]
            region = gray[y : y + w, x : x + h]
            faces.append(region)
            facesID.append(int(id))
    return faces, facesID
