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
        if self.width() > 100:  # Проверка размера
            x = random.randint(10, self.width() - 110)
            y = random.randint(10, self.height() - 110)
            diameter = random.randint(20, 100)
            self.circles.append((x, y, diameter))
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(255, 255, 0))  # Желтый
        painter.setPen(Qt.PenStyle.NoPen)
        for x, y, d in self.circles:
            painter.drawEllipse(x, y, d, d)

    def resizeEvent(self, event):
        self.update()  # Перерисовка при изменении размера


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yellow Circles")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central = QWidget()
        self.setCentralWidget(central)

        # Layout
        layout = QVBoxLayout()

        # Кнопка
        btn = QPushButton("Добавить круг")
        btn.clicked.connect(self.add_circle)

        # Canvas
        self.canvas = Canvas()

        layout.addWidget(btn)
        layout.addWidget(self.canvas)
        central.setLayout(layout)

    def add_circle(self):
        self.canvas.add_circle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
