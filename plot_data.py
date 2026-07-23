from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# CSV Load
csv_path = Path(__file__).with_name("ball_plate_data.csv")
data = pd.read_csv(csv_path)

# Graph 1 : Ball Position
plt.figure(figsize=(10,5))
plt.plot(data["Time"], data["BallX"], label="Ball X")
plt.plot(data["Time"], data["BallY"], label="Ball Y")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Ball Position")
plt.grid(True)
plt.legend()

# Graph 2 : Error
plt.figure(figsize=(10,5))
plt.plot(data["Time"], data["ErrorX"], label="Error X")
plt.plot(data["Time"], data["ErrorY"], label="Error Y")
plt.xlabel("Time (s)")
plt.ylabel("Error (m)")
plt.title("Control Error")
plt.grid(True)
plt.legend()

# Graph 3 : Servo Angle
plt.figure(figsize=(10,5))
plt.plot(data["Time"], data["ServoX"], label="Servo X")
plt.plot(data["Time"], data["ServoY"], label="Servo Y")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Servo Output")
plt.grid(True)
plt.legend()

plt.show()