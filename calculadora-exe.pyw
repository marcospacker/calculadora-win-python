# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
       


# Definindo conexão entre os botoes e as funcoes
        
        self.setupUi(self)
        self.b1.clicked.connect(self.fun_1)
        self.b2.clicked.connect(self.fun_2)
        self.b3.clicked.connect(self.fun_3)
        self.b4.clicked.connect(self.fun_4)
        self.b5.clicked.connect(self.fun_5)
        self.b6.clicked.connect(self.fun_6)
        self.b7.clicked.connect(self.fun_7)
        self.b8.clicked.connect(self.fun_8)
        self.b9.clicked.connect(self.fun_9)
        self.bzero.clicked.connect(self.fun_zero)
        self.bmais.clicked.connect(self.fun_mais)
        self.bigual.clicked.connect(self.fun_igual)
        self.bponto.clicked.connect(self.fun_ponto)
        self.bmenos.clicked.connect(self.fun_menos)
        self.bmult.clicked.connect(self.fun_mult)
        self.bdiv.clicked.connect(self.fun_div)
        self.bapagar.clicked.connect(self.fun_apagar)
        self.bporcent.clicked.connect(self.fun_porcent)
        self.braiz.clicked.connect(self.fun_raiz)
        


        
 # Definindo as funçoes        

    
    def fun_1(self):
        entrada = self.label.text()
        entrada += "1"
        self.label.setText(entrada)

    def fun_2(self):
        entrada = self.label.text()
        entrada += "2"
        self.label.setText(entrada)

    def fun_3(self):
        entrada = self.label.text()
        entrada += "3"
        self.label.setText(entrada)

    def fun_4(self):
        entrada = self.label.text()
        entrada += "4"
        self.label.setText(entrada)

    def fun_5(self):
        entrada = self.label.text()
        entrada += "5"
        self.label.setText(entrada)

    def fun_6(self):
        entrada = self.label.text()
        entrada += "6"
        self.label.setText(entrada)

    def fun_7(self):
        entrada = self.label.text()
        entrada += "7"
        self.label.setText(entrada)

    def fun_8(self):
        entrada = self.label.text()
        entrada += "8"
        self.label.setText(entrada)

    def fun_9(self):
        entrada = self.label.text()
        entrada += "9"
        self.label.setText(entrada)

    def fun_zero(self):
        entrada = self.label.text()
        entrada += "0"
        self.label.setText(entrada)
    
    def fun_mais(self):
        entrada = self.label.text()
        entrada += "+"
        self.label.setText(entrada)

    def fun_igual(self):
        entrada = self.label.text()
        try:
                num1 = eval(entrada)
                self.label.setText(str(num1))
        except:
                self.label.setText("ERROR")

    def fun_ponto(self):
        entrada = self.label.text()
        entrada += "."
        self.label.setText(entrada)

    def fun_div(self):
        entrada = self.label.text()
        entrada += "/"
        self.label.setText(entrada)

    def fun_mult(self):
        entrada = self.label.text()
        entrada += "*"
        self.label.setText(entrada) 

    def fun_menos(self):
        entrada = self.label.text()
        entrada += "-"
        self.label.setText(entrada) 

    def fun_apagar(self):
        entrada = self.label.text()
        self.label.setText(entrada[:len(entrada)-1])

    def fun_porcent(self):
        entrada = self.label.text()
        try:
            self.num1 = (entrada+"/100")
            self.label.setText(self.num1)
        except:
            self.label.setText("")

    def fun_raiz(self):
        entrada = self.label.text()
        try:
            self.num2 = (entrada+"** 0.5")
            self.label.setText(self.num2)
        except:
            self.label.setText("")
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())