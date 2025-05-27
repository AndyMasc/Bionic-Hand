from Preprocessors import *

def controlIndex(joint1landmark, joint2landmark, angle):
    angle = getAngle(joint1landmark, joint2landmark, angle)
    angle = mapAngle(angle, 2.54, 2.75, 0, 180)
    indexFinger.write(angle)