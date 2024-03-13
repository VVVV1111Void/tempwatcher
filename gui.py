import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from collections import deque
import random
import numpy as np
from scipy.interpolate import make_interp_spline
from utils import *
colors = ['g', 'r', 'b', 'w']
class SlidingGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CPU Temperature Monitor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.graph_widget = pg.PlotWidget()
        self.layout.addWidget(self.graph_widget)

        self.data = [deque(maxlen=1000) for _ in range(4)]
        self.x_data = deque( maxlen=1000)

        self.curves = [self.graph_widget.plot(pen=colors[i]) for i in range(4)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(50)  # Update interval in milliseconds

    def update_data(self):
        self.data.append(80)
        new_data_points = get_temps()

        # Update x-axis data
        if not self.x_data:
            self.x_data.append(0)
        else:
            self.x_data.append(self.x_data[-1] + 1)

        # Update all plots
        for i, curve in enumerate(self.curves):
            self.data[i].append(new_data_points[i])
            curve.setData(list(self.x_data), list(self.data[i]))


def main():
    app = QApplication(sys.argv)
    window = SlidingGraphWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()