import sys
import time

from simulator import *
from controller import *
from config import *
from dashboard import *

startSimulation()

app = QApplication(sys.argv)

dashboard = Dashboard()

dashboard.show()
prevErrorX = 0
prevErrorY = 0
currentTime = 0
currentTime = 0

while isSimulationRunning():

    currentTime += DT

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

    setPlateAngle(servoX, servoY)

    dashboard.setGraphData(
        currentTime,
        currentX,
        errorX,
        servoX
    )
    dashboard.updateStatus(
    currentTime,
    currentX,
    currentY,
    errorX,
    errorY,
    servoX,
    servoY
    )
    app.processEvents()

    prevErrorX = errorX
    prevErrorY = errorY

    time.sleep(DT)


stopSimulation()