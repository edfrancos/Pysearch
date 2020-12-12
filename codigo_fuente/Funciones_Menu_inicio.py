import sys
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow, QStackedWidget
from Menu_inicial import *
from sqlite3 import Error
import re
from Funciones_Menu_principal import*

class Funciones_inicio(QMainWindow):
    def __init__(self):
        """Funcion que declara la clase general y establece un estado inicial de los objetos a utilizar en el programa
        :param Variable self: Variable que es un objeto
        :return: None
        """
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_inicio_registrar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_registro))
        self.ui.btn_registrar.clicked.connect(self.registrar)
        self.ui.btn_inicio_ingresar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_Ingreso))
        self.ui.btn_registrar_regresar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.btn_login_regresar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.btn_iniciar_sesion.clicked.connect(self.control_login)
        self.ui.btn_caracol.toggled.connect(self.fav_caracol)
        self.ui.btn_cartoon.toggled.connect(self.fav_cartoon)
        self.ui.btn_fox.toggled.connect(self.fav_fox)
        self.ui.btn_rcn.toggled.connect(self.fav_rcn)
        self.ui.btn_favoritos_finalizar.clicked.connect(self.user_favs)
        self.conexion = None
        self.caracol = None
        self.fox = None
        self.cartoon = None
        self.rcn = None
        self.advertencias = QMessageBox()
        self.show()

    def registrar(self):
        """Recibe la informacion guardada en los objetos de nombre txt_nombre, txt_username, txt_clve y txt_clave_confirm pertenecientes a la clase Ui_Dialog.
        :param Variable self: Variable que es un objeto
        :return: None
        """
        nombre_usuario = self.ui.txt_nombre.text().strip()
        nombre_username = self.ui.txt_username.text().strip()
        clave = self.ui.txt_clave.text()
        clave_confirm = self.ui.txt_clave_confirm.text()
        if re.search('[a-zA-Z]+', nombre_usuario) is not None:
            if re.search('[0-9]+', nombre_usuario) is None:
                self.conexion = sqlite3.connect("DB1.db")
                if not self.existe_nombre(nombre_username):
                    if len(nombre_username) >= 7:
                        if re.search('[a-zA-z]+',clave) is not None:
                            if len(clave) >= 7:
                                if clave == clave_confirm:
                                    sql = '''INSERT INTO Usuarios (Nombres,Username,Contraseña) VALUES ('{}','{}','{}')'''.format(nombre_usuario,
                                                                                                              nombre_username,clave_confirm)
                                    cur = self.conexion.cursor()
                                    cur.execute(sql)
                                    self.conexion.commit()
                                    self.conexion = sqlite3.connect("DB1.db")
                                    sql = '''UPDATE user_actual set user_act = '{}' where  id = 1'''.format(nombre_username)
                                    cur = self.conexion.cursor()
                                    cur.execute(sql)
                                    self.ui.btn_registrar.setVisible(False)
                                    self.ui.btn_favoritos.setVisible(True)
                                    self.ui.btn_favoritos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_favoritos))
                                else:
                                    self.advertencias.setText("Las contraseñas no coinciden")
                                    self.advertencias.setIcon(QMessageBox.Information)
                                    self.advertencias.setWindowTitle("Important")
                                    self.advertencias.exec_()
                            else:
                                self.advertencias.setText("La Contraseña debe tener de 8 a 16 caracteres")
                                self.advertencias.setIcon(QMessageBox.Information)
                                self.advertencias.setWindowTitle("Important-TypeError")
                                self.advertencias.exec_()
                        else:
                            self.advertencias.setText("La Contraseña no debe tener espacios en blanco o empezar por un caracter numéricos")
                            self.advertencias.setIcon(QMessageBox.Information)
                            self.advertencias.setWindowTitle("Important-TypeError")
                            self.advertencias.exec_()
                    else:
                        self.advertencias.setText("El Username debe tener de 8 a 16 caracteres")
                        self.advertencias.setIcon(QMessageBox.Information)
                        self.advertencias.setWindowTitle("Important-TypeError")
                        self.advertencias.exec_()
                else:
                    self.advertencias.setText("El nombre de usaurio ya existe")
                    self.advertencias.setIcon(QMessageBox.Critical)
                    self.advertencias.setWindowTitle("Error")
                    self.advertencias.exec_()
            else:
                self.advertencias.setText("El nombre no debe incluir caracteres numéricos")
                self.advertencias.setIcon(QMessageBox.Warning)
                self.advertencias.setWindowTitle("Important-TypeError")
                self.advertencias.exec_()
        else:
            self.advertencias.setText("No ha ingresado un Nombre")
            self.advertencias.setIcon(QMessageBox.Information)
            self.advertencias.setWindowTitle("Important-TypeError")
            self.advertencias.exec_()

        def existe_nombre(self, user):
        sql = '''SELECT * FROM usuarios WHERE Username = ?;'''
        cur = self.conexion.cursor()
        resultado = cur.execute(sql, (user,)).fetchall()
        return len(resultado) > 0

    def control_login(self):
        """ Contiene el control de los logeos para omitir errores en la base de datos
        :param Variable self: Variable que es un objeto
        :return: None
        """
            username = self.ui.txt_login_username.text()
            clave = self.ui.txt_login_clave.text()
            self.conexion = sqlite3.connect("DB1.db")
            sql = '''UPDATE user_actual set user_act = '{}' where  id = 1'''.format(username)
            cur = self.conexion.cursor()
            cur.execute(sql)
            self.conexion.commit()
            if re.search('[a-zA-Z]+', username) is not None:
                self.conexion = sqlite3.connect("DB1.db")
                if re.search('[a-zA-z]+', clave) is not None:
                    if self.log_in(username,clave):
                        Funciones_inicio.hide(self)
                        self.inicio_1 = QtWidgets.QMainWindow()
                        self.inicio = Menu_principal()
                        self.inicio_1.show()
                    else:
                        self.advertencias.setText("Usuario o Contraseña incorrectos")
                        self.advertencias.setIcon(QMessageBox.Critical)
                        self.advertencias.setWindowTitle("Error")
                        self.advertencias.exec_()

                else:
                    self.advertencias.setText("No ha ingresado una Contraseña")
                    self.advertencias.setIcon(QMessageBox.Information)
                    self.advertencias.setWindowTitle("Important-TypeError")
                    self.advertencias.exec_()
            else:
                self.advertencias.setText("No ha ingresado un Usuario")
                self.advertencias.setIcon(QMessageBox.Information)
                self.advertencias.setWindowTitle("Important-TypeError")
                self.advertencias.exec_()

    def log_in(self, user, contra):
        """Permite el logeo de el usuario al iniciar
        :param Variable self: Variable que es un objeto
        :return: None
        """
        sql = '''SELECT * FROM usuarios WHERE Username = '{}' AND Contraseña = '{}' '''.format(user,contra)
        cur =self.conexion.cursor()
        resultado_1 = cur.execute(sql).fetchall()
        return len(resultado_1) > 0
    def fav_caracol(self):
        """reconoce si seleccionó como favorito a Caracol
        :param Variable self: Variable que es un objeto
        :return: None
        """
        if self.ui.btn_caracol.isChecked() == True:
            self.ui.btn_check_caracol.setVisible(True)
            self.caracol = True
        else:
            self.ui.btn_check_caracol.setVisible(False)
            self.caracol = False
    def fav_cartoon(self):
        """reconoce si seleccionó como favorito a Cartoon
        :param Variable self: Variable que es un objeto
        :return: None
        """
        if self.ui.btn_cartoon.isChecked() == True:
            self.ui.btn_check_cartoon.setVisible(True)
            self.cartoon = True
        else:
            self.ui.btn_check_cartoon.setVisible(False)
            self.cartoon = False
    def fav_fox(self):
        """reconoce si seleccionó como favorito a Fox
        :param Variable self: Variable que es un objeto
        :return: None
        """
        if self.ui.btn_fox.isChecked() == True:
            self.ui.btn_check_fox.setVisible(True)
            self.fox = True
        else:
            self.ui.btn_check_fox.setVisible(False)
            self.fox = False
    def fav_rcn(self):
        """reconoce si seleccionó como favorito a RCN
        :param Variable self: Variable que es un objeto
        :return: None
        """
        if self.ui.btn_rcn.isChecked() == True:
            self.ui.btn_check_rcn.setVisible(True)
            self.rcn = True
        else:
            self.ui.btn_check_rcn.setVisible(False)
            self.rcn = False
    def user_favs(self):
        """reconoce los programas en general seleccionados como favoritos
        :param Variable self: Variable que es un objeto
        :return: None
        """
        nombre_username = self.ui.txt_username.text()
        print("llegue")
        if self.caracol:
            caracol = 1
        else: caracol = 0
        if self.cartoon:
            cartoon = 1
        else: cartoon = 0
        if self.fox:
            fox = 1
        else: fox = 0
        if self.rcn:
            rcn = 1
        else: rcn = 0
        sql = '''SELECT ID FROM Usuarios WHERE Username = "{}"'''.format(nombre_username)
        cur = self.conexion.cursor()
        resultado = cur.execute(sql).fetchall()
        resultado = resultado[0][0]
        sql_2 = '''INSERT INTO favoritos (ID,Caracol,Cartoon,Fox,Rcn) VALUES ({},{},{},{},{})'''.format(resultado,caracol,cartoon,fox,rcn)
        cur_2 = self.conexion.cursor()
        cur_2.execute(sql_2)
        self.conexion.commit()
        Funciones_inicio.hide(self)
        self.inicio_1 = QtWidgets.QMainWindow()
        self.inicio = Menu_principal()
        self.inicio_1.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Funciones_inicio()
    gui.show()
    sys.exit(app.exec_())
