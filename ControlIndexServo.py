from Preprocessors import *

def controlIndex(joint1landmark, joint2landmark, angle):
    angle = getAngle(joint1landmark, joint2landmark, angle)
    angle = mapAngle(angle, 57, 140, 0, 180)
    print(angle)
    #indexFinger.write(angle)