# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastrarDespesas.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastrarDespesas(object):
    def setupUi(self, TelaCadastrarDespesas):
        TelaCadastrarDespesas.setObjectName("TelaCadastrarDespesas")
        TelaCadastrarDespesas.resize(1422, 883)
        self.centralwidget = QtWidgets.QWidget(TelaCadastrarDespesas)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(300, 580, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        self.labelCadastro = QtWidgets.QLabel(self.centralwidget)
        self.labelCadastro.setGeometry(QtCore.QRect(540, 40, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setObjectName("labelCadastro")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(610, 580, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(570, 250, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(330, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelData = QtWidgets.QLabel(self.centralwidget)
        self.labelData.setGeometry(QtCore.QRect(330, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelData.setFont(font)
        self.labelData.setObjectName("labelData")
        self.labelQuantia = QtWidgets.QLabel(self.centralwidget)
        self.labelQuantia.setGeometry(QtCore.QRect(330, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuantia.setFont(font)
        self.labelQuantia.setObjectName("labelQuantia")
        self.labelCategoria = QtWidgets.QLabel(self.centralwidget)
        self.labelCategoria.setGeometry(QtCore.QRect(330, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelCategoria.setFont(font)
        self.labelCategoria.setObjectName("labelCategoria")
        self.lineEditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNome.setGeometry(QtCore.QRect(570, 140, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditNome.setFont(font)
        self.lineEditNome.setText("")
        self.lineEditNome.setObjectName("lineEditNome")
        self.lineEditQuantia = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQuantia.setGeometry(QtCore.QRect(570, 360, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditQuantia.setFont(font)
        self.lineEditQuantia.setObjectName("lineEditQuantia")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 470, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        TelaCadastrarDespesas.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaCadastrarDespesas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1422, 22))
        self.menubar.setObjectName("menubar")
        TelaCadastrarDespesas.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaCadastrarDespesas)
        self.statusbar.setObjectName("statusbar")
        TelaCadastrarDespesas.setStatusBar(self.statusbar)

        self.retranslateUi(TelaCadastrarDespesas)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastrarDespesas)

    def retranslateUi(self, TelaCadastrarDespesas):
        _translate = QtCore.QCoreApplication.translate
        TelaCadastrarDespesas.setWindowTitle(_translate("TelaCadastrarDespesas", "MainWindow"))
        self.btnVoltar.setText(_translate("TelaCadastrarDespesas", "Voltar"))
        self.labelCadastro.setText(_translate("TelaCadastrarDespesas", "Cadastrar despesas"))
        self.btnCadastrar.setText(_translate("TelaCadastrarDespesas", "Cadastrar"))
        self.labelNome.setText(_translate("TelaCadastrarDespesas", "Nome/Descrição:"))
        self.labelData.setText(_translate("TelaCadastrarDespesas", "Data:"))
        self.labelQuantia.setText(_translate("TelaCadastrarDespesas", "Quantia:"))
        self.labelCategoria.setText(_translate("TelaCadastrarDespesas", "Categoria:"))
        self.comboBox.setItemText(1, _translate("TelaCadastrarDespesas", "Lazer"))
        self.comboBox.setItemText(2, _translate("TelaCadastrarDespesas", "Viagem"))
        self.comboBox.setItemText(3, _translate("TelaCadastrarDespesas", "Mercado"))
        self.comboBox.setItemText(4, _translate("TelaCadastrarDespesas", "Moradia"))
        self.comboBox.setItemText(5, _translate("TelaCadastrarDespesas", "Trabalho"))
        self.comboBox.setItemText(6, _translate("TelaCadastrarDespesas", "Outro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCadastrarDespesas = QtWidgets.QMainWindow()
    ui = TelaCadastrarDespesas()
    ui.setupUi(TelaCadastrarDespesas)
    TelaCadastrarDespesas.show()
    sys.exit(app.exec_())
