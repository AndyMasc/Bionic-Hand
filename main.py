from HandControlSetup import *
from ControlServo import *
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        success, frame = cap.read()
        if success:
            RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=RGB_frame)
            results = landmarker.detect(mp_image)

            if results.hand_landmarks:
                handLandmarks = results.hand_landmarks[0]

                for servo, lm in ServoLandmarkDict.items():
                    controlServo(servo, handLandmarks[lm[0]], handLandmarks[lm[1]], handLandmarks[lm[2]])

                # Draw landmarks manually
                for landmark in handLandmarks:
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            cv2.imshow('Video Feed', cv2.flip(frame, 1))
            if cv2.waitKey(1) == ord('q'):
                break

cv2.destroyAllWindows()