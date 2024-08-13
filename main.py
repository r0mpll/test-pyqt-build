import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.mainwindow import MainWindow

app = QApplication(sys.argv)

basedir = os.path.dirname(__file__)
window = MainWindow(basedir)
window.show()

# Start the event loop.
app.exec()