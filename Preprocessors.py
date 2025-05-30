import math, pyfirmata2, cv2
from pyfirmata2 import SERVO
import mediapipe as mp
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

def getAngle(a,b,c):
        a = np.array([a.y - b.y, a.z - b.z])
        b = np.array([c.y - b.y, c.z - b.z])
        angle = abs(math.degrees(np.arctan2(b[1], b[0]) - np.arctan2(a[1], a[0])))
        return angle