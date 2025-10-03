import os
import cv2
import faceDetection as fd

if __name__ == "__main__":
    print("Type image path to detect faces: ")
    test_img_path = input()

    if not os.path.exists(test_img_path):
        print(f"Image not found: {test_img_path}")
    else:
        test_img = cv2.imread(test_img_path)

        if test_img is None:
            print("Error loading image.")
        else:
            face, gray = fd.detectFace(test_img)

            if len(face) > 0:  # Corrects from 'if face is not None:'
                name = {0: "me", 1: "other"}
                faces, facesID = fd.training_data("./facce")
                faceRecognizer = fd.train_classifier(faces, facesID)
                faceRecognizer.save("trainedData.yml")

                for detected_face in face:  # Changed 'face' to 'detected_face' for clarity
                    (x, y, w, h) = detected_face
                    region = gray[y:y + h, x:x + w]
                    label, confidence = faceRecognizer.predict(region)  # Corrected to call the method properly
                    print("Confidence:", confidence)
                    print("Label:", label)
                    fd.draw_rect(test_img, detected_face)
                    predicted_name = name.get(label, "unknown")  # Improved name retrieval
                    if confidence < 60:  # Confidence threshold for name assignment
                        continue
                    fd.put_name(test_img, predicted_name, x, y)

            resized = cv2.resize(test_img, (800, 600))
            cv2.imshow("Face Detected", resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()