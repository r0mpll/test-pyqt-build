import os

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from views.dialog import Dialog
from PyQt5.QtWidgets import QWidget, QCheckBox, QPushButton, QLineEdit, QMainWindow
class MainWindow(QMainWindow):
    basedir = ""
    def __init__(self, basedir):
        super(MainWindow, self).__init__()
        self.basedir = basedir
        uic.loadUi(os.path.join(basedir, "resources", "ui", "mainwindow.ui"), self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.pushButtonClickedSlot)
    def pushButtonClickedSlot(self, slot):
        self.dialog = Dialog(self.basedir)
        self.dialog.show()
    