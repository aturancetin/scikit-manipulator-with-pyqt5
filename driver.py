
# @file: driver.py

# @author: Ali Turan Cetin

# @date: June 11, 2021

# @brief: Scikit Image Manipulator


from ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

os.environ['DISPLAY'] = ':0'


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])

MainWindow = mywindow()
MainWindow.show()


sys.exit(app.exec_())
