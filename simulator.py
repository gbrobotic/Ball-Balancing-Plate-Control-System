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


def movePlate(angleX, angleY):

    sim.setJointTargetPosition(jointX, angleX)

    sim.setJointTargetPosition(jointY, angleY)