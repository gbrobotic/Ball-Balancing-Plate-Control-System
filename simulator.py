from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import cv2
client = RemoteAPIClient()
sim = client.require('sim')

ball = sim.getObject('/Ball')
plate = sim.getObject('/Plate')

jointX = sim.getObject('/RotateX')
jointY = sim.getObject('/RotateY0')

cam = sim.getObject('/Cam')


def getBallPosition():

    pos = sim.getObjectPosition(ball, plate)

    return pos[0], pos[1]


def setPlateAngle(angleX, angleY):

    sim.setJointTargetPosition(jointX, angleX)

    sim.setJointTargetPosition(jointY, angleY)

def startSimulation():
    sim.startSimulation()

def stopSimulation():
    sim.stopSimulation()
def getSimulationState():
    return sim.getSimulationState()

def isSimulationRunning():
    return sim.getSimulationState() != sim.simulation_stopped

def resetBall():

    # Plate ko seedha karo
    setPlateAngle(0, 0)

    # Ball ko plate ke center me rakho
    sim.setObjectPosition(ball, plate, [0, 0, 0.05])

    # Ball ki linear aur angular velocity reset karo
    # sim.setObjectVelocity(ball, [0, 0, 0], [0, 0, 0])
     # Reset dynamics (agar supported ho)
    sim.resetDynamicObject(ball)


def pauseSimulation():
    sim.pauseSimulation()


def resumeSimulation():
    sim.startSimulation()


def getCameraImage():

    image, resolution = sim.getVisionSensorImg(cam)

    img = np.frombuffer(image, dtype=np.uint8)
    img = img.reshape(resolution[1], resolution[0], 3)

    img = cv2.flip(img, 0)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return img