'''from Preprocessors import *

def controlRing(landmark1, landmark2, landmark3):
    angle = getAngle(landmark1, landmark2, landmark3)
    angle = round(mapAngle(angle, 33, 164, 0, 180))
    ringFinger.write(angle)'''

from Preprocessors import *

def controlServo(servo, landmark1, landmark2, landmark3):
    angle = getAngle(landmark1, landmark2, landmark3)
    angle = round(mapAngle(angle, 33, 164, 0, 180))
    servo.write(angle)