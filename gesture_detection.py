import cv2
import mediapipe as mp
import time

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
LEFT_EYE_LEFT = 33
LEFT_EYE_RIGHT = 133
LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145

RIGHT_EYE_LEFT = 362
RIGHT_EYE_RIGHT = 263
RIGHT_EYE_TOP = 386
RIGHT_EYE_BOTTOM = 374

LEFT_IRIS = [468, 469, 470, 471, 472]
RIGHT_IRIS = [473, 474, 475, 476, 477]


# -----------------------------
# Settings
# -----------------------------
HOLD_TIME = 0.6
COOLDOWN_TIME = 1.5

current_gaze = "CENTER"

gesture_start_time = None
last_gesture_time = 0

last_detected_gesture = "NONE"


# -----------------------------
# Iris center
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
# Calculate gaze
# -----------------------------
def calculate_gaze(face, width, height):

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

    iris_x = (left_iris_x + right_iris_x) / 2
    iris_y = (left_iris_y + right_iris_y) / 2


    left_eye_left = face[LEFT_EYE_LEFT].x * width
    left_eye_right = face[LEFT_EYE_RIGHT].x * width

    right_eye_left = face[RIGHT_EYE_LEFT].x * width
    right_eye_right = face[RIGHT_EYE_RIGHT].x * width

    left_eye_top = face[LEFT_EYE_TOP].y * height
    left_eye_bottom = face[LEFT_EYE_BOTTOM].y * height

    right_eye_top = face[RIGHT_EYE_TOP].y * height
    right_eye_bottom = face[RIGHT_EYE_BOTTOM].y * height


    eye_left = (left_eye_left + right_eye_left) / 2
    eye_right = (left_eye_right + right_eye_right) / 2

    eye_top = (left_eye_top + right_eye_top) / 2
    eye_bottom = (left_eye_bottom + right_eye_bottom) / 2


    eye_width = eye_right - eye_left
    eye_height = eye_bottom - eye_top


    if eye_width == 0 or eye_height == 0:
        return "CENTER", iris_x, iris_y


    normalized_x = (iris_x - eye_left) / eye_width
    normalized_y = (iris_y - eye_top) / eye_height


    # Gaze thresholds
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


    gesture_message = "NONE"


    if results.face_landmarks:

        face = results.face_landmarks[0]

        height, width, _ = frame.shape


        # Calculate gaze
        gaze, iris_x, iris_y = calculate_gaze(
            face,
            width,
            height
        )

        current_gaze = gaze


        # Draw iris center
        cv2.circle(
            frame,
            (int(iris_x), int(iris_y)),
            7,
            (0, 255, 255),
            -1
        )


        # -----------------------------
        # Gesture detection
        # -----------------------------

        current_time = time.time()


        if gaze == "DOWN" or gaze == "UP":

            # Start timer
            if gesture_start_time is None:
                gesture_start_time = current_time

            elapsed_time = current_time - gesture_start_time


            # Check hold time
            if elapsed_time >= HOLD_TIME:

                # Check cooldown
                if current_time - last_gesture_time >= COOLDOWN_TIME:

                    if gaze == "DOWN":

                        gesture_message = "NEXT REEL"

                    elif gaze == "UP":

                        gesture_message = "PREVIOUS REEL"


                    last_detected_gesture = gesture_message

                    last_gesture_time = current_time

                    # Reset timer
                    gesture_start_time = None


        else:

            # Reset if gaze returns to center/side
            gesture_start_time = None


        # -----------------------------
        # Display gaze
        # -----------------------------
        cv2.putText(
            frame,
            f"GAZE: {gaze}",
            (20, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )


        # Display last gesture
        cv2.putText(
            frame,
            f"GESTURE: {last_detected_gesture}",
            (20, 85),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )


    else:

        current_gaze = "NO FACE"

        gesture_start_time = None

        cv2.putText(
            frame,
            "NO FACE",
            (20, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )


    # -----------------------------
    # Show camera
    # -----------------------------
    cv2.imshow(
        "Eye Reel Control - Gesture Detection",
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