from Preprocessors import *

def controlThumb(landmark1, landmark2, landmark3):
    angle = getAngle(landmark1, landmark2, landmark3)
    angle = round(mapAngle(angle, 80, 150, 0, 180))
    thumb.write(angle)