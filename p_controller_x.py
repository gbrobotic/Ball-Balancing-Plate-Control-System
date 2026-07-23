from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import csv
import pyqtgraph as pg
client = RemoteAPIClient()
sim = client.require('sim')

ball = sim.getObject('/Ball')
plate = sim.getObject('/Plate')
jointX = sim.getObject('/RotateX')
jointY = sim.getObject('/RotateY0')


Kp = 60.0
Kd = 3
targetX = 0.0
targetY = 0.0
prevErrorX = 0.0
prevErrorY = 0.0
dt = 0.01

def getBallPosition():
    pos = sim.getObjectPosition(ball, plate)
    return pos[0], pos[1]
def computePD(target, current, prevError, Kp, Kd, dt):

    error = target - current

    derivative = (error - prevError) / dt

    output = Kp * error + Kd * derivative

    output = max(min(output, 0.5), -0.5)

    return output, error

logFile = open("ball_plate_data.csv", "w", newline="")
writer = csv.writer(logFile)

writer.writerow([
    "Time",
    "BallX",
    "BallY",
    "ErrorX",
    "ErrorY",
    "ServoX",
    "ServoY"
])

startTime = time.time()
while True:

    currentX, currentY = getBallPosition()
    servoAngleX, errorX = computePD(targetX, currentX, prevErrorX, Kp, Kd, dt)
    servoAngleY, errorY = computePD(targetY, currentY, prevErrorY, Kp, Kd, dt)

    sim.setJointTargetPosition(jointX, servoAngleX)
    sim.setJointTargetPosition(jointY, servoAngleY)
    currentTime = time.time() - startTime

    writer.writerow([
        currentTime,
        currentX,
        currentY,
        errorX,
        errorY,
        servoAngleX,
        servoAngleY
    ])
    prevErrorX = errorX
    prevErrorY = errorY
    time.sleep(0.01)