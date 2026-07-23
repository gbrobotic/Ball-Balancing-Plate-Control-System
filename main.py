from simulator import *
from controller import *
from config import *

import time

prevErrorX = 0
prevErrorY = 0

while True:

    currentX, currentY = getBallPosition()

    servoX, errorX = computePD(
        TARGET_X,
        currentX,
        prevErrorX,
        KP,
        KD,
        DT,
        MAX_ANGLE
    )

    servoY, errorY = computePD(
        TARGET_Y,
        currentY,
        prevErrorY,
        KP,
        KD,
        DT,
        MAX_ANGLE
    )

    movePlate(servoX, servoY)

    prevErrorX = errorX
    prevErrorY = errorY

    time.sleep(DT)