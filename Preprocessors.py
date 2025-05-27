import math, pyfirmata2, cv2
import mediapipe as mp
from pyfirmata2 import SERVO
import numpy as np

board = pyfirmata2.Arduino("/dev/cu.usbmodem101")

# Servo Setup
board.digital[9].mode = SERVO
indexFinger =  board.digital[9]

def mapAngle(angle, in_min, in_max, out_min, out_max):
    angle = (angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if angle > 180:
        return 180
    elif angle < 0:
        return 0
    else:
        return angle

def getAngle(joint1, joint2, unknownAngle):
    angle = (math.atan2((unknownAngle.y - joint2.y),(unknownAngle.x - joint2.x)) - math.atan2((joint1.y - unknownAngle.y), (joint1.x - unknownAngle.x)))
    return angle