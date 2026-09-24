import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# -----------------------------
# Face Landmarker Model
# -----------------------------
MODEL_PATH = "face_landmarker.task"

base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    num_faces=1
)

detector = vision.FaceLandmarker.create_from_options(options)


# -----------------------------
# Camera
# -----------------------------
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera.")
    detector.close()
    exit()


# -----------------------------
# Eye landmark indexes
# -----------------------------
# MediaPipe Face Landmarker has 478 landmarks
# These indexes represent important points around the eyes.

LEFT_EYE = [
    33, 133, 159, 145, 158, 153
]

RIGHT_EYE = [
    362, 263, 386, 374, 385, 380
]


# -----------------------------
# Main Loop
# -----------------------------
while True:

    success, frame = camera.read()

    if not success:
        print("Could not read camera.")
        break

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    results = detector.detect(mp_image)

    if results.face_landmarks:

        face = results.face_landmarks[0]

        height, width, _ = frame.shape

        # -------------------------
        # LEFT EYE
        # -------------------------
        for index in LEFT_EYE:

            landmark = face[index]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            cv2.circle(
                frame,
                (x, y),
                4,
                (255, 0, 0),
                -1
            )


        # -------------------------
        # RIGHT EYE
        # -------------------------
        for index in RIGHT_EYE:

            landmark = face[index]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            cv2.circle(
                frame,
                (x, y),
                4,
                (255, 0, 0),
                -1
            )


        cv2.putText(
            frame,
            "EYES DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:

        cv2.putText(
            frame,
            "NO FACE",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )


    cv2.imshow(
        "Eye Reel Control - Eye Detection",
        frame
    )


    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------
camera.release()
detector.close()
cv2.destroyAllWindows()