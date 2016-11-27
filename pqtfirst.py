import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont

class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a button')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


        self.setGeometry(700, 300, 500, 200)
        self.setWindowTitle('Lilya\'s first widget')
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cl = myClass()
    sys.exit(app.exec_())

        
