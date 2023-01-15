from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from ..layouts.widget_slot import Ui_WidgetSlot


class WidgetSlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetSlot()
        self.ui.setupUi(self)
        self.ui.qlabel_frame.setScaledContents(True)
        self.show()
        self.hide()
        
    def setup(self, slot):
        self.ui.qline_plate_digit.setText(slot.lp_text)
        self.ui.qline_type_vehicle.setText(slot.type_vehicle)
        self.ui.qline_slot.setText(slot.id)
        cv2.imwrite("test.jpg", slot.image)
        if slot.image is not None:
            rgb_img = cv2.cvtColor(slot.image, cv2.COLOR_BGR2RGB)
        else:
            rgb_img = np.zeros((300, 300, 3), np.uint8)
        self.show_image(rgb_img)
        
    def show_image(self, rgb_img):
        # rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        rgb_img = cv2.resize(rgb_img, (300, 300))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height())
        self.ui.qlabel_frame.setPixmap(qt_img)
        