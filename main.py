from HandControlSetup import *
from ControlServo import *

# main
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hand = mpHands.Hands(max_num_hands = 1)

while True:
    success, frame = cap.read()

    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand.process(RGB_frame)

        if results.multi_hand_landmarks:
            handLandmarks = results.multi_hand_landmarks[0]
            mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)

            for servo,lm in ServoLandmarkDict.items():
                controlServo(servo, handLandmarks.landmark[lm[0]], handLandmarks.landmark[lm[1]], handLandmarks.landmark[lm[2]])

        cv2.imshow('Video Feed', cv2.flip(frame,1))
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()