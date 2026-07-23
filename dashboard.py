from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QDoubleSpinBox,
    QPushButton,
    QComboBox

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
        self.ballCurveX = self.ballPlot.plot(pen='b', name="X")
        self.ballCurveY = self.ballPlot.plot(pen='r', name="Y")

        self.errorCurveX = self.errorPlot.plot(pen='g', name="X")
        self.errorCurveY = self.errorPlot.plot(pen='m', name="Y")

        self.servoCurveX = self.servoPlot.plot(pen='c', name="X")
        self.servoCurveY = self.servoPlot.plot(pen='y', name="Y")
        # Graph Data
        self.timeData = []
        self.ballDataX = []
        self.ballDataY = []

        self.errorDataX = []
        self.errorDataY = []

        self.servoDataX = []
        self.servoDataY = []

        self.time = 0
  

        # ===========================
        # Right Panel
        # ===========================
        
        self.rightPanel = QWidget()
        self.rightLayout = QVBoxLayout()
        
        from PyQt5.QtCore import Qt
        self.rightLayout.setAlignment(Qt.AlignTop)
        
        self.rightPanel.setLayout(self.rightLayout)
        
        self.mainLayout.addWidget(self.leftPanel)
        self.mainLayout.addWidget(self.rightPanel)
        self.resetButton = QPushButton("Reset Ball")
        self.pauseButton = QPushButton("Pause")
        self.resumeButton = QPushButton("Resume")
        # =====================================
        # Styles
        # =====================================
        
        titleStyle = """
        font-size:18px;
        font-weight:bold;
        """
        
        labelStyle = """
        font-size:14px;
        padding:2px;
        """
        
        statusStyle = """
        font-size:15px;
        font-weight:bold;
        """
        
        # =====================================
        # Live Status
        # =====================================
        
        self.statusTitle = QLabel("Live Status")
        self.statusTitle.setStyleSheet(titleStyle)
        
        self.statusLabel = QLabel("🔴 Simulation : Stopped")
        self.statusLabel.setStyleSheet(statusStyle)
        
        self.ballXLabel = QLabel("Ball X : 0.000 m")
        self.ballYLabel = QLabel("Ball Y : 0.000 m")
        
        self.errorXLabel = QLabel("Error X : 0.000 m")
        self.errorYLabel = QLabel("Error Y : 0.000 m")
        
        self.servoXLabel = QLabel("Servo X : 0.000 rad")
        self.servoYLabel = QLabel("Servo Y : 0.000 rad")
        
        self.timeLabel = QLabel("Time : 0.00 s")
        
        # Apply Style
        
        for label in [
            self.ballXLabel,
            self.ballYLabel,
            self.errorXLabel,
            self.errorYLabel,
            self.servoXLabel,
            self.servoYLabel,
            self.timeLabel
        ]:
            label.setStyleSheet(labelStyle)
        
        # =====================================
        # Controller
        # =====================================
        
        self.controllerTitle = QLabel("Controller")
        self.controllerTitle.setStyleSheet(titleStyle)
        
        # Target Spin Boxes
        
        self.targetXSpin = QDoubleSpinBox()
        self.targetYSpin = QDoubleSpinBox()
        self.trajectoryCombo = QComboBox()

        self.trajectoryCombo.addItems([
            "Manual",
            "Point",
            "Line",
            "Circle",
            "Figure-8"
        ])
        for spin in [self.targetXSpin, self.targetYSpin]:
        
            spin.setRange(-0.2, 0.2)
            spin.setDecimals(3)
            spin.setSingleStep(0.01)
            spin.setValue(0)
        
        # KP KD Labels
        
        self.kpSpin = QDoubleSpinBox()
        self.kdSpin = QDoubleSpinBox()
        self.kpSpin.setRange(0, 500)
        self.kdSpin.setRange(0, 100)

        self.kpSpin.setDecimals(2)
        self.kdSpin.setDecimals(2)

        self.kpSpin.setSingleStep(1)
        self.kdSpin.setSingleStep(0.1)

        self.kpSpin.setValue(60)
        self.kdSpin.setValue(3)

        self.actionTitle = QLabel("Actions")
        self.actionTitle.setStyleSheet(titleStyle)
        # =====================================
        # Add Widgets
        # =====================================
        
        # -------- Live Status --------
        
        self.rightLayout.addWidget(self.statusTitle)
        self.rightLayout.addWidget(self.statusLabel)
        
        self.rightLayout.addSpacing(10)
        
        self.rightLayout.addWidget(self.ballXLabel)
        self.rightLayout.addWidget(self.ballYLabel)
        
        self.rightLayout.addSpacing(10)
        
        self.rightLayout.addWidget(self.errorXLabel)
        self.rightLayout.addWidget(self.errorYLabel)
        
        self.rightLayout.addSpacing(10)
        
        self.rightLayout.addWidget(self.servoXLabel)
        self.rightLayout.addWidget(self.servoYLabel)
        
        self.rightLayout.addSpacing(10)
        
        self.rightLayout.addWidget(self.timeLabel)
        
        # -------- Controller --------
        
        self.rightLayout.addSpacing(25)
        
        self.rightLayout.addWidget(self.controllerTitle)
        
        self.rightLayout.addSpacing(10)
        
        self.rightLayout.addWidget(QLabel("Target X"))
        self.rightLayout.addWidget(self.targetXSpin)
        
        self.rightLayout.addSpacing(5)
        
        self.rightLayout.addWidget(QLabel("Target Y"))
        self.rightLayout.addWidget(self.targetYSpin)
        self.rightLayout.addWidget(QLabel("Trajectory"))
        self.rightLayout.addWidget(self.trajectoryCombo)
        self.rightLayout.addSpacing(15)
        
        
        self.rightLayout.addWidget(QLabel("KP"))
        self.rightLayout.addWidget(self.kpSpin)
        
        self.rightLayout.addSpacing(5)
        
        self.rightLayout.addWidget(QLabel("KD"))
        self.rightLayout.addWidget(self.kdSpin)
        self.rightLayout.addSpacing(20)
        self.rightLayout.addWidget(self.actionTitle)
        self.rightLayout.addSpacing(10)
        self.rightLayout.addWidget(self.resetButton)
        self.rightLayout.addWidget(self.pauseButton)
        self.rightLayout.addWidget(self.resumeButton)
        # Stretch
        
        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 1)
        
        self.leftPanel.setStyleSheet("background-color: lightgray;")
        self.rightPanel.setStyleSheet("background-color: white;")
      


    def setGraphData(
    
        self,

        time,

        ballX,
        ballY,

        errorX,
        errorY,

        servoX,
        servoY

    ):
        self.timeData.append(time)
        self.ballDataX.append(ballX)
        self.ballDataY.append(ballY)

        self.errorDataX.append(errorX)
        self.errorDataY.append(errorY)

        self.servoDataX.append(servoX)
        self.servoDataY.append(servoY)

        if len(self.timeData) > 500:
            self.timeData.pop(0)
            self.ballDataX.pop(0)
            self.ballDataY.pop(0)
            self.errorDataX.pop(0)
            self.errorDataY.pop(0)
            self.servoDataX.pop(0)
            self.servoDataY.pop(0)

        self.ballCurveX.setData(self.timeData, self.ballDataX)
        self.ballCurveY.setData(self.timeData, self.ballDataY)
        
        self.errorCurveX.setData(self.timeData, self.errorDataX)
        self.errorCurveY.setData(self.timeData, self.errorDataY)
        
        self.servoCurveX.setData(self.timeData, self.servoDataX)
        self.servoCurveY.setData(self.timeData, self.servoDataY)
    def updateStatus(
        self,
        time,
        ballX,
        ballY,
        errorX,
        errorY,
        servoX,
        servoY,
        targetX,
        targetY,
        kp,
        kd
    ):
        self.statusLabel.setText("🟢 Simulation : Running")
        self.ballXLabel.setText(f"Ball X : {ballX:.3f} m")
        self.ballYLabel.setText(f"Ball Y : {ballY:.3f} m")

        self.errorXLabel.setText(f"Error X : {errorX:.3f} m")
        self.errorYLabel.setText(f"Error Y : {errorY:.3f} m")

        self.servoXLabel.setText(f"Servo X : {servoX:.3f} rad")
        self.servoYLabel.setText(f"Servo Y : {servoY:.3f} rad")

        self.timeLabel.setText(f"Time : {time:.2f} s")
    def getTrajectory(self):
        return self.trajectoryCombo.currentText()
        
    
if __name__ == "__main__":
    app = QApplication([])

    dashboard = Dashboard()
    dashboard.show()

    app.exec()
        