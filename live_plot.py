import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
import sys
import random

app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsLayoutWidget(title="Ball Position")
win.resize(900,500)
win.show()

plot = win.addPlot(title="Live Ball Position")

curveX = plot.plot(pen='r', name="X")
curveY = plot.plot(pen='b', name="Y")

xData=[]
yData=[]
timeData=[]

t=0

def update():

    global t

    timeData.append(t)

    xData.append(random.random())
    yData.append(random.random())

    curveX.setData(timeData,xData)
    curveY.setData(timeData,yData)

    t+=1

timer=QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

sys.exit(app.exec())