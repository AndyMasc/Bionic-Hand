from Preprocessors import *

def controlPinky(landmark1, landmark2, landmark3):
    angle = getAngle(landmark1, landmark2, landmark3)
    angle = round(mapAngle(angle, 33, 164, 0, 180))
    pinkyFinger.write(angle)