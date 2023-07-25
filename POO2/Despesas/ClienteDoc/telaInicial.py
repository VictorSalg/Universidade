# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaInicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaInicial(object):
    def setupUi(self, TelaInicial):
        """
        Configura a interface gráfica da tela inicial.

        Parameters
        ----------
        TelaInicial : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        TelaInicial.setObjectName("TelaInicial")
        TelaInicial.resize(1419, 881)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaInicial.sizePolicy().hasHeightForWidth())
        TelaInicial.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(TelaInicial)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(610, 510, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(610, 630, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 10, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUser.setGeometry(QtCore.QRect(550, 210, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditUser.setFont(font)
        self.lineEditUser.setText("")
        self.lineEditUser.setObjectName("lineEditUser")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(550, 120, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelNome_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_2.setGeometry(QtCore.QRect(550, 290, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_2.setFont(font)
        self.labelNome_2.setObjectName("labelNome_2")
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setGeometry(QtCore.QRect(550, 380, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditSenha.setFont(font)
        self.lineEditSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSenha.setObjectName("lineEditSenha")
        TelaInicial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaInicial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1419, 22))
        self.menubar.setObjectName("menubar")
        TelaInicial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaInicial)
        self.statusbar.setObjectName("statusbar")
        TelaInicial.setStatusBar(self.statusbar)

        self.retranslateUi(TelaInicial)
        QtCore.QMetaObject.connectSlotsByName(TelaInicial)

    def retranslateUi(self, TelaInicial):
        """
        Traduz os textos exibidos na interface gráfica.

        Parameters
        ----------
        TelaInicial : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        TelaInicial.setWindowTitle(_translate("TelaInicial", "MainWindow"))
        self.btnLogin.setText(_translate("TelaInicial", "Login"))
        self.btnCadastrar.setText(_translate("TelaInicial", "Cadastrar"))
        self.label.setText(_translate("TelaInicial", "Controle de despesas"))
        self.labelNome.setText(_translate("TelaInicial", "Usuário:"))
        self.labelNome_2.setText(_translate("TelaInicial", "Senha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaInicial = QtWidgets.QMainWindow()
    ui = TelaInicial()
    ui.setupUi(TelaInicial)
    TelaInicial.show()
    sys.exit(app.exec_())
