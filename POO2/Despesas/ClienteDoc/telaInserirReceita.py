# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaInserirReceita.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaInserirReceita(object):
    """
    Classe para configurar a interface gráfica da tela de inserção de receita.

    ...

    Attributes
    ----------
    centralwidget : QtWidgets.QWidget
        Widget central da janela.

    btnVoltar : QtWidgets.QPushButton
        Botão para voltar à tela anterior.

    btnInserir : QtWidgets.QPushButton
        Botão para inserir a receita.

    labelQuantia : QtWidgets.QLabel
        Rótulo para o campo de edição da quantia da receita.

    lineEditQuantia : QtWidgets.QLineEdit
        Campo de edição para inserir a quantia da receita.

    labelCadastro : QtWidgets.QLabel
        Rótulo da tela de inserção de receita.

    labelData : QtWidgets.QLabel
        Rótulo para o campo de edição da data da receita.

    dateEdit : QtWidgets.QDateEdit
        Campo de edição para inserir a data da receita.

    Methods
    -------
    setupUi(self, TelaInserirReceita)
        Configura a interface gráfica da tela de inserção de receita.

    retranslateUi(self, TelaInserirReceita)
        Traduz os textos exibidos na interface gráfica.
    """
    def setupUi(self, TelaInserirReceita):
        """
        Configura a interface gráfica da tela de inserção de receita.

        Parameters
        ----------
        TelaInserirReceita : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        TelaInserirReceita.setObjectName("TelaInserirReceita")
        TelaInserirReceita.resize(1417, 880)
        self.centralwidget = QtWidgets.QWidget(TelaInserirReceita)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(590, 520, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        self.btnInserir = QtWidgets.QPushButton(self.centralwidget)
        self.btnInserir.setGeometry(QtCore.QRect(590, 430, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnInserir.setFont(font)
        self.btnInserir.setObjectName("btnInserir")
        self.labelQuantia = QtWidgets.QLabel(self.centralwidget)
        self.labelQuantia.setGeometry(QtCore.QRect(400, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuantia.setFont(font)
        self.labelQuantia.setObjectName("labelQuantia")
        self.lineEditQuantia = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQuantia.setGeometry(QtCore.QRect(550, 210, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditQuantia.setFont(font)
        self.lineEditQuantia.setText("")
        self.lineEditQuantia.setObjectName("lineEditQuantia")
        self.labelCadastro = QtWidgets.QLabel(self.centralwidget)
        self.labelCadastro.setGeometry(QtCore.QRect(580, 100, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setObjectName("labelCadastro")
        self.labelData = QtWidgets.QLabel(self.centralwidget)
        self.labelData.setGeometry(QtCore.QRect(400, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelData.setFont(font)
        self.labelData.setObjectName("labelData")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(550, 310, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        TelaInserirReceita.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaInserirReceita)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1417, 22))
        self.menubar.setObjectName("menubar")
        TelaInserirReceita.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaInserirReceita)
        self.statusbar.setObjectName("statusbar")
        TelaInserirReceita.setStatusBar(self.statusbar)

        self.retranslateUi(TelaInserirReceita)
        QtCore.QMetaObject.connectSlotsByName(TelaInserirReceita)

    def retranslateUi(self, TelaInserirReceita):
        """
        Traduz os textos exibidos na interface gráfica.

        Parameters
        ----------
        TelaInserirReceita : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        TelaInserirReceita.setWindowTitle(_translate("TelaInserirReceita", "MainWindow"))
        self.btnVoltar.setText(_translate("TelaInserirReceita", "Voltar"))
        self.btnInserir.setText(_translate("TelaInserirReceita", "Inserir"))
        self.labelQuantia.setText(_translate("TelaInserirReceita", "Quantia:"))
        self.labelCadastro.setText(_translate("TelaInserirReceita", "Inserir receita"))
        self.labelData.setText(_translate("TelaInserirReceita", "Data:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaInserirReceita = QtWidgets.QMainWindow()
    ui = TelaInserirReceita()
    ui.setupUi(TelaInserirReceita)
    TelaInserirReceita.show()
    sys.exit(app.exec_())
