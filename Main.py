from konecta import *
import sys,time,datetime,glob
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import os, glob, datetime
import shutil,subprocess,configparser
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtWidgets, QtGui
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ## ACCION BOTONES
        self.ui.BTN_CrearRutaTrabajo.clicked.connect(lambda: self.CREAR_RUTA_DE_TRABAJO())
        self.ui.BTN_ir_RutaDeTrabajo.clicked.connect(lambda: self.IR_RUTA_DE_TRABAJO())
        self.ui.BTN_Subir_Boletas_txt.clicked.connect(lambda: self.SUBIR_BOLETAS_TXT())
        self.ui.BTN_Convertir_boleta_pdf.clicked.connect(lambda: self.CONVERTIR_BOLETA_A_PDF())
        self.ui.BTN_Enviar_Correo.clicked.connect(lambda: self.ENVIAR_BOLETAS_CORREO())

        # self.ruta_boletas_pdf = ''  # Variable global para almacenar la ruta de Boletas_PDF
        # self.ruta_boletas_txt = ''  # Variable global para almacenar la ruta de Boletas_TXT

        # Cargar las rutas de trabajo almacenadas en el archivo de configuración
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.ruta_boletas_pdf = self.config.get('Rutas', 'Boletas_PDF', fallback='')
        self.ruta_boletas_txt = self.config.get('Rutas', 'Boletas_TXT', fallback='')

    def GUARDAR_RUTAS(self):
        # Verificar si la sección 'Rutas' existe en el archivo de configuración
        if not self.config.has_section('Rutas'):
            self.config.add_section('Rutas')

        # Guardar las rutas de trabajo en el archivo de configuración
        self.config.set('Rutas', 'Boletas_PDF', self.ruta_boletas_pdf)
        self.config.set('Rutas', 'Boletas_TXT', self.ruta_boletas_txt)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def CREAR_RUTA_DE_TRABAJO(self):
        #global ruta_boletas_pdf, ruta_boletas_txt
        max_espacio_libre = 0
        unidad_optima = ''

        # Buscar la unidad con más espacio libre
        for unidad in range(ord('A'), ord('Z')+1):
            unidad = chr(unidad) + ':\\'
            if os.path.exists(unidad):
                espacio_libre = shutil.disk_usage(unidad).free
                if espacio_libre > max_espacio_libre:
                    max_espacio_libre = espacio_libre
                    unidad_optima = unidad

        if unidad_optima == '':
            # No se encontró ninguna unidad disponible
            QMessageBox.critical(None, 'Error', 'No se encontró ninguna unidad DISCO disponible, para la creacion.')
            return

        # Crear la ruta /Consolidado_Boletas
        ruta_consolidado = os.path.join(unidad_optima, 'Consolidado_Boletas')
        if os.path.exists(ruta_consolidado):
            # La carpeta ya existe, preguntar si se desea eliminar
            confirmacion = QMessageBox.question(None, 'Confirmación',
                                                'La carpeta "Consolidado_Boletas" ya existe. ¿Desea eliminarla y su contenido?',
                                                QMessageBox.Yes | QMessageBox.No)
            if confirmacion == QMessageBox.No:
                return
            else:
                try:
                    shutil.rmtree(ruta_consolidado)  # Eliminar carpeta y su contenido
                except OSError:
                    QMessageBox.critical(None, 'Error', 'No se pudo eliminar la carpeta "Consolidado_Boletas".')
                    return

        try:
            os.mkdir(ruta_consolidado)
        except OSError:
            QMessageBox.critical(None, 'Error', 'No se pudo crear la carpeta "Consolidado_Boletas".')
            return

        # Crear las carpetas Boletas_TXT y Boletas_PDF dentro de Consolidado_Boletas
        ruta_boletas_txt = os.path.join(ruta_consolidado, 'Boletas_TXT')
        ruta_boletas_pdf = os.path.join(ruta_consolidado, 'Boletas_PDF')
        try:
            os.mkdir(ruta_boletas_txt)
            os.mkdir(ruta_boletas_pdf)
        except OSError:
            QMessageBox.critical(None, 'Error', 'No se pudieron crear las carpetas "Boletas_TXT" y "Boletas_PDF".')
            return

        # Almacenar las rutas de trabajo
        self.ruta_boletas_pdf = ruta_boletas_pdf
        self.ruta_boletas_txt = ruta_boletas_txt
        self.GUARDAR_RUTAS()

        QMessageBox.information(None, 'Éxito', 'La ruta de trabajo, creado correctamente en la unidad {}'.format(unidad_optima) + 'Con mas Espacio en el OS.')


    def IR_RUTA_DE_TRABAJO(self):
        # Verificar si la ruta de trabajo se ha creado
        if self.ruta_boletas_pdf == '' or self.ruta_boletas_txt == '':
            QMessageBox.warning(None, 'Advertencia', 'No se ha creado la ruta de CARPETAS de TRABAJO..!')
            return

        # Mostrar un cuadro de diálogo para seleccionar la carpeta
        opciones = ['Boletas_PDF', 'Boletas_TXT']
        seleccion, ok = QtWidgets.QInputDialog.getItem(self, 'Ir a la carpeta.', 'Selecciona una carpeta:', opciones, editable=False)

        if ok and seleccion:  # Si se presionó Aceptar y se seleccionó una opción
            if seleccion == 'Boletas_PDF':
                QMessageBox.information(None, 'Éxito', 'Has seleccionado la carpeta Boletas_PDF.\nRuta: {}'.format(self.ruta_boletas_pdf))
                subprocess.Popen(r'explorer /root,"{}"'.format(self.ruta_boletas_pdf))
            elif seleccion == 'Boletas_TXT':
                QMessageBox.information(None, 'Éxito', 'Has seleccionado la carpeta Boletas_TXT.\nRuta: {}'.format(self.ruta_boletas_txt))
                subprocess.Popen(r'explorer /root,"{}"'.format(self.ruta_boletas_txt))
        else:
            QMessageBox.information(None, 'Cancelado', 'Has cancelado la selección de carpeta.')



    def SUBIR_BOLETAS_TXT(self):
        # Obtener la ruta de destino del archivo desde el archivo de configuración
        config = configparser.ConfigParser()
        config.read('config.ini')
        ruta_destino = config.get('Rutas', 'boletas_txt', fallback='')

        if not ruta_destino:
            QMessageBox.warning(None, 'Advertencia', 'No se ha especificado la ruta de destino en el archivo de configuración.')
            return

        # Abrir el cuadro de diálogo para seleccionar los archivos
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setWindowTitle('Seleccionar archivos de Boletas_TXT')
        dialog.setLabelText(QtWidgets.QFileDialog.Accept, 'Guardar')
        dialog.setLabelText(QtWidgets.QFileDialog.Reject, 'Cancelar')
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            archivos_seleccionados = dialog.selectedFiles()
            
            # Mover los archivos seleccionados a la ruta de destino
            try:
                for archivo in archivos_seleccionados:
                    #shutil.move(archivo, ruta_destino) #MOVER DE DOCUMENTOS
                    shutil.copy(archivo, ruta_destino)  #COPIAR DOCUMENTOS
            except Exception as e:
                QMessageBox.critical(None, 'Error', 'Ocurrió un error al mover los archivos, Verifica ruta: {}'.format(str(e)))
                return
            
            QMessageBox.information(None, 'Éxito', 'Los archivos se han guardado en la ubicación especificada.')
        else:
            QMessageBox.information(None, 'Cancelado', 'Has cancelado la operación.')


    def CONVERTIR_BOLETA_A_PDF(self):
        # Obtener la ruta de boletas_txt del archivo de configuración
        config = configparser.ConfigParser()
        config.read('config.ini')
        ruta_boletas_txt = config.get('Rutas', 'boletas_txt', fallback='')

        if not ruta_boletas_txt:
            QtWidgets.QMessageBox.warning(None, 'Advertencia', 'La ruta de boletas_txt no está configurada.')
            return

        # Obtener la ruta de boletas_pdf del archivo de configuración
        ruta_boletas_pdf = config.get('Rutas', 'boletas_pdf', fallback='')

        if not ruta_boletas_pdf:
            QtWidgets.QMessageBox.warning(None, 'Advertencia', 'La ruta de boletas_pdf no está configurada.')
            return

        # Obtener la lista de archivos .txt en la carpeta boletas_txt
        archivos_txt = glob.glob(os.path.join(ruta_boletas_txt, '*.txt'))

        if not archivos_txt:
            QtWidgets.QMessageBox.warning(None, 'Advertencia', 'No se encontraron archivos .txt en la carpeta boletas_txt.')
            return

        try:
            # Crear la carpeta boletas_pdf si no existe
            if not os.path.exists(ruta_boletas_pdf):
                os.makedirs(ruta_boletas_pdf)

            for archivo_txt in archivos_txt:
                nombre_archivo = os.path.basename(archivo_txt)
                nombre_archivo_pdf = os.path.splitext(nombre_archivo)[0] + '.pdf'
                ruta_archivo_pdf = os.path.join(ruta_boletas_pdf, nombre_archivo_pdf)

                # Leer el contenido del archivo de texto
                with open(archivo_txt, 'r') as file:
                    contenido_txt = file.read()

                # Crear el PDF
                c = canvas.Canvas(ruta_archivo_pdf, pagesize=letter)
                c.setFillColor(colors.black)
                c.setFont("Helvetica", 16)
                c.drawString(50, 750, "BOLETA KONECTA")
                c.setFont("Helvetica", 12)
                c.drawString(50, 700, "Fecha de creación: {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                c.setFont("Helvetica", 10)
                c.drawString(50, 650, "Contenido del archivo:")

                # Escribir el contenido del archivo en el PDF con saltos de línea
                lines = contenido_txt.splitlines()
                y = 630
                for line in lines:
                    c.drawString(50, y, line)
                    y -= 15

                c.showPage()
                c.save()

                QtWidgets.QMessageBox.information(None, 'Éxito', 'El archivo {} se ha convertido y guardado como {}'.format(nombre_archivo, nombre_archivo_pdf))

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Ha ocurrido un error al convertir los archivos a PDF:\n{}'.format(str(e)))





    def ENVIAR_BOLETAS_CORREO(self):
        # Obtener la ruta de boletas_pdf del archivo de configuración
        config = configparser.ConfigParser()
        config.read('config.ini')
        ruta_boletas_pdf = config.get('Rutas', 'boletas_pdf', fallback='')

        if not ruta_boletas_pdf:
            QtWidgets.QMessageBox.warning(None, 'Advertencia', 'La ruta de boletas_pdf no está configurada.')
            return

        # Crear el cuadro de diálogo para seleccionar el proveedor de correo
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle('Enviar Boletas por Correo')
        layout = QtWidgets.QVBoxLayout(dialog)

        # Campo Proveedor de correo
        provider_label = QtWidgets.QLabel('Proveedor de Correo:')
        provider_combo = QtWidgets.QComboBox()
        provider_combo.addItem('Gmail')
        provider_combo.addItem('Outlook')
        layout.addWidget(provider_label)
        layout.addWidget(provider_combo)

        # Campo DE (Correo remitente)
        from_label = QtWidgets.QLabel('De:')
        from_edit = QtWidgets.QLineEdit()
        layout.addWidget(from_label)
        layout.addWidget(from_edit)

        # Campo Clave (Contraseña)
        password_label = QtWidgets.QLabel('Clave:')
        password_edit = QtWidgets.QLineEdit()
        password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(password_label)
        layout.addWidget(password_edit)

        # Campo Para (Correos destinatarios)
        to_label = QtWidgets.QLabel('Para:')
        to_edit = QtWidgets.QLineEdit()
        layout.addWidget(to_label)
        layout.addWidget(to_edit)

        # Botones Aceptar y Cancelar
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        layout.addWidget(button_box)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        # Mostrar el cuadro de diálogo y obtener los valores ingresados
        if not dialog.exec():
            return

        # Obtener los valores ingresados
        provider = provider_combo.currentText()
        from_address = from_edit.text()
        password = password_edit.text()
        to_addresses = to_edit.text().split(';')

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = ', '.join(to_addresses)
        msg['Subject'] = 'Boletas Konecta'

        # Obtener los archivos seleccionados en la ruta de boletas_pdf
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(None, 'Adjuntar Boletas', ruta_boletas_pdf, 'PDF Files (*.pdf)')

        if not selected_files:
            QtWidgets.QMessageBox.warning(None, 'Advertencia', 'No se han seleccionado archivos.')
            return

        try:
            # Adjuntar los archivos seleccionados al mensaje
            for file_path in selected_files:
                with open(file_path, 'rb') as file:
                    part = MIMEApplication(file.read(), Name=os.path.basename(file_path))
                    part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file_path))
                    msg.attach(part)

            # Establecer conexión con el servidor SMTP según el proveedor seleccionado
            if provider == 'Gmail':
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
            elif provider == 'Outlook':
                smtp_server = 'smtp.office365.com'
                smtp_port = 587
            else:
                QtWidgets.QMessageBox.warning(None, 'Advertencia', 'Proveedor de correo no válido.')
                return

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(from_address, password)
                server.send_message(msg)

            QtWidgets.QMessageBox.information(None, 'Éxito', 'El correo se ha enviado correctamente.')

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', 'Ha ocurrido un error al enviar el correo:\n{}'.format(str(e)))
            print(f'Error', 'Ha ocurrido un error al enviar el correo:\n{}'.format(str(e)))


if __name__=='__main__':
   app= QtWidgets.QApplication(sys.argv)
   mi_app = Main()
   mi_app.show()
   sys.exit(app.exec_())
