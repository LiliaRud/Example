from PyQt5.QtCore import *
from PyQt5.QtWidgets  import *
 
import sys
 
# этот класс позволяет легко использовать 
# главное меню и другие бонусы QMainWindow

class MyMainWindow(QMainWindow):
 
    def __init__(self, parent=None):
 
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget) 
        self.statusBar()
        #self.statusBar().showMessage(FormWidget.buttonClicked(self) + ' was pressed')

class FormWidget(QWidget):
 
    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
 
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

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

 
app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())
