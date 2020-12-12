from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        """"Este script contiene la clase principal y padre de todo el diseño grafico de la interfaz en su apartado inicial, por ello este script es practicamente infuncional en este estado,todo esto debido a que todo los botones, paginas, etiquetas y demas widgets no tienen asignado un evento especifico.Cabe destacar que dichos eventos de funcionalidad se desarrollan el script Funciones_Menu_Inicial.
        :param Variable self: Variable es un objeto
        :param Clase Dialog: Dialog es una clase
        :return: None
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 550)
        Dialog.setMinimumSize(QtCore.QSize(400, 550))
        Dialog.setMaximumSize(QtCore.QSize(400, 550))
        Dialog.setToolTip("")
        Dialog.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.506, cy:0.506, radius:0.5, fx:0.511, fy:0.511, stop:0 rgba(0, 42, 86, 255), stop:0.306818 rgba(0, 31, 65, 255), stop:0.625 rgba(0, 31, 65, 255), stop:1 rgba(0, 22, 45, 255));\n"
"QFrame{\n"
"background:rgba(0,0,10,0.5);\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit{\n"
"background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 20, 381, 571))
        self.stackedWidget.setStyleSheet("background:transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_inicio = QtWidgets.QWidget()
        self.page_inicio.setObjectName("page_inicio")
        self.frame = QtWidgets.QFrame(self.page_inicio)
        self.frame.setGeometry(QtCore.QRect(10, 0, 361, 511))
        self.frame.setStyleSheet("QFrame{\n"
"background:rgba(0,0,10,0.5);\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_inicio_pysearch = QtWidgets.QLabel(self.frame)
        self.lbl_inicio_pysearch.setGeometry(QtCore.QRect(40, 70, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.lbl_inicio_pysearch.setFont(font)
        self.lbl_inicio_pysearch.setStyleSheet("background:transparent;")
        self.lbl_inicio_pysearch.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_inicio_pysearch.setObjectName("lbl_inicio_pysearch")
        self.lbl_inicio_saludo = QtWidgets.QLabel(self.frame)
        self.lbl_inicio_saludo.setGeometry(QtCore.QRect(10, 150, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.lbl_inicio_saludo.setFont(font)
        self.lbl_inicio_saludo.setStyleSheet("background:transparent;")
        self.lbl_inicio_saludo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_inicio_saludo.setObjectName("lbl_inicio_saludo")
        self.btn_inicio_ingresar = QtWidgets.QPushButton(self.frame)
        self.btn_inicio_ingresar.setGeometry(QtCore.QRect(60, 300, 241, 41))
        self.btn_inicio_ingresar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"font-weigth:bold;\n"
"border-radius:18px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icon_login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inicio_ingresar.setIcon(icon)
        self.btn_inicio_ingresar.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio_ingresar.setObjectName("btn_inicio_ingresar")
        self.btn_inicio_registrar = QtWidgets.QPushButton(self.frame)
        self.btn_inicio_registrar.setGeometry(QtCore.QRect(60, 420, 241, 41))
        self.btn_inicio_registrar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"font-weigth:bold;\n"
"border-radius:18px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icon_registrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inicio_registrar.setIcon(icon1)
        self.btn_inicio_registrar.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio_registrar.setObjectName("btn_inicio_registrar")
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_registro = QtWidgets.QWidget()
        self.page_registro.setObjectName("page_registro")
        self.frame_2 = QtWidgets.QFrame(self.page_registro)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 361, 521))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,10,0.5);\n"
"border-radius:15px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_registro = QtWidgets.QLabel(self.frame_2)
        self.lbl_registro.setGeometry(QtCore.QRect(100, 40, 171, 51))
        self.lbl_registro.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:40px; \n"
"background:transparent; \n"
"")
        self.lbl_registro.setObjectName("lbl_registro")
        self.lbl_registro_nombres = QtWidgets.QLabel(self.frame_2)
        self.lbl_registro_nombres.setGeometry(QtCore.QRect(40, 130, 121, 21))
        self.lbl_registro_nombres.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; \n"
"")
        self.lbl_registro_nombres.setObjectName("lbl_registro_nombres")
        self.txt_nombre = QtWidgets.QLineEdit(self.frame_2)
        self.txt_nombre.setGeometry(QtCore.QRect(40, 160, 271, 20))
        self.txt_nombre.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_nombre.setMaxLength(32)
        self.txt_nombre.setObjectName("txt_nombre")
        self.lbl_registro_username = QtWidgets.QLabel(self.frame_2)
        self.lbl_registro_username.setGeometry(QtCore.QRect(40, 210, 111, 21))
        self.lbl_registro_username.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; ")
        self.lbl_registro_username.setObjectName("lbl_registro_username")
        self.txt_username = QtWidgets.QLineEdit(self.frame_2)
        self.txt_username.setGeometry(QtCore.QRect(40, 240, 271, 20))
        self.txt_username.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_username.setMaxLength(16)
        self.txt_username.setObjectName("txt_username")
        self.lbl_registro_clave = QtWidgets.QLabel(self.frame_2)
        self.lbl_registro_clave.setGeometry(QtCore.QRect(40, 290, 131, 21))
        self.lbl_registro_clave.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; ")
        self.lbl_registro_clave.setObjectName("lbl_registro_clave")
        self.txt_clave = QtWidgets.QLineEdit(self.frame_2)
        self.txt_clave.setGeometry(QtCore.QRect(40, 320, 271, 20))
        self.txt_clave.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_clave.setMaxLength(20)
        self.txt_clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_clave.setObjectName("txt_clave")
        self.lbl_registro_clave_confirm = QtWidgets.QLabel(self.frame_2)
        self.lbl_registro_clave_confirm.setGeometry(QtCore.QRect(40, 370, 261, 21))
        self.lbl_registro_clave_confirm.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; ")
        self.lbl_registro_clave_confirm.setObjectName("lbl_registro_clave_confirm")
        self.txt_clave_confirm = QtWidgets.QLineEdit(self.frame_2)
        self.txt_clave_confirm.setGeometry(QtCore.QRect(40, 400, 271, 20))
        self.txt_clave_confirm.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_clave_confirm.setMaxLength(20)
        self.txt_clave_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_clave_confirm.setObjectName("txt_clave_confirm")
        self.btn_registrar = QtWidgets.QPushButton(self.frame_2)
        self.btn_registrar.setGeometry(QtCore.QRect(80, 450, 191, 41))
        self.btn_registrar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"font-weigth:bold;\n"
"border-radius:18px;\n"
"}")
        self.btn_favoritos = QtWidgets.QPushButton(self.frame_2)
        self.btn_favoritos.setGeometry(QtCore.QRect(80, 450, 191, 41))
        self.btn_favoritos.setVisible(False)
        self.btn_favoritos.setStyleSheet("QPushButton{\n"
                                         "font-family: calibri;\n"
                                         "background:transparent;\n"
                                         "color: white;\n"
                                         "text-transform: uppercase;\n"
                                         "letter-spacing: 2px;\n"
                                         "text-decoration:none;\n"
                                         "font-size:24px;\n"
                                         "overflow: hidden;\n"
                                         "transition: o.2s;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "color: white;\n"
                                         "border-bottom:1px solid white;\n"
                                         "border-top:1px solid white;\n"
                                         "border-left:1px solid white;\n"
                                         "border-right:1px solid white;\n"
                                         "font-weigth:bold;\n"
                                         "border-radius:18px;\n"
                                         "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icon_entrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_registrar.setIcon(icon2)
        self.btn_registrar.setIconSize(QtCore.QSize(20, 20))
        self.btn_registrar.setObjectName("btn_registrar")
        self.btn_favoritos.setIcon(icon2)
        self.btn_favoritos.setIconSize(QtCore.QSize(20, 20))
        self.btn_favoritos.setObjectName("btn_favoritos")
        self.btn_registrar_regresar = QtWidgets.QPushButton(self.frame_2)
        self.btn_registrar_regresar.setGeometry(QtCore.QRect(320, 10, 41, 41))
        self.btn_registrar_regresar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"")
        self.btn_registrar_regresar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icon_salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_registrar_regresar.setIcon(icon3)
        self.btn_registrar_regresar.setObjectName("btn_registrar_regresar")
        self.stackedWidget.addWidget(self.page_registro)
        self.page_Ingreso = QtWidgets.QWidget()
        self.page_Ingreso.setObjectName("page_Ingreso")
        self.frame_3 = QtWidgets.QFrame(self.page_Ingreso)
        self.frame_3.setGeometry(QtCore.QRect(10, 0, 361, 521))
        self.frame_3.setStyleSheet("QFrame{\n"
"background:rgba(0,0,10,0.5);\n"
"border-radius:15px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_registro_2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_registro_2.setGeometry(QtCore.QRect(60, 70, 241, 51))
        self.lbl_registro_2.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:40px; \n"
"background:transparent; \n"
"")
        self.lbl_registro_2.setObjectName("lbl_registro_2")
        self.label_inicio_usuario = QtWidgets.QLabel(self.frame_3)
        self.label_inicio_usuario.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.label_inicio_usuario.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; ")
        self.label_inicio_usuario.setObjectName("label_inicio_usuario")
        self.txt_login_username = QtWidgets.QLineEdit(self.frame_3)
        self.txt_login_username.setGeometry(QtCore.QRect(40, 240, 271, 20))
        self.txt_login_username.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_login_username.setMaxLength(16)
        self.txt_login_username.setObjectName("txt_login_username")
        self.label_inicio_clave = QtWidgets.QLabel(self.frame_3)
        self.label_inicio_clave.setGeometry(QtCore.QRect(40, 320, 131, 21))
        self.label_inicio_clave.setStyleSheet("font-family: century gothic;\n"
"color:white;\n"
"font-size:22px; \n"
"background:transparent; ")
        self.label_inicio_clave.setObjectName("label_inicio_clave")
        self.txt_login_clave = QtWidgets.QLineEdit(self.frame_3)
        self.txt_login_clave.setGeometry(QtCore.QRect(40, 360, 271, 20))
        self.txt_login_clave.setStyleSheet("background:transparent; \n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"")
        self.txt_login_clave.setMaxLength(20)
        self.txt_login_clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_login_clave.setObjectName("txt_login_clave")
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.frame_3)
        self.btn_iniciar_sesion.setGeometry(QtCore.QRect(70, 450, 221, 41))
        self.btn_iniciar_sesion.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"font-weigth:bold;\n"
"border-radius:18px;\n"
"}")
        self.btn_iniciar_sesion.setIcon(icon)
        self.btn_iniciar_sesion.setIconSize(QtCore.QSize(20, 20))
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.btn_login_regresar = QtWidgets.QPushButton(self.frame_3)
        self.btn_login_regresar.setGeometry(QtCore.QRect(320, 10, 41, 41))
        self.btn_login_regresar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"")
        self.btn_login_regresar.setText("")
        self.btn_login_regresar.setIcon(icon3)
        self.btn_login_regresar.setObjectName("btn_login_regresar")
        self.stackedWidget.addWidget(self.page_Ingreso)
        self.page_favoritos = QtWidgets.QWidget()
        self.page_favoritos.setObjectName("page_favoritos")
        self.frame_4 = QtWidgets.QFrame(self.page_favoritos)
        self.frame_4.setGeometry(QtCore.QRect(10, 0, 361, 511))
        self.frame_4.setStyleSheet("QFrame{\n"
"background:rgba(0,0,10,0.5);\n"
"border-radius:15px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lbl_favoritos_tusfav = QtWidgets.QLabel(self.frame_4)
        self.lbl_favoritos_tusfav.setGeometry(QtCore.QRect(30, 30, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.lbl_favoritos_tusfav.setFont(font)
        self.lbl_favoritos_tusfav.setStyleSheet("background:transparent;")
        self.lbl_favoritos_tusfav.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_favoritos_tusfav.setObjectName("lbl_favoritos_tusfav")
        self.lbl_favoritos_1 = QtWidgets.QLabel(self.frame_4)
        self.lbl_favoritos_1.setGeometry(QtCore.QRect(10, 110, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.lbl_favoritos_1.setFont(font)
        self.lbl_favoritos_1.setStyleSheet("background:transparent;")
        self.lbl_favoritos_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_favoritos_1.setObjectName("lbl_favoritos_1")
        self.btn_favoritos_finalizar = QtWidgets.QPushButton(self.frame_4)
        self.btn_favoritos_finalizar.setGeometry(QtCore.QRect(60, 450, 241, 41))
        self.btn_favoritos_finalizar.setStyleSheet("QPushButton{\n"
"font-family: calibri;\n"
"background:transparent;\n"
"color: white;\n"
"text-transform: uppercase;\n"
"letter-spacing: 2px;\n"
"text-decoration:none;\n"
"font-size:24px;\n"
"overflow: hidden;\n"
"transition: o.2s;\n"
"}\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-bottom:1px solid white;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"font-weigth:bold;\n"
"border-radius:18px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Icon_verificado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_favoritos_finalizar.setIcon(icon4)
        self.btn_favoritos_finalizar.setIconSize(QtCore.QSize(20, 20))
        self.btn_favoritos_finalizar.setObjectName("btn_favoritos_finalizar")
        self.lbl_favoritos_2 = QtWidgets.QLabel(self.frame_4)
        self.lbl_favoritos_2.setGeometry(QtCore.QRect(10, 130, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.lbl_favoritos_2.setFont(font)
        self.lbl_favoritos_2.setStyleSheet("background:transparent;")
        self.lbl_favoritos_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_favoritos_2.setObjectName("lbl_favoritos_2")
        self.btn_caracol = QtWidgets.QPushButton(self.frame_4)
        self.btn_caracol.setGeometry(QtCore.QRect(50, 190, 101, 81))
        self.btn_caracol.setText("")
        self.btn_caracol.setCheckable(True)
        self.btn_caracol.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Icon_caracol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_caracol.setIcon(icon5)
        self.btn_caracol.setIconSize(QtCore.QSize(80, 80))
        self.btn_caracol.setObjectName("btn_caracol")
        self.btn_cartoon = QtWidgets.QPushButton(self.frame_4)
        self.btn_cartoon.setGeometry(QtCore.QRect(210, 190, 101, 81))
        self.btn_cartoon.setText("")
        self.btn_cartoon.setCheckable(True)
        self.btn_cartoon.setChecked(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Icon_cartoon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cartoon.setIcon(icon6)
        self.btn_cartoon.setIconSize(QtCore.QSize(100, 100))
        self.btn_cartoon.setObjectName("btn_cartoon")
        self.btn_rcn = QtWidgets.QPushButton(self.frame_4)
        self.btn_rcn.setGeometry(QtCore.QRect(210, 300, 101, 81))
        self.btn_rcn.setCheckable(True)
        self.btn_rcn.setChecked(False)
        self.btn_rcn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Icon_rcn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rcn.setIcon(icon7)
        self.btn_rcn.setIconSize(QtCore.QSize(100, 100))
        self.btn_rcn.setObjectName("btn_rcn")
        self.btn_fox = QtWidgets.QPushButton(self.frame_4)
        self.btn_fox.setGeometry(QtCore.QRect(50, 300, 101, 81))
        self.btn_fox.setCheckable(True)
        self.btn_fox.setChecked(False)
        self.btn_fox.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/Icon_fox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fox.setIcon(icon8)
        self.btn_fox.setIconSize(QtCore.QSize(100, 100))
        self.btn_fox.setObjectName("btn_fox")
        self.btn_check_caracol = QtWidgets.QPushButton(self.frame_4)
        self.btn_check_caracol.setGeometry(QtCore.QRect(40, 180, 31, 31))
        self.btn_check_caracol.setText("")
        self.btn_check_caracol.setVisible(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/Icono_check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_check_caracol.setIcon(icon9)
        self.btn_check_caracol.setObjectName("btn_check_caracol")
        self.btn_check_cartoon = QtWidgets.QPushButton(self.frame_4)
        self.btn_check_cartoon.setGeometry(QtCore.QRect(190, 180, 31, 31))
        self.btn_check_cartoon.setText("")
        self.btn_check_cartoon.setVisible(False)
        self.btn_check_cartoon.setIcon(icon9)
        self.btn_check_cartoon.setObjectName("btn_check_cartoon")
        self.btn_check_fox = QtWidgets.QPushButton(self.frame_4)
        self.btn_check_fox.setGeometry(QtCore.QRect(30, 300, 21, 21))
        self.btn_check_fox.setText("")
        self.btn_check_fox.setVisible(False)
        self.btn_check_fox.setIcon(icon9)
        self.btn_check_fox.setObjectName("btn_check_fox")
        self.btn_check_rcn = QtWidgets.QPushButton(self.frame_4)
        self.btn_check_rcn.setGeometry(QtCore.QRect(190, 290, 31, 31))
        self.btn_check_rcn.setText("")
        self.btn_check_rcn.setVisible(False)
        self.btn_check_rcn.setIcon(icon9)
        self.btn_check_rcn.setObjectName("btn_check_rcn")
        self.stackedWidget.addWidget(self.page_favoritos)
        Dialog.setCentralWidget(self.centralwidget)
        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menu Inicio"))
        self.lbl_inicio_pysearch.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#f0f0f0;\">Py</span><span style=\" font-size:48pt; color:#f0f0f0;\">search</span><span style=\" font-size:48pt; font-weight:600; color:#f0f0f0;\">!</span></p></body></html>"))
        self.lbl_inicio_saludo.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#f1f1f1;\">Disfruta</span><span style=\" font-size:11pt; color:#f1f1f1;\"> donde quieras, en el momento que quieras.</span></p></body></html>"))
        self.btn_inicio_ingresar.setText(_translate("Dialog", "INGRESAR"))
        self.btn_inicio_registrar.setText(_translate("Dialog", "registrar"))
        self.lbl_registro.setText(_translate("Dialog", "Registro"))
        self.lbl_registro_nombres.setText(_translate("Dialog", "Nombre/s"))
        self.txt_nombre.setPlaceholderText(_translate("Dialog", "Nombres/s"))
        self.lbl_registro_username.setText(_translate("Dialog", "Username"))
        self.txt_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.lbl_registro_clave.setText(_translate("Dialog", "Contraseña"))
        self.txt_clave.setPlaceholderText(_translate("Dialog", "**********"))
        self.lbl_registro_clave_confirm.setText(_translate("Dialog", "Confirmar Contraseña"))
        self.txt_clave_confirm.setPlaceholderText(_translate("Dialog", "**********"))
        self.btn_registrar.setText(_translate("Dialog", "Registrar"))
        self.btn_favoritos.setText(_translate("Dialog", "Continuar"))
        self.lbl_registro_2.setText(_translate("Dialog", "Inicia Sesión"))
        self.label_inicio_usuario.setText(_translate("Dialog", "Username"))
        self.txt_login_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.label_inicio_clave.setText(_translate("Dialog", "Contraseña"))
        self.txt_login_clave.setPlaceholderText(_translate("Dialog", "**********"))
        self.btn_iniciar_sesion.setText(_translate("Dialog", "iniciar sesión"))
        self.lbl_favoritos_tusfav.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#dddddd;\">Tus</span><span style=\" color:#dddddd;\"> Favoritos</span></p></body></html>"))
        self.lbl_favoritos_1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ebebeb;\">Para nosotros es importante</span></p><p><span style=\" color:#ebebeb;\"><br/></span></p></body></html>"))
        self.btn_favoritos_finalizar.setText(_translate("Dialog", "finalizar"))
        self.lbl_favoritos_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ebebeb;\">conocer tus gustos.</span></p><p><span style=\" color:#ebebeb;\"><br/></span></p></body></html>"))
import Source_image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
