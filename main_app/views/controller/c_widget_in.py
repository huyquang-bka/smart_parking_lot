from PyQt5 import QtCore, QtGui, QtWidgets
from ..layouts.widget_in import Ui_WidgetIn
from ..controller.c_widget_slot import WidgetSlot
from ...object.slot_object import SlotObject
from ...util.tools import detect
import cv2

class WidgetIn(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetIn()
        self.widget_slot = WidgetSlot()
        self.ui.setupUi(self)
        
        self.image = None
        
        self.grid_layout_cameras = QtWidgets.QGridLayout()
        self.grid_layout_cameras.setContentsMargins(0, 0, 0, 0)
        self.ui.qframe_map.setLayout(self.grid_layout_cameras)
        
        self.create_slots()
        
        self.connect_btn_signals()
        
    def connect_btn_signals(self):
        self.ui.btn_apply.clicked.connect(self.apply)
            
    def create_slots(self):
        self.slots = {}
        for i in range(5):
            for j in range(5):
                slot_text = i * 5 + j + 1
                slot = SlotObject(self.ui.qframe_map)
                slot.sig_clicked.connect(self.show_slot)
                slot.id = str(slot_text)
                slot.setText(str(slot.id))
                self.grid_layout_cameras.addWidget(slot, i, j)
                self.slots[str(slot_text)] = slot
    
    def apply(self):
        slot_text = self.ui.qline_slot.text()
        if not self.ui.qline_plate_digit.text() or not self.ui.qline_type_vehicle.text() or not self.ui.qline_slot.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Nhập đầy đủ thông tin")
            return
        try:
            slot_text = int(slot_text)
        except:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chọn chỗ đỗ")
            return
        if slot_text < 1 or slot_text > 25:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chọn chỗ đỗ từ 1 đến 25")
            return
        if self.slots[str(slot_text)].busy:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chỗ đỗ đã có xe")
            return
        slot_text = str(slot_text)
        for slot in self.slots.values():
            if slot.color == (255, 255, 0):
                slot.busy = False
                slot.color = (0, 255, 0)
                slot.apply()
        slot_id = self.ui.qline_slot.text()
        slot = self.slots[slot_id]
        slot.busy = True
        slot.color = (255, 0, 0)
        slot.lp_text = self.ui.qline_plate_digit.text()
        slot.type_vehicle = self.ui.qline_type_vehicle.text()
        slot.image = self.image
        slot.apply()
    
    def start(self, fn):
        self.image = cv2.imread(fn)
        self.ui.qline_plate_digit.setText("In progress...")
        self.ui.qline_type_vehicle.setText("In progress...")
        self.ui.qline_slot.setText("In progress...")
        cls, lp_text = detect(self.image)
        if cls in [2, 5, 7]:
            cls = "Ô tô"
        elif cls in [3]:
            cls = "Xe máy"
        self.ui.qline_plate_digit.setText(lp_text.upper())
        self.ui.qline_type_vehicle.setText(cls)
        for slot in self.slots.values():
            if not slot.busy:
                slot.color = (255, 255, 0)
                self.ui.qline_slot.setText(str(slot.id))
                slot.apply()
                break
    
    def paintEvent(self, event):
        if self.image is not None:
            rgb_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.show_image(rgb_img)
        # self.show_slots()
        self.update()

    def show_image(self, rgb_img):
        rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height())
        self.ui.qlabel_frame.setPixmap(qt_img)
        self.ui.qlabel_frame.setScaledContents(True)
        
    def show_slot(self, slot_id):
        slot = self.slots[slot_id]
        self.widget_slot.resize(500, 300)
        self.widget_slot.setup(slot)
        self.widget_slot.show()
        self.widget_slot.raise_()
        
                
                
    