import math, pyfirmata2, cv2
import mediapipe as mp
from pyfirmata2 import SERVO
import numpy as np

#board = pyfirmata2.Arduino("/dev/cu.usbmodem101")

# Servo Setup
#board.digital[9].mode = SERVO
#indexFinger =  board.digital[9]

def mapAngle(angle, in_min, in_max, out_min, out_max):
    angle = (angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if angle > 180:
        return 180
    elif angle < 0:
        return 0
    else:
        return angle

def getAngle(joint1, joint2, unknownAngleJoint):
    vec1 = np.array([joint1.x - unknownAngleJoint.x, joint1.y - unknownAngleJoint.y, joint1.z - unknownAngleJoint.z])
    vec2 = np.array([joint2.x - unknownAngleJoint.x, joint2.y - unknownAngleJoint.y, joint2.z - unknownAngleJoint.z])
    dotProduct = np.dot(vec1, vec2)
    angle = math.degrees(math.acos(dotProduct / (abs(np.linalg.norm(vec2)) * abs(np.linalg.norm(vec1)))))
    return angle