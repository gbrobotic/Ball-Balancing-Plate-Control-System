import cv2
import numpy as np

from simulator import getCameraImage

points = []


def mouseCallback(event, x, y, flags, param):

    global points

    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:

        points.append([x, y])

        print(f"Point {len(points)} : ({x}, {y})")


cv2.namedWindow("Calibration", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Calibration", 800, 800)

cv2.setMouseCallback("Calibration", mouseCallback)


while True:

    frame = getCameraImage()

    display = frame.copy()

    # Draw clicked points
    for i, p in enumerate(points):

        cv2.circle(display, tuple(p), 6, (0, 0, 255), -1)

        cv2.putText(
            display,
            str(i + 1),
            (p[0] + 10, p[1]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Calibration", display)

    key = cv2.waitKey(1)

    if key == 27:
        break

    if len(points) == 4:
        break

cv2.destroyAllWindows()

print("\nSelected Points")
print(points)