# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'konecta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 508)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 71))
        self.label.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.BTN_CrearRutaTrabajo = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_CrearRutaTrabajo.setGeometry(QtCore.QRect(120, 110, 181, 23))
        self.BTN_CrearRutaTrabajo.setStyleSheet("QPushButton {\n"
"   \n"
"    border: 1px solid rgb(0, 85, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(0, 85, 127);\n"
"   color: white;\n"
"    \n"
"}")
        self.BTN_CrearRutaTrabajo.setObjectName("BTN_CrearRutaTrabajo")
        self.BTN_ir_RutaDeTrabajo = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_ir_RutaDeTrabajo.setGeometry(QtCore.QRect(120, 140, 181, 23))
        self.BTN_ir_RutaDeTrabajo.setStyleSheet("QPushButton {\n"
"   \n"
"    border: 1px solid rgb(0, 85, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(0, 85, 127);\n"
"   color: white;\n"
"    \n"
"}")
        self.BTN_ir_RutaDeTrabajo.setObjectName("BTN_ir_RutaDeTrabajo")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 361, 101))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(0, 85, 127);\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 85, 127);\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 190, 361, 101))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(0, 85, 127);\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 85, 127);\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.BTN_Subir_Boletas_txt = QtWidgets.QPushButton(self.groupBox_2)
        self.BTN_Subir_Boletas_txt.setGeometry(QtCore.QRect(80, 30, 181, 23))
        self.BTN_Subir_Boletas_txt.setStyleSheet("QPushButton {\n"
"   \n"
"    border: 1px solid rgb(0, 85, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(0, 85, 127);\n"
"   color: white;\n"
"    \n"
"}")
        self.BTN_Subir_Boletas_txt.setObjectName("BTN_Subir_Boletas_txt")
        self.BTN_Convertir_boleta_pdf = QtWidgets.QPushButton(self.groupBox_2)
        self.BTN_Convertir_boleta_pdf.setGeometry(QtCore.QRect(80, 60, 181, 23))
        self.BTN_Convertir_boleta_pdf.setStyleSheet("QPushButton {\n"
"   \n"
"    border: 1px solid rgb(0, 85, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(0, 85, 127);\n"
"   color: white;\n"
"    \n"
"}")
        self.BTN_Convertir_boleta_pdf.setObjectName("BTN_Convertir_boleta_pdf")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 300, 361, 101))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(0, 85, 127);\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 85, 127);\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.BTN_Enviar_Correo = QtWidgets.QPushButton(self.groupBox_3)
        self.BTN_Enviar_Correo.setGeometry(QtCore.QRect(80, 30, 181, 23))
        self.BTN_Enviar_Correo.setStyleSheet("QPushButton {\n"
"   \n"
"    border: 1px solid rgb(0, 85, 127);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(0, 85, 127);\n"
"   color: white;\n"
"    \n"
"}")
        self.BTN_Enviar_Correo.setObjectName("BTN_Enviar_Correo")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 241, 31))
        self.label_3.setStyleSheet("\n"
"color: rgb(0, 0, 127);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 400, 331, 41))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 480, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.BTN_CrearRutaTrabajo.raise_()
        self.BTN_ir_RutaDeTrabajo.raise_()
        self.groupBox_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPA KONECTA"))
        self.label.setText(_translate("MainWindow", "CONSOLIDADO BOLETAS"))
        self.BTN_CrearRutaTrabajo.setText(_translate("MainWindow", "1. CREAR RUTA DE TRABAJO"))
        self.BTN_ir_RutaDeTrabajo.setText(_translate("MainWindow", "2. IR A LA RUTA DE CARPETAS"))
        self.groupBox.setTitle(_translate("MainWindow", "Ruta Y Carpetas:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Manejando Formatos:"))
        self.BTN_Subir_Boletas_txt.setText(_translate("MainWindow", "3. SUBIR BOLETAS (.txt)"))
        self.BTN_Convertir_boleta_pdf.setText(_translate("MainWindow", "4. CONVERTIR BOLETA A .PDF"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Enviar Correo:"))
        self.BTN_Enviar_Correo.setText(_translate("MainWindow", "5. EJECUTAR CORREO"))
        self.label_3.setText(_translate("MainWindow", "Previa Configuracion con su provedor de correo, se recomienda outlook."))
        self.label_2.setText(_translate("MainWindow", "Guia: Debemos Seguir en Orden de los Botones, para no caer en error de otra forma cada boton te dara la alerta que necesitas."))
        self.label_4.setText(_translate("MainWindow", "JONATHAN VERA SEGURA"))
