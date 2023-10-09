from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow  # Assuming "ui" contains your UI class
import main
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        main.TaskExecution()

starExe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)  # Fixed the connection

    def startTask(self):
        self.gui.gif1 = QMovie("LCPT.gif")
        self.gui.label_2.setMovie(self.gui.gif1)
        self.gui.gif1.start()

        starExe.start()

if __name__ == "__main__":
    GuiApp = QApplication(sys.argv)
    jarvis_gui = Gui_Start()
    jarvis_gui.show()
    sys.exit(GuiApp.exec_())
