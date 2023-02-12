from PyQt5 import QtCore, QtGui, QtWidgets
from ..layouts.main_window import Ui_MainWindow
from .c_widget_in import WidgetIn
from .c_widget_out import WidgetOut


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.combo_options.hide()
        
        self.widget_in = WidgetIn(self)
        self.widget_out = WidgetOut(self)
        
        #maximize window
        self.showMaximized()
        
        self.grid_layout_cameras = QtWidgets.QGridLayout()
        self.grid_layout_cameras.setContentsMargins(0, 0, 0, 0)
        self.ui.qframe_widget.setLayout(self.grid_layout_cameras)
        self.grid_layout_cameras.addWidget(self.widget_in, 0, 0)
        self.grid_layout_cameras.addWidget(self.widget_out, 0, 0)
        self.widget_out.hide()
        
        self.current_widget = self.widget_in
        
        self.connect_btn_signals()
        
        # self.connect_signals()
        
    def connect_btn_signals(self):
        self.ui.btn_choose_file.clicked.connect(self.choose_file)
        self.ui.btn_start.clicked.connect(self.start)
        
    def choose_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath(), "Image Files (*.png *.jpg *.jpeg)")
        if file_name:
            self.ui.qtext_file_path.setText(file_name)
            
    # def connect_signals(self):
    #     self.ui.combo_options.currentIndexChanged.connect(self.change_option)
        
    # def change_option(self):
    #     current_index = self.ui.combo_options.currentIndex()
    #     if current_index == 0:
    #         self.widget_in.show()
    #         self.widget_out.hide()
    #         self.current_widget = self.widget_in
    #     elif current_index == 1:
    #         self.widget_in.hide()
    #         self.widget_out.show()
    #         self.current_widget = self.widget_out
            
    def start(self):
        if not self.ui.qtext_file_path.toPlainText():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please choose a file")
            return
        self.current_widget.start(self.ui.qtext_file_path.toPlainText())
        
        