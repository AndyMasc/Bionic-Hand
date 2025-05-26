from Preprocessors import *

def controlIndex(joint1landmark, joint2landmark, unknownAngleLandmark):
    angle = getAngle(joint1landmark, joint2landmark, unknownAngleLandmark)
    angle = mapAngle(angle, 57,140,0,180)
    indexFinger.write(angle)