import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect

class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 600, 400)

        self.circles = []

        self.button = QPushButton("Нарисовать окружность", self)
        self.button.setGeometry(200, 330, 200, 40)
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 120)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 50)

        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, d, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QRect(x, y, d, d))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
