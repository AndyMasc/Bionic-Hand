import math, pyfirmata2, cv2
from pyfirmata2 import SERVO
import mediapipe as mp
import numpy as np

board = pyfirmata2.Arduino("/dev/cu.usbmodem101")

# Servo Setup
board.digital[9].mode = board.digital[5].mode = board.digital[3].mode = board.digital[10].mode = board.digital[11].mode = SERVO

indexFinger =  board.digital[9]
middleFinger = board.digital[5]
ringFinger = board.digital[3]
thumb = board.digital[10]
pinkyFinger = board.digital[11]

# Lists values in dictionary correspond to hand landmark numbers
ServoLandmarkDict = {thumb:[4,3,2], indexFinger:[8,5,1], middleFinger:[12,9,0], ringFinger:[16,13,0], pinkyFinger:[20,17,0]}

def mapAngle(angle, in_min, in_max, out_min, out_max):
    angle = (angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if angle > out_max:
        return out_max
    elif angle < out_min:
        return out_min
    else:
        return angle

def getAngle(landmark1,landmark2,landmark3): #landmark2 = unknown angle
    vec1 = np.array([landmark1.y - landmark2.y, landmark1.z - landmark2.z])
    vec2 = np.array([landmark3.y - landmark2.y, landmark3.z - landmark2.z])
    angle = abs(np.degrees(np.arctan2(vec2[1], vec2[0]) - np.arctan2(vec1[1], vec1[0])))
    return angle