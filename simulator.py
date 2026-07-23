from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require('sim')

ball = sim.getObject('/Ball')
plate = sim.getObject('/Plate')

jointX = sim.getObject('/RotateX')
jointY = sim.getObject('/RotateY0')


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