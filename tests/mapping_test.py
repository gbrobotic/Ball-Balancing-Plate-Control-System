import cv2

from simulator import *
from vision import *

startSimulation()

while isSimulationRunning():

    frame = getCameraImage()

    px, py = detectBall(frame)

    if px is not None:

        sx, sy = getBallPosition()

        worldX, worldY = pixelToWorld(px, py)

        print(
            f"Vision : ({worldX:.3f}, {worldY:.3f})",
            f"Simulator : ({sx:.3f}, {sy:.3f})"
        )

        cv2.circle(frame, (px, py), 8, (0,255,0), 2)

    # Hamesha display banao
    display = cv2.resize(frame, (800,800))

    # Hamesha window show karo
    cv2.imshow("Mapping Test", display)

    if cv2.waitKey(1) == 27:
        break

stopSimulation()

cv2.destroyAllWindows()