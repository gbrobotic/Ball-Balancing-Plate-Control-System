from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import math

client = RemoteAPIClient()
sim = client.require('sim')

# Get joints
jointX = sim.getObject('/RotateX')
jointY = sim.getObject('/RotateY0')

print("Joint X:", jointX)
print("Joint Y:", jointY)

# Move X servo by 10 degrees
sim.setJointTargetPosition(jointX, math.radians(10))

time.sleep(3)

# Move back
sim.setJointTargetPosition(jointX, 0)