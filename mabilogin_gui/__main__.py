import sys
from PyQt5.QtWidgets import QApplication
from mabilogin_gui.mainwindow import MainWindow

def run():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
