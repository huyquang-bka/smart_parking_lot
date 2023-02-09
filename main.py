import os
from PyQt5.QtWidgets import QApplication
import sys
import signal
from main_app.views.controller.c_main_window import MainWindow


if __name__ == "__main__":
    print("Current Directory: ", os.getcwd())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
