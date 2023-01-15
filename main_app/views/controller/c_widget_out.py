from PyQt5 import QtCore, QtGui, QtWidgets
from ..layouts.widget_out import Ui_WidgetOut


class WidgetOut(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetOut()
        self.ui.setupUi(self)
        
        