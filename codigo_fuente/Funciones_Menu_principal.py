import sys
import sqlite3
from urllib.request import urlopen
import re
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QTableWidgetItem
from PyQt5.QtCore import QPropertyAnimation, QRect, QAbstractAnimation
from Menu_principal import *
from dicc_program import *
from Funciones_Menu_inicio import *
from sqlite3 import Error
from dicc_program import General_Canal_Dic


class Menu_principal(QMainWindow):
    def __init__(self):
        """ declara todos los botones a utilizar y sus propiedades
        :param None:
        :return: None
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inicio = Funciones_inicio()
        self.conexion = sqlite3.connect("DB1.db")
        self.ui.tbl_prograamacion.setColumnWidth(0,300)
        self.ui.tbl_prograamacion.setColumnWidth(1, 300)
        self.ui.tbl_prograamacion.setColumnWidth(2, 150)
        self.x = 1
        self.cambiar_botones()
        self.ui.frm_slide_imagen_slider_1.setStyleSheet("background: url(:/slider/banner_{}.jpg)".format(self.x))
        self.ui.btn_slider_anterior.clicked.connect(self.anterior)
        self.ui.btn_slider_siguiente.clicked.connect(self.siguiente)
        self.ui.btn_inicio_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_inicial))
        self.ui.btn_inicio_peliculas.clicked.connect(lambda: print(General_Canal_Dic))
        self.ui.btn_inicio_canales.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales))
        self.ui.btn_search_inicial.clicked.connect(self.busqueda)
        self.ui.btn_fav_1.clicked.connect(self.redirigir_fav_1)
        self.ui.btn_fav_2.clicked.connect(self.redirigir_fav_2)
        self.ui.btn_fav_3.clicked.connect(self.redirigir_fav_3)
        self.ui.btn_fav_4.clicked.connect(self.redirigir_fav_4)
        self.ui.btn_canal_1.clicked.connect(self.caracol)
        self.ui.btn_canal_2.clicked.connect(self.cartoon)
        self.ui.btn_canal_3.clicked.connect(self.Fox)
        self.ui.btn_canal_4.clicked.connect(self.rcn)
        self.show()

    def cambiar_botones(self):
        """ determina los canalesfavoritos para luego mostrarlos en la pantalla principal
        :param None:
        :return: None
        """
        self.ui.btn_fav_1.setVisible(False)
        self.ui.btn_fav_2.setVisible(False)
        self.ui.btn_fav_3.setVisible(False)
        self.ui.btn_fav_4.setVisible(False)
        sql = '''SELECT user_act FROM user_actual WHERE id = 1'''
        cur = self.conexion.cursor()
        user_act = cur.execute(sql).fetchall()
        user_act = user_act[0][0]
        sql = '''SELECT ID FROM Usuarios WHERE Username = "{}"'''.format(user_act)
        cur = self.conexion.cursor()
        resultado = cur.execute(sql).fetchall()
        resultado = resultado[0][0]
        sql = '''SELECT * FROM Favoritos where ID ={}'''.format(resultado)
        cur = self.conexion.cursor()
        favs = cur.execute(sql).fetchall()
        favs = favs[0][1:]
        favs = [int(i_favs)for i_favs in favs]
        canales = ["caracol","cartoon","fox","rcn"]
        c = 0
        btn_1 = True
        btn_2 = True
        btn_3 = True
        btn_4 = True
        for i in favs:
            if i == 1:
                if btn_1:
                    self.canal_fav_1=canales[c]
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/Icon_{}.png".format(canales[c])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.btn_fav_1.setIcon(icon)
                    self.ui.btn_fav_1.setIconSize(QtCore.QSize(130, 130))
                    self.ui.btn_fav_1.setVisible(True)
                    if canales[c] == "caracol":
                        self.ui.btn_fav_1.setIconSize(QtCore.QSize(80, 80))
                    btn_1 = False
                    c += 1
                elif btn_2:
                    self.canal_fav_2 = canales[c]
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/Icon_{}.png".format(canales[c])), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    self.ui.btn_fav_2.setIcon(icon)
                    self.ui.btn_fav_2.setIconSize(QtCore.QSize(130, 130))
                    self.ui.btn_fav_2.setVisible(True)
                    btn_2 = False
                    c += 1
                elif btn_3:
                    self.canal_fav_3 = canales[c]
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/Icon_{}.png".format(canales[c])), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    self.ui.btn_fav_3.setIcon(icon)
                    self.ui.btn_fav_3.setIconSize(QtCore.QSize(130, 130))
                    self.ui.btn_fav_3.setVisible(True)
                    btn_3 = False
                    c += 1
                elif btn_4:
                    self.canal_fav_4 = canales[c]
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/Icon_{}.png".format(canales[c])), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    self.ui.btn_fav_4.setIcon(icon)
                    self.ui.btn_fav_4.setIconSize(QtCore.QSize(130, 130))
                    self.ui.btn_fav_4.setVisible(True)
                    btn_4 = False
                    c += 1
            else:
                c += 1
    def anterior(self):
        """ 
        """
        self.ui.frm_slide_imagen_slider_2.setGeometry(QtCore.QRect(840, 0, 840, 189))
        if self.x != 1:
            self.x -= 1
            self.ui.frm_slide_imagen_slider_1.setStyleSheet("background-image : url(banner_{}.jpg);".format(self.x+1))
        else:
            self.x = 9
            self.ui.frm_slide_imagen_slider_1.setStyleSheet("background-image : url(banner_1.jpg);")
        self.ui.frm_slide_imagen_slider_3.setStyleSheet("background-image : url(banner_{}.jpg);".format(self.x))
        self.animacionMostar_1 = QPropertyAnimation(self.ui.frm_slide_imagen_slider_1, b"geometry")
        self.animacionMostar_1.setDuration(650)
        self.animacionMostar_1.setStartValue(QRect(0, 0, 840, 189))
        self.animacionMostar_1.setEndValue(QRect(840, 0, 840, 189))
        self.animacionMostar_1.start()
        self.ui.frm_slide_imagen_slider_1.setGeometry(QtCore.QRect(0,0,840,189))
        self.ui.frm_slide_imagen_slider_3.setGeometry(QtCore.QRect(-840, 0, 840, 189))
        self.animacionMostar = QPropertyAnimation(self.ui.frm_slide_imagen_slider_3, b"geometry")
        self.animacionMostar.setDuration(650)
        self.animacionMostar.setStartValue(QRect(-840, 0, 840, 189))
        self.animacionMostar.setEndValue(QRect(0, 0, 840, 189))
        self.animacionMostar.start()
        self.ui.frm_slide_imagen_slider_1.setGeometry(QtCore.QRect(0, 0, 840, 189))
        print(self.x)
    def siguiente(self):
        self.ui.frm_slide_imagen_slider_3.setGeometry(QtCore.QRect(-840, 0, 840, 189))
        if self.x != 9:
            self.ui.frm_slide_imagen_slider_1.setStyleSheet("background-image : url(banner_{}.jpg);".format(self.x))
        if self.x == 9:
            self.x = 1
            self.ui.frm_slide_imagen_slider_1.setStyleSheet("background-image : url(banner_9.jpg);")
        else:
            self.x += 1
        print(self.x)
        self.ui.frm_slide_imagen_slider_2.setStyleSheet("background-image : url(banner_{}.jpg);".format(self.x))
        self.animacionMostar = QPropertyAnimation(self.ui.frm_slide_imagen_slider_2, b"geometry")
        self.animacionMostar.setDuration(650)
        self.animacionMostar.setStartValue(QRect(840, 0, 840, 189))
        self.animacionMostar.setEndValue(QRect(0, 0, 840, 189))
        self.animacionMostar.start()
        self.animacionMostar_1 = QPropertyAnimation(self.ui.frm_slide_imagen_slider_1, b"geometry")
        self.animacionMostar_1.setDuration(650)
        self.animacionMostar_1.setStartValue(QRect(0, 0, 840, 189))
        self.animacionMostar_1.setEndValue(QRect(-840, 0, 840, 189))
        self.animacionMostar_1.start()
        self.ui.frm_slide_imagen_slider_2.setGeometry(QtCore.QRect(840, 0, 840, 189))
        self.ui.frm_slide_imagen_slider_1.setGeometry(QtCore.QRect(0, 0, 840, 189))

    def redirigir_fav_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
        if self.canal_fav_1 == "caracol":
            self.caracol()
        elif self.canal_fav_1 == "cartoon":
            self.cartoon()
        elif self.canal_fav_1 == "fox":
            self.Fox()
        elif self.canal_fav_1== "rcn":
            self.rcn()
    def redirigir_fav_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
        if self.canal_fav_2 == "caracol":
            self.caracol()
        elif self.canal_fav_2 == "cartoon":
            self.cartoon()
        elif self.canal_fav_2 == "fox":
            self.Fox()
        elif self.canal_fav_2 == "rcn":
            self.rcn()
    def redirigir_fav_3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
        if self.canal_fav_3 == "caracol":
            self.caracol()
        elif self.canal_fav_3 == "cartoon":
            self.cartoon()
        elif self.canal_fav_3 == "fox":
            self.Fox()
        elif self.canal_fav_3 == "rcn":
            self.rcn()
    def redirigir_fav_4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
        if self.canal_fav_4 == "caracol":
            self.caracol()
        elif self.canal_fav_4 == "cartoon":
            self.cartoon()
        elif self.canal_fav_4 == "fox":
            self.Fox()
        elif self.canal_fav_4 == "rcn":
            self.rcn()

    def seleccion_inicial(self):
        print("hello world")
    def caracol(self):
        fila = 0
        columna=0
        print(Dicc_Caracol)
        for programa in Dicc_Caracol:
            lista_carac = Dicc_Caracol.get(programa)
            for columna in range(2):
                self.ui.tbl_prograamacion.insertRow(fila)
                celda_1 = QTableWidgetItem(programa)
                celda_2 = QTableWidgetItem(lista_carac[0])
                celda_3 = QTableWidgetItem(lista_carac[1])
                self.ui.tbl_prograamacion.setItem(fila,0,celda_1)
                self.ui.tbl_prograamacion.setItem(fila,1,celda_2)
                self.ui.tbl_prograamacion.setItem(fila, 2, celda_3)
                columna += 1
            fila+=1
    def cartoon(self):
        fila = 0
        columna=0
        for programa in Dicc_CN:
            lista_carac = Dicc_CN.get(programa)
            for columna in range(2):
                self.ui.tbl_prograamacion.insertRow(fila)
                celda_1 = QTableWidgetItem(programa)
                celda_2 = QTableWidgetItem(lista_carac[0])
                celda_3 = QTableWidgetItem(lista_carac[1])
                self.ui.tbl_prograamacion.setItem(fila,0,celda_1)
                self.ui.tbl_prograamacion.setItem(fila,1,celda_2)
                self.ui.tbl_prograamacion.setItem(fila, 2, celda_3)
                columna += 1
            fila+=1
    def Fox(self):
        fila = 0
        columna=0
        for programa in Dicc_Fox:
            lista_carac = Dicc_Fox.get(programa)
            for columna in range(2):
                self.ui.tbl_prograamacion.insertRow(fila)
                celda_1 = QTableWidgetItem(programa)
                celda_2 = QTableWidgetItem(lista_carac[0])
                celda_3 = QTableWidgetItem(lista_carac[1])
                self.ui.tbl_prograamacion.setItem(fila,0,celda_1)
                self.ui.tbl_prograamacion.setItem(fila,1,celda_2)
                self.ui.tbl_prograamacion.setItem(fila, 2, celda_3)
                columna += 1
            fila+=1
    def rcn(self):
        fila = 0
        columna=0
        for programa in Dicc_RCN:
            lista_carac = Dicc_RCN.get(programa)
            for columna in range(2):
                self.ui.tbl_prograamacion.insertRow(fila)
                celda_1 = QTableWidgetItem(programa)
                celda_2 = QTableWidgetItem(lista_carac[0])
                celda_3 = QTableWidgetItem(lista_carac[1])
                self.ui.tbl_prograamacion.setItem(fila,0,celda_1)
                self.ui.tbl_prograamacion.setItem(fila,1,celda_2)
                self.ui.tbl_prograamacion.setItem(fila, 2, celda_3)
                columna += 1
            fila+=1

    def busqueda(self):
        busqueda = self.ui.txt_buscar_inicial.text().strip()
        busqueda.lower()
        if busqueda == "caracol":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
            self.caracol()
        elif busqueda == "cartoon network":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
            self.cartoon()
        elif busqueda == "rcn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
            self.rcn()
        elif busqueda == "fox":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_canales)
            self.fox()
        elif busqueda in Dicc_Caracol:
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_busqueda)
            info = Dicc_Caracol.get(busqueda)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/Icon_caracol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.btn_busqueda_canal.setIcon(icon)
            self.ui.lbl_busqueda_dias_emi.setText(info[0])
            self.ui.lbl_busqueda_horas_emi.setText(info[1])
            self.ui.lbl_busqueda_canal_emi.setText("Caracol")
            self.ui.lbl_busqueda_titulo.setText(busqueda)
            self.ui.lbl_busqueda_tipo.setText(info[2])
            self.ui.lbl_busqueda_sinopsis.setText(info[3])
        elif busqueda in Dicc_CN:
            info= Dicc_CN.get(busqueda)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/Icon_cartoon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_busqueda)
            self.ui.btn_busqueda_canal.setIcon(icon)
            self.ui.lbl_busqueda_dias_emi.setText(info[0])
            self.ui.lbl_busqueda_horas_emi.setText(info[1])
            self.ui.lbl_busqueda_canal_emi.setText("Carton Network")
            self.ui.lbl_busqueda_titulo.setText(busqueda)
            self.ui.lbl_busqueda_tipo.setText(info[2])
            self.ui.lbl_busqueda_sinopsis.setText(info[3])
        elif busqueda in Dicc_RCN:
            info = Dicc_RCN.get(busqueda)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/Icon_rcn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_busqueda)
            self.ui.btn_busqueda_canal.setIcon(icon)
            self.ui.lbl_busqueda_dias_emi.setText(info[0])
            self.ui.lbl_busqueda_horas_emi.setText(info[1])
            self.ui.lbl_busqueda_canal_emi.setText("RCN")
            self.ui.lbl_busqueda_titulo.setText(busqueda)
            self.ui.lbl_busqueda_tipo.setText(info[2])
            self.ui.lbl_busqueda_sinopsis.setText(info[3])
        elif busqueda in Dicc_Fox:
            info = Dicc_Fox.get(busqueda)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/Icon_fox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_busqueda)
            self.ui.btn_busqueda_canal.setIcon(icon)
            self.ui.lbl_busqueda_dias_emi.setText(info[0])
            self.ui.lbl_busqueda_horas_emi.setText(info[1])
            self.ui.lbl_busqueda_canal_emi.setText("FOX")
            self.ui.lbl_busqueda_titulo.setText(busqueda)
            self.ui.lbl_busqueda_tipo.setText(info[2])
            self.ui.lbl_busqueda_sinopsis.setText(info[3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Menu_principal()
    gui.show()
    sys.exit(app.exec_())
