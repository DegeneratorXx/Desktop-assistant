from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import main
import sys

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        main.TaskExecution()
        # main.speak("Standby mode")
        # self.query = main.Takecommand()
        # if "wake up" in self.query:
        #     main.TaskExecution()


starExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):

        self.gui.gif1=QtGui.QMovie("C:\\Users\\narut\\Desktop\\Complete jarvis\\LCPT.gif")
        self.gui.label_2.setMovie(self.gui.gif1)
        self.gui.gif1.start()

        starExe.start()

GuiApp= QApplication(sys.argv)
jarvis_gui= Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())