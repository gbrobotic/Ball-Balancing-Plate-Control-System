import math

def point():
    return 0.0, 0.0


def line(t):
    speed = 0.08   # m/s
    x = min(speed * t, 0.30)
    y = 0.0
    return x, y


def circle(t):
    radius = 0.05
    omega = 0.9

    x = radius * math.cos(omega * t)
    y = radius * math.sin(omega * t)

    return x, y


def figure8(t):

    A = 0.05      # X radius
    B = 0.025     # Y radius
    omega = 1.0

    x = A * math.sin(omega * t)
    y = B * math.sin(2 * omega * t)

    return x, y