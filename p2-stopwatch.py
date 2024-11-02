import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        # Set object names for button styles
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 25.5px;
                font-weight: bold;
                font-family: georgia;
            }
            QPushButton {
                font-size: 50px;
            }
            QLabel {
                font-size: 120px;
                background-color: #d64d0d;
                border-radius: 30px;
            }
            /* Start Button Hover Effect */
            QPushButton#start_button {
                background-color: lightgreen;  /* Default background color */
            }
            QPushButton#start_button:hover {
                background-color: green;       /* Hover background color */
            }
            
            QPushButton#stop_button {
                background-color: lightcoral;  /* Default background color */
            }
            QPushButton#stop_button:hover {
                background-color: red;         /* Hover background color */
            }
            /* Reset Button Hover Effect */
            QPushButton#reset_button {
                background-color: lightblue;   /* Default background color */
            }
            QPushButton#reset_button:hover {
                background-color: blue;        /* Hover background color */
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(11)
    
    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        millisec = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millisec:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
