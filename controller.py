def computePD(target, current, prevError, kp, kd, dt, maxAngle):

    # Position Error
    error = target - current

    # Derivative Term
    derivative = (error - prevError) / dt

    # PD Output
    output = kp * error + kd * derivative

    # Output Saturation
    output = max(min(output, maxAngle), -maxAngle)

    return output, error