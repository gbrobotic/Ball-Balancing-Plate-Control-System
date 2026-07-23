import csv
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

filename = datetime.now().strftime("logs/run_%Y%m%d_%H%M%S.csv")

csvFile = open(filename, "w", newline="")

writer = csv.writer(csvFile)

writer.writerow([
    "Time",
    "BallX",
    "BallY",
    "ErrorX",
    "ErrorY",
    "ServoX",
    "ServoY"
])


def logData(time, ballX, ballY, errorX, errorY, servoX, servoY):

    writer.writerow([
        time,
        ballX,
        ballY,
        errorX,
        errorY,
        servoX,
        servoY
    ])


def closeLogger():
    csvFile.close()