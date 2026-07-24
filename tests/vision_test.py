import cv2
from simulator import *
from vision import *

startSimulation()

while isSimulationRunning():

    frame = getCameraImage()

    x, y = detectBall(frame)

    if x is not None:

        print(f"Pixel : ({x}, {y})")

        cv2.circle(frame, (x, y), 8, (0,255,0), 2)

        cv2.putText(
            frame,
            f"({x},{y})",
            (x+10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0),
            2
        )

    display = cv2.resize(frame, (800,800))

    cv2.imshow("Vision Test", display)

    if cv2.waitKey(1) == 27:
        break

stopSimulation()

cv2.destroyAllWindows()