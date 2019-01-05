from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyModbusTCP.client import ModbusClient
import time
import os
import sys
from PyQt5.QtWidgets import *
from converter import Ui_converter


class main(QWidget, Ui_converter):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


app = QApplication(sys.argv)
window = main()
window.show()
sys.exit(app.exec_())
