import math, pyfirmata2, cv2
import mediapipe as mp
from pyfirmata2 import SERVO

#board = pyfirmata2.Arduino("/dev/cu.usbmodem101")

# Servo Setup
#board.digital[9].mode = SERVO
#indexFinger =  board.digital[9]

def mapAngle(x, in_min, in_max, out_min, out_max):
    angle = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if angle > 180:
        return 180
    elif angle < 0:
        return 0
    else:
        return angle

def getDistance(joint1, joint2):
    return math.sqrt((joint1.x - joint2.x) ** 2 + (joint1.y - joint2.y) ** 2)