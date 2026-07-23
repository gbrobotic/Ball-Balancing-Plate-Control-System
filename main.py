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
dashboard.resetButton.clicked.connect(resetBall)
dashboard.pauseButton.clicked.connect(pauseSimulation)
dashboard.resumeButton.clicked.connect(resumeSimulation)
prevErrorX = 0
prevErrorY = 0
currentTime = 0
currentTime = 0

while isSimulationRunning():

    currentTime += DT

    currentX, currentY = getBallPosition()

    servoX, errorX = computePD(
        dashboard.targetXSpin.value(),
        currentX,
        prevErrorX,
        dashboard.kpSpin.value(),
        dashboard.kdSpin.value(),
        DT,
        MAX_ANGLE
    )

    servoY, errorY = computePD(
        dashboard.targetYSpin.value(),
        currentY,
        prevErrorY,
        dashboard.kpSpin.value(),
        dashboard.kdSpin.value(),
        DT,
        MAX_ANGLE
    )

    setPlateAngle(servoX, servoY)

    dashboard.setGraphData(
        currentTime,
        currentX,
        currentY,
        errorX,
        errorY,
        servoX,
        servoY
    )
    dashboard.updateStatus(
    currentTime,
    currentX,
    currentY,
    errorX,
    errorY,
    servoX,
    servoY,
    dashboard.targetXSpin.value(),
    dashboard.targetYSpin.value(),
    KP,
    KD
)
    app.processEvents()

    prevErrorX = errorX
    prevErrorY = errorY

    time.sleep(DT)

    print(
        dashboard.kpSpin.value(),
        dashboard.kdSpin.value()
    )
stopSimulation()