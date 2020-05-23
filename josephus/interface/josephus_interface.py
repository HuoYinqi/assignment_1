# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '库\josephus\interface\josephus_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 110, 411, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_start = QtWidgets.QLabel(self.frame)
        self.label_start.setGeometry(QtCore.QRect(40, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setObjectName("label_start")
        self.label_step = QtWidgets.QLabel(self.frame)
        self.label_step.setGeometry(QtCore.QRect(40, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_step.setFont(font)
        self.label_step.setObjectName("label_step")
        self.line_edit_start = QtWidgets.QLineEdit(self.frame)
        self.line_edit_start.setGeometry(QtCore.QRect(130, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.line_edit_start.setFont(font)
        self.line_edit_start.setText("")
        self.line_edit_start.setObjectName("line_edit_start")
        self.line_edit_step = QtWidgets.QLineEdit(self.frame)
        self.line_edit_step.setGeometry(QtCore.QRect(130, 50, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.line_edit_step.setFont(font)
        self.line_edit_step.setText("")
        self.line_edit_step.setObjectName("line_edit_step")
        self.label_hint_start = QtWidgets.QLabel(self.frame)
        self.label_hint_start.setGeometry(QtCore.QRect(190, 10, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_hint_start.setFont(font)
        self.label_hint_start.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_hint_start.setText("")
        self.label_hint_start.setObjectName("label_hint_start")
        self.label_hint_step = QtWidgets.QLabel(self.frame)
        self.label_hint_step.setGeometry(QtCore.QRect(190, 50, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_hint_step.setFont(font)
        self.label_hint_step.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_hint_step.setText("")
        self.label_hint_step.setObjectName("label_hint_step")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(160, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 200, 301, 351))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_people = QtWidgets.QLabel(self.frame_2)
        self.label_people.setGeometry(QtCore.QRect(40, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_people.setFont(font)
        self.label_people.setObjectName("label_people")
        self.people_info = QtWidgets.QTextEdit(self.frame_2)
        self.people_info.setGeometry(QtCore.QRect(40, 50, 201, 271))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.people_info.setFont(font)
        self.people_info.setObjectName("people_info")
        self.button_file = QtWidgets.QToolButton(self.frame_2)
        self.button_file.setGeometry(QtCore.QRect(160, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_file.setFont(font)
        self.button_file.setObjectName("button_file")
        self.button_ok = QtWidgets.QToolButton(self.frame_2)
        self.button_ok.setGeometry(QtCore.QRect(160, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(300, 250, 401, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.button_run = QtWidgets.QToolButton(self.frame_3)
        self.button_run.setGeometry(QtCore.QRect(270, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_run.setFont(font)
        self.button_run.setObjectName("button_run")
        self.result = QtWidgets.QTextBrowser(self.frame_3)
        self.result.setGeometry(QtCore.QRect(0, 0, 261, 271))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.button_quit = QtWidgets.QToolButton(self.frame_3)
        self.button_quit.setGeometry(QtCore.QRect(270, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_quit.setFont(font)
        self.button_quit.setObjectName("button_quit")
        self.button_next = QtWidgets.QToolButton(self.frame_3)
        self.button_next.setGeometry(QtCore.QRect(270, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_next.setFont(font)
        self.button_next.setObjectName("button_next")
        self.button_clear = QtWidgets.QToolButton(self.frame_3)
        self.button_clear.setGeometry(QtCore.QRect(270, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.label_showresult = QtWidgets.QLabel(self.centralwidget)
        self.label_showresult.setGeometry(QtCore.QRect(390, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showresult.setFont(font)
        self.label_showresult.setObjectName("label_showresult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 23))
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
        self.label_start.setText(_translate("MainWindow", "START:"))
        self.label_step.setText(_translate("MainWindow", "STEP:"))
        self.label_title.setText(_translate("MainWindow", "Game of Josephus Ring"))
        self.label_people.setText(_translate("MainWindow", "PEOPLE"))
        self.people_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.button_file.setText(_translate("MainWindow", "from file"))
        self.button_ok.setText(_translate("MainWindow", "OK"))
        self.button_run.setText(_translate("MainWindow", "RUN ALL"))
        self.button_quit.setText(_translate("MainWindow", "Quit"))
        self.button_next.setText(_translate("MainWindow", "NEXT"))
        self.button_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label_showresult.setText(_translate("MainWindow", "show result"))
