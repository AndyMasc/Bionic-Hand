from Preprocessors import *

def controlIndex(joint1landmark, joint2landmark, joint3landmark):
    angle = round(getAngle(joint1landmark, joint2landmark, joint3landmark))
    angle = mapAngle(angle, 1900, 9410, 0, 180)
    print(angle)
    indexFinger.write(angle)