import sys
import time

from simulator import *
from controller import *
from config import *
from dashboard import *
from logger import *
from trajectory import *


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


while isSimulationRunning():

    currentTime += DT
    mode = dashboard.getTrajectory()
    
    if mode == "Manual":
        targetX = dashboard.targetXSpin.value()
        targetY = dashboard.targetYSpin.value()
    
    elif mode == "Point":
        targetX, targetY = point()
    
    elif mode == "Line":
        targetX, targetY = line(currentTime)
    
    elif mode == "Circle":
        targetX, targetY = circle(currentTime)
    
    elif mode == "Figure-8":
        targetX, targetY = figure8(currentTime)
    currentX, currentY = getBallPosition()

    servoX, errorX = computePD(
        # dashboard.targetXSpin.value(),
        targetX,
        currentX,
        prevErrorX,
        dashboard.kpSpin.value(),
        dashboard.kdSpin.value(),
        DT,
        MAX_ANGLE
    )

    servoY, errorY = computePD(
        # dashboard.targetYSpin.value(),
        targetY,
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
    # dashboard.targetXSpin.value(),
    # dashboard.targetYSpin.value(),
    targetX,
    targetY,
    KP,
    KD
)
    logData(
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

    # print(
    #     dashboard.kpSpin.value(),
    #     dashboard.kdSpin.value()
    # )
stopSimulation()
closeLogger()