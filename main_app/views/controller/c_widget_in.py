import os
from PyQt5 import QtCore, QtGui, QtWidgets
from ..layouts.widget_in import Ui_WidgetIn
from ..controller.c_widget_slot import WidgetSlot
from ...object.slot_object_2 import SlotObject
from ...util.tools import detect
import cv2
from gtts import gTTS
import playsound

class WidgetIn(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_image = []
        self.ui = Ui_WidgetIn()
        self.widget_slot = WidgetSlot()
        self.groupBox_dict = {}
        self.ui.setupUi(self)
        self.setup_ui()
        
        self.image = None
        
        # self.grid_layout_cameras = QtWidgets.QGridLayout()
        # self.grid_layout_cameras.setContentsMargins(0, 0, 0, 0)
        # self.ui.qframe_map.setLayout(self.grid_layout_cameras)
        
        self.create_slots()
        
        self.connect_btn_signals()
        
    def setup_ui(self):
        pass
    
    def connect_btn_signals(self):
        self.ui.btn_apply.clicked.connect(self.apply)
            
    def create_slots(self):
        self.slots = {}
        for i in range(7):
            slot_text = i + 1
            
            #a
            slot_a = SlotObject(self.ui.groupBox_A)
            slot_a.sig_clicked.connect(self.show_slot)
            slot_a.id = f"A{slot_text}"
            slot_a.setText(str(slot_a.id))
            self.ui.gridLayout_A.addWidget(slot_a, i, 0)
            self.slots[f"A{slot_text}"] = slot_a
            
            # b
            slot_b = SlotObject(self.ui.groupBox_B)
            slot_b.sig_clicked.connect(self.show_slot)
            slot_b.id = f"B{slot_text}"
            slot_b.setText(str(slot_b.id))
            self.ui.gridLayout_B.addWidget(slot_b, i, 0)
            self.slots[f"B{slot_text}"] = slot_b
            
            #c
            slot_c = SlotObject(self.ui.groupBox_C)
            slot_c.sig_clicked.connect(self.show_slot)
            slot_c.id = f"C{slot_text}"
            slot_c.setText(str(slot_c.id))
            self.ui.gridLayout_C.addWidget(slot_c, i, 0)
            self.slots[f"C{slot_text}"] = slot_c
            
            # #d
            slot_d = SlotObject(self.ui.groupBox_D)
            slot_d.sig_clicked.connect(self.show_slot)
            slot_d.id = f"D{slot_text}"
            slot_d.setText(str(slot_d.id))
            self.ui.gridLayout_D.addWidget(slot_d, i, 0)
            self.slots[f"D{slot_text}"] = slot_d

    
    def apply(self):
        slot_text = self.ui.qcomboBox_slot.currentText()
        if not self.ui.qline_plate_digit.text() or not self.ui.qline_type_vehicle.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Nhập đầy đủ thông tin")
            return
        if not slot_text in self.slots.keys():
            QtWidgets.QMessageBox.warning(self, "Warning", "Chọn chỗ đỗ phù hợp")
            return
        # if slot_text < 1 or slot_text > 25:
        #     QtWidgets.QMessageBox.warning(self, "Warning", "Chọn chỗ đỗ từ 1 đến 25")
        #     return
        if self.slots[str(slot_text)].busy:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chỗ đỗ đã có xe")
            return
        if self.ui.qline_type_vehicle.text().lower() == "Ô tô".lower() and ("C" in slot_text or "D" in slot_text):
            QtWidgets.QMessageBox.warning(self, "Warning", "Ô tô chỉ được đỗ ở A và B")
            return
        slot_text = str(slot_text)
        for slot in self.slots.values():
            if slot.color == (255, 255, 0):
                slot.busy = False
                slot.color = (0, 255, 0)
                slot.apply()
        slot_id = slot_text
        slot = self.slots[slot_id]
        slot.busy = True
        slot.color = (255, 0, 0)
        slot.lp_text = self.ui.qline_plate_digit.text()
        slot.type_vehicle = self.ui.qline_type_vehicle.text()
        slot.image = self.image
        slot.apply()
        tts = gTTS(text=f'Vị trí {slot_id}', lang='vi')
        tts.save("slot.mp3")
        playsound.playsound("slot.mp3")
        os.remove("slot.mp3")
        self.index += 1
        if self.index == len(self.list_image):
            QtWidgets.QMessageBox.warning(self, "Warning", "Đã hết ảnh!")
        self.start(self.list_image[self.index])

    def start_(self, fp):
        self.index = 0
        self.list_image = [os.path.join(fp, fn) for fn in os.listdir(fp) if (fn.endswith(".jpg") or fn.endswith(".jpg"))]
        if not self.list_image:
            QtWidgets.QMessageBox.warning(self, "Warning", "Thư mục không có ảnh phù hợp!")
        self.start(self.list_image[self.index])
    
    def start(self, fn):
        self.image = cv2.imread(fn)
        self.ui.qline_plate_digit.setText("In progress...")
        self.ui.qline_type_vehicle.setText("In progress...")
        # self.ui.qline_slot.setText("In progress...")
        cls, lp_text = detect(self.image)
        if cls in [2, 5, 7]:
            cls = "Ô tô"
        elif cls in [3]:
            cls = "Xe máy"
        self.ui.qline_plate_digit.setText(lp_text.upper())
        self.ui.qline_type_vehicle.setText(cls)
        #set list slot to combo box
        self.ui.qcomboBox_slot.clear()
        items = []
        for key in sorted(self.slots.keys()):
            slot = self.slots[key]
            if cls.lower() == "Ô tô".lower() and ("C" in key or "D" in key):
                continue
            if cls.lower() == "Xe máy".lower() and ("A" in key or "B" in key):
                continue
            if not slot.busy:
                items.append(str(slot.id))
        self.ui.qcomboBox_slot.addItems(items)
        for key in sorted(self.slots.keys()):
            slot = self.slots[key]
            if cls.lower() == "Ô tô".lower() and ("C" in key or "D" in key):
                continue
            if cls.lower() == "Xe máy".lower() and ("A" in key or "B" in key):
                continue
            if not slot.busy:
                slot.color = (255, 255, 0)
                self.ui.qcomboBox_slot.setCurrentText(str(slot.id))
                slot.apply()
                break
    
    def paintEvent(self, event):
        if self.image is not None:
            rgb_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.show_image(rgb_img)
        # self.show_slots()
        self.update()

    def show_image(self, rgb_img):
        # rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        rgb_img = cv2.resize(rgb_img, (1280, 720))
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
        
                
                
    
