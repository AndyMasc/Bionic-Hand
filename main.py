from Preprocessors import *

from ControlIndexServo import *
from ControlMiddleServo import *
from ControlRingServo import *
from ControlThumbServo import *
from ControlPinkyServo import *

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

            controlIndex(handLandmarks.landmark[8], handLandmarks.landmark[5], handLandmarks.landmark[1])
            controlMiddle(handLandmarks.landmark[12], handLandmarks.landmark[9], handLandmarks.landmark[0])
            controlRing(handLandmarks.landmark[16], handLandmarks.landmark[13], handLandmarks.landmark[0])
            controlThumb(handLandmarks.landmark[4], handLandmarks.landmark[3], handLandmarks.landmark[2])
            controlPinky(handLandmarks.landmark[20], handLandmarks.landmark[17], handLandmarks.landmark[0])

        cv2.imshow('Video Feed', cv2.flip(frame, 1))
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()