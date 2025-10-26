from HandControlSetup import *

def controlServo(servo, landmark1, landmark2, landmark3):
    angle = getAngle(landmark1, landmark2, landmark3, 'yz')
    if servo == thumb: # Thumb moves in different plane compared to other fingers and requires different mapping values
        angle = getAngle(landmark1, landmark2, landmark3, 'xz') # Thumb moves in xz plane compared to yz plane for other fingers
        angle = round(mapAngle(angle, 175, 330, 0, 180))
    elif servo == pinkyFinger:
        angle = round(mapAngle(angle, 35, 176, 0, 180))
    else:
        angle = round(mapAngle(angle, 33, 164, 0, 180))
    servo.write(angle)