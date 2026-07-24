import cv2

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
def pixelToWorld(px, py, width=800, height=800, plateSize=1.0):

    worldX = (px / width - 0.5) * plateSize

    worldY = -(py / height - 0.5) * plateSize

    return worldX, worldY