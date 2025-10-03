import cv2
import os
import numpy as np
face = cv2.face


def detectFace(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_face = cv2.CascadeClassifier(r"./haar/haarcascade_frontalface_default.xml")

    if haar_face.empty():
        raise Exception("Haar cascade file not found or unable to load.")

    face = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return face, gray


def training_data(directory):
    faces = []
    facesID = []

    for path, subdir, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Found dotfile, skipping...")
                continue

            id = os.path.basename(path) 
            image_path = os.path.join(path, filename)
            img_test = cv2.imread(image_path)
            if img_test is None:
                print(f"Error opening image: {image_path}")
                continue

            face, gray = detectFace(img_test)
            if len(face) != 1:
                print(f"Found {len(face)} faces in image {filename}, skipping...")
                continue

            (x, y, w, h) = face[0]
            region = gray[y:y + h, x:x + w] 
            faces.append(region)
            facesID.append(int(id))

    return faces, facesID


def train_classifier(faces, facesID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(facesID))
    return face_recognizer


def draw_rect(test_img, face):
    (x, y, w, h) = face
    cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 0, 255), thickness=5)


def put_name(test_img, text, x, y):
    cv2.putText(test_img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
