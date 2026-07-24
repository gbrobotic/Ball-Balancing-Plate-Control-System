import cv2
import numpy as np

# # Pixel coordinates (Calibration)
# imagePoints = np.float32([
#     [40,40],
#     [763,36],
#     [761,760],
#     [43,758]
# ])

# # Plate coordinates (meters)
# worldPoints = np.float32([
#     [-0.5, 0.5],
#     [ 0.5, 0.5],
#     [ 0.5,-0.5],
#     [-0.5,-0.5]
# ])

# H = cv2.getPerspectiveTransform(imagePoints, worldPoints)


def pixelToWorld(px, py):

    width = 800
    height = 800

    worldX = -(px - width/2) * (1.0 / width)
    worldY =  (py - height/2) * (1.0 / height)

    return worldX, worldY
def detectBall(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray,(7,7),0)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=30,
        param1=80,
        param2=20,
        minRadius=5,
        maxRadius=40
    )

    if circles is None:
        return None,None

    circles = circles[0]

    x,y,r = circles[0]

    return int(x),int(y)
