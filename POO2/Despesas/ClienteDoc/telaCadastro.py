# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastro(object):
    """
    Classe para configurar a interface gráfica da tela de cadastro.

    ...

    Attributes
    ----------
    centralwidget : QtWidgets.QWidget
        Widget central da janela.

    labelCadastro : QtWidgets.QLabel
        Rótulo da tela de cadastro.

    labelNome : QtWidgets.QLabel
        Rótulo do campo de nome.

    labelNome_2 : QtWidgets.QLabel
        Rótulo do campo de CPF.

    labelNome_3 : QtWidgets.QLabel
        Rótulo do campo de usuário.

    labelNome_4 : QtWidgets.QLabel
        Rótulo do campo de senha.

    btnCadastrar : QtWidgets.QPushButton
        Botão para cadastrar.

    btnVoltar : QtWidgets.QPushButton
        Botão para voltar à tela anterior.

    lineEditCPF : QtWidgets.QLineEdit
        Campo de edição para inserir o CPF.

    lineEditUser : QtWidgets.QLineEdit
        Campo de edição para inserir o usuário.

    lineEditSenha : QtWidgets.QLineEdit
        Campo de edição para inserir a senha.

    lineEditNome : QtWidgets.QLineEdit
        Campo de edição para inserir o nome.

    Methods
    -------
    setupUi(self, TelaCadastro)
        Configura a interface gráfica da tela de cadastro.

    retranslateUi(self, TelaCadastro)
        Traduz os textos exibidos na interface gráfica.
    """
    def setupUi(self, TelaCadastro):
        """
        Configura a interface gráfica da tela de cadastro.

        Parameters
        ----------
        TelaCadastro : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        TelaCadastro.setObjectName("TelaCadastro")
        TelaCadastro.resize(1405, 855)
        self.centralwidget = QtWidgets.QWidget(TelaCadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCadastro = QtWidgets.QLabel(self.centralwidget)
        self.labelCadastro.setGeometry(QtCore.QRect(630, 0, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setObjectName("labelCadastro")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(430, 140, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelNome_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_2.setGeometry(QtCore.QRect(430, 350, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_2.setFont(font)
        self.labelNome_2.setObjectName("labelNome_2")
        self.labelNome_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_3.setGeometry(QtCore.QRect(430, 240, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_3.setFont(font)
        self.labelNome_3.setObjectName("labelNome_3")
        self.labelNome_4 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_4.setGeometry(QtCore.QRect(430, 450, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_4.setFont(font)
        self.labelNome_4.setObjectName("labelNome_4")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(610, 560, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(360, 560, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        self.lineEditCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCPF.setGeometry(QtCore.QRect(570, 330, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditCPF.setFont(font)
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.lineEditUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUser.setGeometry(QtCore.QRect(570, 230, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditUser.setFont(font)
        self.lineEditUser.setText("")
        self.lineEditUser.setObjectName("lineEditUser")
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setGeometry(QtCore.QRect(570, 430, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditSenha.setFont(font)
        self.lineEditSenha.setObjectName("lineEditSenha")
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNome.setGeometry(QtCore.QRect(570, 130, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditNome.setFont(font)
        self.lineEditNome.setText("")
        self.lineEditNome.setObjectName("lineEditNome")
        TelaCadastro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaCadastro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 22))
        self.menubar.setObjectName("menubar")
        TelaCadastro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaCadastro)
        self.statusbar.setObjectName("statusbar")
        TelaCadastro.setStatusBar(self.statusbar)

        self.retranslateUi(TelaCadastro)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastro)

    def retranslateUi(self, TelaCadastro):
        """
        Traduz os textos exibidos na interface gráfica.

        Parameters
        ----------
        TelaCadastro : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        TelaCadastro.setWindowTitle(_translate("TelaCadastro", "MainWindow"))
        self.labelCadastro.setText(_translate("TelaCadastro", "Cadastro"))
        self.labelNome.setText(_translate("TelaCadastro", "Nome:"))
        self.labelNome_2.setText(_translate("TelaCadastro", "CPF:"))
        self.labelNome_3.setText(_translate("TelaCadastro", "Usuário:"))
        self.labelNome_4.setText(_translate("TelaCadastro", "Senha:"))
        self.btnCadastrar.setText(_translate("TelaCadastro", "Cadastrar"))
        self.btnVoltar.setText(_translate("TelaCadastro", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCadastro = QtWidgets.QMainWindow()
    ui = TelaCadastro()
    ui.setupUi(TelaCadastro)
    TelaCadastro.show()
    sys.exit(app.exec_())
