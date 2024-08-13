from PyQt5 import uic
from PyQt5 import QtCore
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QCheckBox, QPushButton, QLineEdit, QDialog
class Dialog(QDialog):
    def __init__(self, basedir):
        super(Dialog, self).__init__()
        uic.loadUi(os.path.join(basedir, "resources", "ui" ,"dialog.ui"), self)

