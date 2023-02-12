from PyQt5 import QtCore, QtGui, QtWidgets


class SlotObject(QtWidgets.QLabel):
    sig_clicked = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumHeight(80)
        self.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                            "border: 2px solid black;\n"
                            "border-radius: 6px;")
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.id = "0"
        self.lp_text = ""
        self.type_vehicle = ""
        self.image = None
        self.busy = False
        self.color = (0, 255, 0)
        self.setStyleSheet("background-color: rgb({}, {}, {});".format(self.color[0], self.color[1], self.color[2]))
        
    def apply(self):
        self.setStyleSheet("background-color: rgb({}, {}, {});".format(self.color[0], self.color[1], self.color[2]))
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.sig_clicked.emit(self.id)
