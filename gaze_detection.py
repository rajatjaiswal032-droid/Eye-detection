import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# -----------------------------
# MediaPipe Face Landmarker
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
# Landmark indexes
# -----------------------------

# Left eye
LEFT_EYE_LEFT = 33
LEFT_EYE_RIGHT = 133
LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145

# Right eye
RIGHT_EYE_LEFT = 362
RIGHT_EYE_RIGHT = 263
RIGHT_EYE_TOP = 386
RIGHT_EYE_BOTTOM = 374

# Iris
LEFT_IRIS = [468, 469, 470, 471, 472]
RIGHT_IRIS = [473, 474, 475, 476, 477]


# -----------------------------
# Function: iris center
# -----------------------------
def get_iris_center(face, indexes, width, height):

    x = 0
    y = 0

    for index in indexes:
        landmark = face[index]

        x += landmark.x * width
        y += landmark.y * height

    x /= len(indexes)
    y /= len(indexes)

    return x, y


# -----------------------------
# Function: calculate gaze
# -----------------------------
def calculate_gaze(face, width, height):

    # Iris centers
    left_iris_x, left_iris_y = get_iris_center(
        face,
        LEFT_IRIS,
        width,
        height
    )

    right_iris_x, right_iris_y = get_iris_center(
        face,
        RIGHT_IRIS,
        width,
        height
    )

    # Average iris position
    iris_x = (left_iris_x + right_iris_x) / 2
    iris_y = (left_iris_y + right_iris_y) / 2


    # Eye boundaries
    left_x1 = face[LEFT_EYE_LEFT].x * width
    left_x2 = face[LEFT_EYE_RIGHT].x * width

    right_x1 = face[RIGHT_EYE_LEFT].x * width
    right_x2 = face[RIGHT_EYE_RIGHT].x * width

    top_y1 = face[LEFT_EYE_TOP].y * height
    bottom_y1 = face[LEFT_EYE_BOTTOM].y * height

    top_y2 = face[RIGHT_EYE_TOP].y * height
    bottom_y2 = face[RIGHT_EYE_BOTTOM].y * height


    # Average eye boundaries
    eye_left = (left_x1 + right_x1) / 2
    eye_right = (left_x2 + right_x2) / 2

    eye_top = (top_y1 + top_y2) / 2
    eye_bottom = (bottom_y1 + bottom_y2) / 2


    # Normalize iris position
    eye_width = eye_right - eye_left
    eye_height = eye_bottom - eye_top

    if eye_width == 0 or eye_height == 0:
        return "CENTER", iris_x, iris_y


    normalized_x = (iris_x - eye_left) / eye_width
    normalized_y = (iris_y - eye_top) / eye_height


    # -----------------------------
    # Gaze thresholds
    # -----------------------------

    if normalized_y < 0.35:
        gaze = "UP"

    elif normalized_y > 0.65:
        gaze = "DOWN"

    elif normalized_x < 0.35:
        gaze = "LEFT"

    elif normalized_x > 0.65:
        gaze = "RIGHT"

    else:
        gaze = "CENTER"


    return gaze, iris_x, iris_y


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


        # Calculate gaze
        gaze, iris_x, iris_y = calculate_gaze(
            face,
            width,
            height
        )


        # Draw iris center
        cv2.circle(
            frame,
            (int(iris_x), int(iris_y)),
            7,
            (0, 255, 255),
            -1
        )


        # Display gaze
        cv2.putText(
            frame,
            f"GAZE: {gaze}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 255, 0),
            3
        )


    else:

        cv2.putText(
            frame,
            "NO FACE",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 0, 255),
            3
        )


    cv2.imshow(
        "Eye Reel Control - Gaze Detection",
        frame
    )


    # Q = Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------
camera.release()
detector.close()
cv2.destroyAllWindows()
