import math, pyfirmata2, cv2
from pyfirmata2 import SERVO
import mediapipe as mp
import numpy as np

board = pyfirmata2.Arduino("/dev/cu.usbmodem101")

# Servo Setup
board.digital[9].mode = board.digital[5].mode = board.digital[3].mode = board.digital[10].mode = board.digital[11].mode = SERVO
indexFinger, middleFinger, ringFinger, thumb, pinkyFinger = board.digital[9], board.digital[3], board.digital[5], board.digital[10], board.digital[11]

# Lists values in dictionary correspond to hand landmark numbers
ServoLandmarkDict = {thumb:[4,2,0], indexFinger:[8,5,1], middleFinger:[12,9,0], ringFinger:[16,13,0], pinkyFinger:[20,17,0]}

def mapAngle(angle, in_min, in_max, out_min, out_max): # Maps the captured angle of bent fingers to angles that servos can respond and move to
    angle = (angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # If mapped angle is out of range, write max/min value servo should move to
    if angle > out_max:
        return out_max
    elif angle < out_min:
        return out_min
    else:
        return angle

def getAngle(landmark1,landmark2,landmark3, plane): # Using 2D vectors for planar joint angles is simpler, faster, and avoids 3D ambiguity.
    if plane == "yz": # All fingers except thumb
        vec1 = np.array([landmark1.z - landmark2.z, landmark1.y - landmark2.y])
        vec2 = np.array([landmark3.z - landmark2.z, landmark3.y - landmark2.y])
    else: # Thumb moves in xz plane
        vec1 = np.array([landmark1.z - landmark2.z, landmark1.x - landmark2.x])
        vec2 = np.array([landmark3.z - landmark2.z, landmark3.x - landmark2.x])
    angle = abs(np.degrees(np.arctan2(vec2[0], vec2[1]) - np.arctan2(vec1[0], vec1[1])))
    return angle