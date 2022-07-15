# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(332, 432)
        MainWindow.setMinimumSize(QSize(332, 432))
        MainWindow.setMaximumSize(QSize(332, 432))
        icon = QIcon()
        icon.addFile(u"../compilador_python_pyinstaller_pyside/Calculator-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bapagar = QPushButton(self.centralwidget)
        self.bapagar.setObjectName(u"bapagar")
        self.bapagar.setGeometry(QRect(10, 110, 71, 31))
        font = QFont()
        font.setPointSize(16)
        self.bapagar.setFont(font)
        self.bapagar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(156, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.braiz = QPushButton(self.centralwidget)
        self.braiz.setObjectName(u"braiz")
        self.braiz.setGeometry(QRect(90, 80, 71, 61))
        font1 = QFont()
        font1.setPointSize(26)
        self.braiz.setFont(font1)
        self.braiz.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bdiv = QPushButton(self.centralwidget)
        self.bdiv.setObjectName(u"bdiv")
        self.bdiv.setGeometry(QRect(170, 80, 71, 61))
        font2 = QFont()
        font2.setPointSize(24)
        self.bdiv.setFont(font2)
        self.bdiv.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bmult = QPushButton(self.centralwidget)
        self.bmult.setObjectName(u"bmult")
        self.bmult.setGeometry(QRect(250, 80, 71, 61))
        self.bmult.setFont(font1)
        self.bmult.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b7 = QPushButton(self.centralwidget)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(10, 150, 71, 61))
        font3 = QFont()
        font3.setFamily(u"Segoe Script")
        font3.setPointSize(24)
        self.b7.setFont(font3)
        self.b7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b8 = QPushButton(self.centralwidget)
        self.b8.setObjectName(u"b8")
        self.b8.setGeometry(QRect(90, 150, 71, 61))
        self.b8.setFont(font3)
        self.b8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b9 = QPushButton(self.centralwidget)
        self.b9.setObjectName(u"b9")
        self.b9.setGeometry(QRect(170, 150, 71, 61))
        self.b9.setFont(font3)
        self.b9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bmenos = QPushButton(self.centralwidget)
        self.bmenos.setObjectName(u"bmenos")
        self.bmenos.setGeometry(QRect(250, 150, 71, 61))
        self.bmenos.setFont(font3)
        self.bmenos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bponto = QPushButton(self.centralwidget)
        self.bponto.setObjectName(u"bponto")
        self.bponto.setGeometry(QRect(170, 360, 71, 61))
        self.bponto.setFont(font3)
        self.bponto.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b4 = QPushButton(self.centralwidget)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(10, 220, 71, 61))
        self.b4.setFont(font3)
        self.b4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b5 = QPushButton(self.centralwidget)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(90, 220, 71, 61))
        self.b5.setFont(font3)
        self.b5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b6 = QPushButton(self.centralwidget)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(170, 220, 71, 61))
        self.b6.setFont(font3)
        self.b6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bmais = QPushButton(self.centralwidget)
        self.bmais.setObjectName(u"bmais")
        self.bmais.setGeometry(QRect(250, 220, 71, 61))
        self.bmais.setFont(font3)
        self.bmais.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bzero = QPushButton(self.centralwidget)
        self.bzero.setObjectName(u"bzero")
        self.bzero.setGeometry(QRect(90, 360, 71, 61))
        self.bzero.setFont(font3)
        self.bzero.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b1 = QPushButton(self.centralwidget)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(10, 290, 71, 61))
        self.b1.setFont(font3)
        self.b1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b2 = QPushButton(self.centralwidget)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(90, 290, 71, 61))
        self.b2.setFont(font3)
        self.b2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.b3 = QPushButton(self.centralwidget)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(170, 290, 71, 61))
        self.b3.setFont(font3)
        self.b3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 94);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bigual = QPushButton(self.centralwidget)
        self.bigual.setObjectName(u"bigual")
        self.bigual.setGeometry(QRect(250, 290, 71, 131))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(28)
        self.bigual.setFont(font4)
        self.bigual.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bporcent = QPushButton(self.centralwidget)
        self.bporcent.setObjectName(u"bporcent")
        self.bporcent.setGeometry(QRect(10, 360, 71, 61))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(26)
        self.bporcent.setFont(font5)
        self.bporcent.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 143, 14);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.bclear = QPushButton(self.centralwidget)
        self.bclear.setObjectName(u"bclear")
        self.bclear.setGeometry(QRect(10, 72, 71, 31))
        self.bclear.setFont(font)
        self.bclear.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"  \n"
"\n"
"	\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(156, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 331, 61))
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(26)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setMargin(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bclear.clicked.connect(self.label.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MPCalc", None))
        self.bapagar.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.braiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.bdiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.bmult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bmenos.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.bponto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.bmais.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bzero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.bigual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.bporcent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.bclear.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.label.setText("")
    # retranslateUi

