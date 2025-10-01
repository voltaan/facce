import cv2
import os
import numpy as np
import faceDetection as fd

test_img_path = "./facce/0/picture_2025-10-01_20-02-20.jpg"
if not os.path.exists(test_img_path):
    print(f"Image not found: {test_img_path}")
else:
    test_img = cv2.imread(test_img_path)

    if test_img is None:
        print("Error loading image.")
    else:
        face, gray = fd.faceDetection(test_img)

        if face is not None:
            for (x, y, w, h) in face:
                cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 0, 255), thickness=5)

        resized = cv2.resize(test_img, (1920, 1080))

        cv2.imshow("Face Detected", resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
