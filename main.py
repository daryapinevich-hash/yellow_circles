import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.setMinimumHeight(400)

    def add_circle(self):
        if self.width() > 100:
            x = random.randint(10, self.width() - 110)
            y = random.randint(10, self.height() - 110)
            diameter = random.randint(20, 100)
            color = QColor(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
            self.circles.append((x, y, diameter, color))
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, d, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, d, d)

    def resizeEvent(self, event):
        self.update()


class UI:
    def __init__(self):
        self.btn_add = QPushButton("Добавить случайный круг")
        self.canvas = Canvas()

    def setup_ui(self, parent):
        layout = QVBoxLayout()
        layout.addWidget(self.btn_add)
        layout.addWidget(self.canvas)
        parent.setLayout(layout)
        return self.btn_add, self.canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные цветные круги")
        self.setGeometry(100, 100, 800, 600)

        central = QWidget()
        self.setCentralWidget(central)

        self.ui = UI()
        btn, canvas = self.ui.setup_ui(central)
        btn.clicked.connect(canvas.add_circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
