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
# Iris landmark indexes
# -----------------------------
# Left iris
LEFT_IRIS = [468, 469, 470, 471, 472]

# Right iris
RIGHT_IRIS = [473, 474, 475, 476, 477]


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
        # Left Iris
        # -------------------------
        left_x = 0
        left_y = 0

        for index in LEFT_IRIS:

            landmark = face[index]

            left_x += int(landmark.x * width)
            left_y += int(landmark.y * height)

        left_x //= len(LEFT_IRIS)
        left_y //= len(LEFT_IRIS)

        cv2.circle(
            frame,
            (left_x, left_y),
            6,
            (0, 255, 255),
            -1
        )


        # -------------------------
        # Right Iris
        # -------------------------
        right_x = 0
        right_y = 0

        for index in RIGHT_IRIS:

            landmark = face[index]

            right_x += int(landmark.x * width)
            right_y += int(landmark.y * height)

        right_x //= len(RIGHT_IRIS)
        right_y //= len(RIGHT_IRIS)

        cv2.circle(
            frame,
            (right_x, right_y),
            6,
            (0, 255, 255),
            -1
        )


        cv2.putText(
            frame,
            "IRIS DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
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
        "Eye Reel Control - Iris Detection",
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