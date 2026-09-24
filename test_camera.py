import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not access the camera.")
    exit()

print("Camera started successfully.")
print("Press Q to close.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read camera.")
        break

    cv2.imshow("Eye Reel Control - Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()