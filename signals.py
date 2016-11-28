import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLCDNumber, QSlider, QMessageBox,  QMainWindow,
                             QWidget, QPushButton, QVBoxLayout, QApplication)

class MyMainWindow(QMainWindow):
 
    def __init__(self, parent):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = MyClass() 
        self.setCentralWidget(self.form_widget)
        self.statusBar()
        
class MyClass(QWidget):
    def __init__(self, parent):
        super(MyClass, self).__init__(parent)
        self.initUI()

    def initUI(self, parent):

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        sld.valueChanged.connect(lcd.display)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        
        self.resize(500, 300)
        self.setWindowTitle('Signal & slot')

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

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
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
