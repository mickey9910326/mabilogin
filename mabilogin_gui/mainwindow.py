from mabilogin_gui.ui.ui_mainwindow import Ui_MainWindow
from mabilogin_gui.custom_grips import CustomGrip

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5 import QtGui 
from PyQt5 import QtCore




GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)

        self.titleBarInit()

    def titleBarInit(self):
        self.maximized = False
        self.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        # self.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.closeAppBtn.clicked.connect(lambda: self.close())
        self.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.maximized:
                self.maximize_restore()
            # MOVE WINDOW
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.titleWidget.mouseMoveEvent = moveWindow
        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self, QtCore.Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, QtCore.Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, QtCore.Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, QtCore.Qt.BottomEdge, True)

    
    def maximize_restore(self):
        if self.maximized == False:
            self.maximized = True
            self.showMaximized()
            self.maximizeRestoreAppBtn.setToolTip("Restore")
        else:
            self.maximized = False
            self.showNormal()
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
    
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == QtCore.Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == QtCore.Qt.RightButton:
            print('Mouse click: RIGHT CLICK')