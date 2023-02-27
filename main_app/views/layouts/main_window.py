# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/layouts/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.qframe_widget = QtWidgets.QFrame(self.centralwidget)
        self.qframe_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qframe_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qframe_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qframe_widget.setObjectName("qframe_widget")
        self.gridLayout.addWidget(self.qframe_widget, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.groupBox.setStyleSheet("background-color: rgb(173, 221, 230);\n"
"border: 2px solid black;\n"
"border-radius: 6px;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_choose_folder = QtWidgets.QPushButton(self.groupBox)
        self.btn_choose_folder.setGeometry(QtCore.QRect(21, 40, 141, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choose_folder.sizePolicy().hasHeightForWidth())
        self.btn_choose_folder.setSizePolicy(sizePolicy)
        self.btn_choose_folder.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_choose_folder.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #fff;\n"
"                border-radius: 25px;\n"
"                border: 2px solid #2980b9;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                cursor: pointer;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #2980b9;\n"
"                padding-left: 15px;\n"
"                padding-top: 15px;\n"
"            }")
        self.btn_choose_folder.setObjectName("btn_choose_file")
        self.btn_start = QtWidgets.QPushButton(self.groupBox)
        self.btn_start.setGeometry(QtCore.QRect(22, 190, 141, 61))
        self.btn_start.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_start.setStyleSheet("QPushButton {\n"
"                background-color: #3498db;\n"
"                color: #fff;\n"
"                border-radius: 25px;\n"
"                border: 2px solid #2980b9;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2980b9;\n"
"                cursor: pointer;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #2980b9;\n"
"                padding-left: 15px;\n"
"                padding-top: 15px;\n"
"            }")
        self.btn_start.setObjectName("btn_start")
        self.qtext_file_path = QtWidgets.QTextEdit(self.groupBox)
        self.qtext_file_path.setGeometry(QtCore.QRect(21, 120, 141, 51))
        self.qtext_file_path.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qtext_file_path.setObjectName("qtext_file_path")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_choose_folder.setText(_translate("MainWindow", "Chọn thư mục"))
        self.btn_start.setText(_translate("MainWindow", "Chấp nhận"))
        self.qtext_file_path.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
