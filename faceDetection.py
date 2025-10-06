import cv2

faceCascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')

def detectFace(width, height, flip=+1, scaleFactor=1.2, minNeighbors=5, red=255, green=0, blue=0):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    while True:
        ret, img = cap.read()
        img = cv2.flip(img, flip)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (red, green, blue), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        cv2.imshow('face detection - press esc to close', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def detectEye(width, height, flip=+1, scaleFactor=1.2, minNeighbors=5, eyeScaleFactor=1.5, eyeMinNeighbors=10, red=255,
              green=0, blue=0, eyeRed=0, eyeGreen=255, eyeBlue=0):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    while True:
        ret, img = cap.read()
        img = cv2.flip(img, flip)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=(30, 30)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (red, green, blue), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor=eyeScaleFactor,
                minNeighbors=eyeMinNeighbors,
                minSize=(5, 5)
            )
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (eyeRed, eyeGreen, eyeBlue), 2)

        cv2.imshow('eye detection - press esc to close', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
