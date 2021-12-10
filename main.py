import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class RandomCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.createCircleButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.createCircle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def createCircle(self, qp):
        size = random.randint(0, 200)
        x, y = random.randint(0, 400), random.randint(0, 400)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, size, size)


def main():
    app = QApplication(sys.argv)
    process = RandomCircles()
    process.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
