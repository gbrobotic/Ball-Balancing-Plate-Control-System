def computePD(target, current, prevError, kp, kd, dt, maxAngle):

    error = target - current

    derivative = (error - prevError) / dt

    output = kp * error + kd * derivative

    output = max(min(output, maxAngle), -maxAngle)

    return output, error