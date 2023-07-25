# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaSaldo.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaSaldo(object):
    def setupUi(self, TelaSaldo):
        """
        Configura a interface gráfica da tela de verificação de saldo.

        Parameters
        ----------
        TelaSaldo : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        TelaSaldo.setObjectName("TelaSaldo")
        TelaSaldo.resize(1405, 855)
        self.centralwidget = QtWidgets.QWidget(TelaSaldo)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCadastro = QtWidgets.QLabel(self.centralwidget)
        self.labelCadastro.setGeometry(QtCore.QRect(570, 0, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setObjectName("labelCadastro")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setGeometry(QtCore.QRect(820, 240, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelNome_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_2.setGeometry(QtCore.QRect(820, 420, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_2.setFont(font)
        self.labelNome_2.setObjectName("labelNome_2")
        self.labelNome_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelNome_3.setGeometry(QtCore.QRect(820, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome_3.setFont(font)
        self.labelNome_3.setObjectName("labelNome_3")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(780, 540, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(450, 540, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        self.lineEditSaldo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSaldo.setGeometry(QtCore.QRect(970, 410, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditSaldo.setFont(font)
        self.lineEditSaldo.setReadOnly(True)
        self.lineEditSaldo.setObjectName("lineEditSaldo")
        self.lineEditDespesas = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDespesas.setGeometry(QtCore.QRect(970, 330, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditDespesas.setFont(font)
        self.lineEditDespesas.setText("")
        self.lineEditDespesas.setReadOnly(True)
        self.lineEditDespesas.setObjectName("lineEditDespesas")
        self.lineEditReceita = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditReceita.setGeometry(QtCore.QRect(970, 240, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEditReceita.setFont(font)
        self.lineEditReceita.setText("")
        self.lineEditReceita.setReadOnly(True)
        self.lineEditReceita.setObjectName("lineEditReceita")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(430, 110, 231, 391))
        self.tableView.setObjectName("tableView")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(800, 110, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dateEdit.setFont(font)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        TelaSaldo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaSaldo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 22))
        self.menubar.setObjectName("menubar")
        TelaSaldo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaSaldo)
        self.statusbar.setObjectName("statusbar")
        TelaSaldo.setStatusBar(self.statusbar)

        self.retranslateUi(TelaSaldo)
        QtCore.QMetaObject.connectSlotsByName(TelaSaldo)

    def retranslateUi(self, TelaSaldo):
        """
        Traduz os textos exibidos na interface gráfica.

        Parameters
        ----------
        TelaSaldo : QtWidgets.QMainWindow
            A referência para a janela principal.
        """
        _translate = QtCore.QCoreApplication.translate
        TelaSaldo.setWindowTitle(_translate("TelaSaldo", "MainWindow"))
        self.labelCadastro.setText(_translate("TelaSaldo", "Verificar saldo"))
        self.labelNome.setText(_translate("TelaSaldo", "Receita:"))
        self.labelNome_2.setText(_translate("TelaSaldo", "Saldo:"))
        self.labelNome_3.setText(_translate("TelaSaldo", "Despesas:"))
        self.btnBuscar.setText(_translate("TelaSaldo", "Buscar"))
        self.btnVoltar.setText(_translate("TelaSaldo", "Voltar"))
        self.dateEdit.setDisplayFormat(_translate("TelaSaldo", "MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaSaldo = QtWidgets.QMainWindow()
    ui = TelaSaldo()
    ui.setupUi(TelaSaldo)
    TelaSaldo.show()
    sys.exit(app.exec_())
