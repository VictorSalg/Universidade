# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaDespesasMes.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaDespesasMes(object):
    def setupUi(self, TelaDespesasMes):
        TelaDespesasMes.setObjectName("TelaDespesasMes")
        TelaDespesasMes.resize(1414, 859)
        self.centralwidget = QtWidgets.QWidget(TelaDespesasMes)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(480, 590, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setObjectName("btnVoltar")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(620, 100, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dateEdit.setFont(font)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(440, 180, 531, 391))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 10, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(740, 590, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setObjectName("btnBuscar")
        TelaDespesasMes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaDespesasMes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1414, 22))
        self.menubar.setObjectName("menubar")
        TelaDespesasMes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaDespesasMes)
        self.statusbar.setObjectName("statusbar")
        TelaDespesasMes.setStatusBar(self.statusbar)

        self.retranslateUi(TelaDespesasMes)
        QtCore.QMetaObject.connectSlotsByName(TelaDespesasMes)

    def retranslateUi(self, TelaDespesasMes):
        _translate = QtCore.QCoreApplication.translate
        TelaDespesasMes.setWindowTitle(_translate("TelaDespesasMes", "MainWindow"))
        self.btnVoltar.setText(_translate("TelaDespesasMes", "Voltar"))
        self.dateEdit.setDisplayFormat(_translate("TelaDespesasMes", "MM/yyyy"))
        self.label.setText(_translate("TelaDespesasMes", "Selecione o mês"))
        self.btnBuscar.setText(_translate("TelaDespesasMes", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaDespesasMes = QtWidgets.QMainWindow()
    ui = TelaDespesasMes()
    ui.setupUi(TelaDespesasMes)
    TelaDespesasMes.show()
    sys.exit(app.exec_())
