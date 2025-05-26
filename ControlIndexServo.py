from Preprocessors import *

def controlIndex(joint1landmark, joint2landmark):
    dist = getDistance(joint1landmark, joint2landmark)
    angle = mapAngle(dist, 0.1, 0.36, 0, 180)
    print(angle)
    #indexFinger.write(angle)