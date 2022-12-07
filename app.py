from PySide2.QtWidgets import QApplication
from mainWindow import MainWindow
import sys

app = QApplication()
myWindow = MainWindow()
myWindow.show()

sys.exit(app.exec_())