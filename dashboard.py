from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

import pyqtgraph as pg
class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ball & Plate Dashboard")

        self.resize(1400, 800)
        # Central Widget
        self.centralWidget = QWidget()

        self.setCentralWidget(self.centralWidget)
        # Main Layout
        self.mainLayout = QHBoxLayout()

        self.centralWidget.setLayout(self.mainLayout)
        # Left Panel
        self.leftPanel = QWidget()
        # Left Panel Layout
        self.leftLayout = QVBoxLayout()
        
        self.leftPanel.setLayout(self.leftLayout)

        # Graph Area
        self.graphWidget = pg.GraphicsLayoutWidget()


        self.leftLayout.addWidget(self.graphWidget)

        # Ball Position Graph
        self.ballPlot = self.graphWidget.addPlot(
            title="Ball Position"
        )

        self.ballPlot.setLabel('left', 'Position (m)')
        self.ballPlot.setLabel('bottom', 'Time (s)')
        self.ballPlot.showGrid(x=True, y=True)
        self.graphWidget.nextRow()

        self.errorPlot = self.graphWidget.addPlot(
            title="Control Error"
        )

        self.errorPlot.setLabel('left', 'Error (m)')
        self.errorPlot.setLabel('bottom', 'Time (s)')
        self.errorPlot.showGrid(x=True, y=True)
        self.graphWidget.nextRow()

        self.servoPlot = self.graphWidget.addPlot(
            title="Servo Output"
        )

        self.servoPlot.setLabel('left', 'Angle (rad)')
        self.servoPlot.setLabel('bottom', 'Time (s)')
        self.servoPlot.showGrid(x=True, y=True)


        # Curves
        self.ballCurve = self.ballPlot.plot()

        self.errorCurve = self.errorPlot.plot()

        self.servoCurve = self.servoPlot.plot()
        # Graph Data
        self.timeData = []
        self.ballData = []
        self.errorData = []
        self.servoData = []

        self.time = 0
  

        # Right Panel
        self.rightPanel = QWidget()

        self.mainLayout.addWidget(self.leftPanel)
        self.mainLayout.addWidget(self.rightPanel)
        self.rightLayout = QVBoxLayout()
        from PyQt5.QtCore import Qt
        self.rightLayout.setAlignment(Qt.AlignTop)
        self.rightPanel.setLayout(self.rightLayout)
        self.statusLabel = QLabel("Simulation : Stopped")
        self.ballXLabel = QLabel("Ball X : 0.000 m")
        self.ballYLabel = QLabel("Ball Y : 0.000 m")

        self.errorXLabel = QLabel("Error X : 0.000 m")
        self.errorYLabel = QLabel("Error Y : 0.000 m")

        self.servoXLabel = QLabel("Servo X : 0.000 rad")
        self.servoYLabel = QLabel("Servo Y : 0.000 rad")

        self.timeLabel = QLabel("Time : 0.00 s")
        self.rightLayout.addWidget(self.statusLabel)
        self.rightLayout.addWidget(self.ballXLabel)
        self.rightLayout.addWidget(self.ballYLabel)

        self.rightLayout.addSpacing(15)

        self.rightLayout.addWidget(self.errorXLabel)
        self.rightLayout.addWidget(self.errorYLabel)

        self.rightLayout.addSpacing(15)

        self.rightLayout.addWidget(self.servoXLabel)
        self.rightLayout.addWidget(self.servoYLabel)

        self.rightLayout.addSpacing(15)

        self.rightLayout.addWidget(self.timeLabel)
        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 1)


        self.leftPanel.setStyleSheet("background-color: lightgray;")
        self.rightPanel.setStyleSheet("background-color: white;")



    def setGraphData(self, time, ball, error, servo):

        self.timeData.append(time)
        self.ballData.append(ball)
        self.errorData.append(error)
        self.servoData.append(servo)

        if len(self.timeData) > 500:
            self.timeData.pop(0)
            self.ballData.pop(0)
            self.errorData.pop(0)
            self.servoData.pop(0)

        self.ballCurve.setData(self.timeData, self.ballData)
        self.errorCurve.setData(self.timeData, self.errorData)
        self.servoCurve.setData(self.timeData, self.servoData)
    def updateStatus(self, time, ballX, ballY, errorX, errorY, servoX, servoY):
    
        self.statusLabel.setText("Simulation : Running")
    
        self.ballXLabel.setText(f"Ball X : {ballX:.3f} m")
        self.ballYLabel.setText(f"Ball Y : {ballY:.3f} m")
    
        self.errorXLabel.setText(f"Error X : {errorX:.3f} m")
        self.errorYLabel.setText(f"Error Y : {errorY:.3f} m")
    
        self.servoXLabel.setText(f"Servo X : {servoX:.3f} rad")
        self.servoYLabel.setText(f"Servo Y : {servoY:.3f} rad")
    
        self.timeLabel.setText(f"Time : {time:.2f} s")
if __name__ == "__main__":
    app = QApplication([])

    dashboard = Dashboard()
    dashboard.show()

    app.exec()
        