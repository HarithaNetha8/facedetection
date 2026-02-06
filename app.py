import cv2
import threading
from deepface import DeepFace

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

reference_img = cv2.imread("reference.jpg")
reference_img = cv2.resize(reference_img, (640, 480))

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(
            frame,
            reference_img,
            detector_backend='opencv',
            enforce_detection=False
        )
        face_match = result["verified"]
    except:
        face_match = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if counter % 30 == 0:
        threading.Thread(target=check_face, args=(frame.copy(),)).start()

    counter += 1

    if face_match:
        cv2.putText(frame, "MATCH!", (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "NO MATCH!", (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("Face Verification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
