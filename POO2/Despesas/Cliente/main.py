from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import datetime
import sys
from cliente import *

from telaInicial import TelaInicial
from telaCadastro import TelaCadastro
from telaMenu import TelaMenu
from telaCadastrarDespesas import TelaCadastrarDespesas
from telaInserirReceita import TelaInserirReceita
from telaDespesasMes import TelaDespesasMes
from telaSaldo import TelaSaldo

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(664, 382)
        
        self.server = cliente()


        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.telaInicial = TelaInicial()
        self.telaInicial.setupUi(self.stack0)

        self.telaMenu = TelaMenu()
        self.telaMenu.setupUi(self.stack1)

        self.telaCadastro = TelaCadastro()
        self.telaCadastro.setupUi(self.stack2)
        
        self.telaCadastrarDespesas = TelaCadastrarDespesas()
        self.telaCadastrarDespesas.setupUi(self.stack3)

        self.telaInserirReceita = TelaInserirReceita()
        self.telaInserirReceita.setupUi(self.stack4)

        self.telaDespesasMes = TelaDespesasMes()
        self.telaDespesasMes.setupUi(self.stack5)

        self.telaSaldo = TelaSaldo()
        self.telaSaldo.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        self.usuario_id = None

        self.telaInicial.btnCadastrar.clicked.connect(self.abrirCadastro)
        self.telaInicial.btnLogin.clicked.connect(self.BotaoLogin)

        self.telaCadastro.btnCadastrar.clicked.connect(self.BotaoCadastrar)
        self.telaCadastro.btnVoltar.clicked.connect(self.BotaoVoltarTelaInicial)

        self.telaMenu.btnCadastrarDesp.clicked.connect(self.abrirCadastrarDesp)
        self.telaMenu.btnInserirReceita.clicked.connect(self.abrirInserirReceita)
        self.telaMenu.btnVerificarMes.clicked.connect(self.abrirVerificarMes)
        self.telaMenu.btnVerificarSaldo.clicked.connect(self.abrirVerificarSaldo)
        self.telaMenu.btnSair.clicked.connect(self.sair)
        self.telaMenu.btnVoltar.clicked.connect(self.BotaoVoltarTelaInicial)

        self.telaCadastrarDespesas.btnVoltar.clicked.connect(self.BotaoVoltarTelaMenu)
        self.telaCadastrarDespesas.btnCadastrar.clicked.connect(self.cadastrarDespesa)

        self.telaInserirReceita.btnVoltar.clicked.connect(self.BotaoVoltarTelaMenu)
        self.telaInserirReceita.btnInserir.clicked.connect(self.inserirReceita)

        self.telaDespesasMes.btnVoltar.clicked.connect(self.BotaoVoltarTelaMenu)
        self.telaDespesasMes.btnBuscar.clicked.connect(self.BotaoBuscarDesp)

        self.telaSaldo.btnBuscar.clicked.connect(self.BotaoBuscarSaldo)
        self.telaSaldo.btnVoltar.clicked.connect(self.BotaoVoltarTelaMenu)


    def sair(self):
        self.request_server('sair')
        sys.exit()

    def BotaoVoltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def BotaoVoltarTelaMenu(self):
        solicit = f'login*{self.user}*{self.passw}'
        flag = self.request_server(solicit)
        if flag[0]:
            self.QtStack.setCurrentIndex(1)
            empty_model = PandasModel(pd.DataFrame())
            self.telaDespesasMes.tableView.setModel(empty_model)
            self.telaSaldo.tableView.setModel(empty_model)

        
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(2)

    def abrirCadastrarDesp(self):
        self.telaCadastrarDespesas.lineEditNome.setText("")
        self.telaCadastrarDespesas.dateEdit.setDate(QtCore.QDate.currentDate())
        self.telaCadastrarDespesas.lineEditQuantia.setText("")
        self.telaCadastrarDespesas.comboBox.setCurrentIndex(0)
        self.QtStack.setCurrentIndex(3)

    def abrirInserirReceita(self):
        self.telaInserirReceita.dateEdit.setDate(QtCore.QDate.currentDate())
        self.telaInserirReceita.lineEditQuantia.setText("")
        self.QtStack.setCurrentIndex(4)

    def abrirVerificarMes(self):
        self.telaDespesasMes.dateEdit.setDate(QtCore.QDate.currentDate())
        self.QtStack.setCurrentIndex(5)

    def abrirVerificarSaldo(self):
        self.telaSaldo.dateEdit.setDate(QtCore.QDate.currentDate())
        self.telaSaldo.lineEditSaldo.setText("")
        self.telaSaldo.lineEditReceita.setText("")
        self.telaSaldo.lineEditDespesas.setText("")
        self.QtStack.setCurrentIndex(6)

    def request_server(self, request):
        self.server.send(request.encode())
        recv = self.server.recv(2048)
        flag = recv.decode()
        flag = flag.replace("(", "").replace("datetime.date", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
        '''try:
            print(flag[0])
            print(flag[1])
            print(flag[2])
            print(flag[3])
            print(flag[4])
            print(flag[5])
        except:
            print('Não sei')'''
        return flag
    
    def concatenar(self, string):
        noti = ''
        for i in range(1,len(string)):
            noti += string[i] + " "
        return noti
    
    def BotaoCadastrar(self):
        nome = self.telaCadastro.lineEditNome.text()
        cpf = (self.telaCadastro.lineEditCPF.text())
        usuario = self.telaCadastro.lineEditUser.text()
        senha = self.telaCadastro.lineEditSenha.text()
        if nome != '' and cpf != '' and usuario != '' and senha != '':
            if cpf.isdigit() and len(cpf) == 11:
                solicit = f'add_conta*{nome}*{cpf}*{usuario}*{senha}'
                flag = self.request_server(solicit)
                noti = self.concatenar(flag)
                self.request_server(solicit)
                self.telaCadastro.lineEditNome.setText("")
                self.telaCadastro.lineEditCPF.setText("")
                self.telaCadastro.lineEditUser.setText("")
                self.telaCadastro.lineEditSenha.setText("")
                QMessageBox.information(None, 'Cadastro', noti)
            else:
                QMessageBox.information(None, 'Cadastro', 'O CPF não existe')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os dados devem estar preenchidos!')

    def BotaoLogin(self):
        usuario = self.telaInicial.lineEditUser.text()
        senha = self.telaInicial.lineEditSenha.text()
        if usuario != '' and senha != '':
            resul = f'login*{usuario}*{senha}'
            flag = self.request_server(resul)
            if flag[0] == 'True':
                obter_id_request = f'obterIdUsuario2*{usuario}'
                response = self.request_server(obter_id_request)
                if response[0] == 'True':
                    self.usuario_id = int(response[1])
                    self.user = usuario
                    self.passw = senha
                    self.QtStack.setCurrentIndex(1)
                else:
                    noti = self.concatenar(response[1:])
                    QMessageBox.information(None, 'Login', noti)
            else:
                noti = self.concatenar(flag[1:])
                QMessageBox.information(None, 'Login', noti)
        else:
            QMessageBox.information(None, 'Login', 'Todos os dados devem ser preenchidos.')
        self.telaInicial.lineEditUser.setText("")
        self.telaInicial.lineEditSenha.setText("")


    def cadastrarDespesa(self):
        nome = self.telaCadastrarDespesas.lineEditNome.text()
        data = self.telaCadastrarDespesas.dateEdit.date().toString('yyyy-MM-dd')
        quantia_str = self.telaCadastrarDespesas.lineEditQuantia.text()
        categoria = self.telaCadastrarDespesas.comboBox.currentText()
        nome = nome.replace(' ', '_')
        if nome and data and quantia_str and categoria:
            try:
                quantia = float(quantia_str)
                if self.usuario_id is not None:
                    usuario_id = self.usuario_id
                    solicit = f'cad_desp*{usuario_id}*{nome}*{data}*{quantia}*{categoria}'
                    flag = self.request_server(solicit)
                    noti = self.concatenar(flag)
                    self.telaCadastrarDespesas.lineEditNome.setText("")
                    self.telaCadastrarDespesas.dateEdit.setDate(QtCore.QDate.currentDate())
                    self.telaCadastrarDespesas.lineEditQuantia.setText("")
                    self.telaCadastrarDespesas.comboBox.setCurrentIndex(0)
                    QMessageBox.information(None, 'Cadastro de Despesa', noti)
                else:
                    QMessageBox.warning(None, 'Cadastro de Despesa', 'Usuário não encontrado.')
            except ValueError:
                QMessageBox.warning(None, 'Cadastro de Despesa', 'A quantia deve ser um valor numérico válido.')
        else:
            QMessageBox.warning(None, 'Cadastro de Despesa', 'Todos os campos devem estar preenchidos.')

    def inserirReceita(self):
        quantia_str = self.telaInserirReceita.lineEditQuantia.text()
        data = self.telaInserirReceita.dateEdit.date().toString('yyyy-MM-dd')
        if quantia_str and data:
            try:
                quantia = float(quantia_str)
                if self.usuario_id is not None:
                    usuario_id = self.usuario_id
                    solicit = f'inserir*{usuario_id}*{data}*{quantia}'
                    flag = self.request_server(solicit)
                    noti = self.concatenar(flag)
                    self.telaInserirReceita.lineEditQuantia.setText("")
                    self.telaInserirReceita.dateEdit.setDate(QtCore.QDate.currentDate())
                    QMessageBox.information(None, 'Receita', noti)
                else:
                    QMessageBox.warning(None, 'Receita', 'Usuário não encontrado.')
            except ValueError:
                QMessageBox.warning(None, 'Receita', 'A quantia deve ser um valor numérico válido.')
        else:
            QMessageBox.warning(None, 'Receita', 'A receita deve ser colocada.')

    def BotaoBuscarDesp(self):
        selected_date = self.telaDespesasMes.dateEdit.date()
        month = selected_date.month()
        year = selected_date.year()

        if self.usuario_id is not None:
            usuario_id = self.usuario_id
            solicit = f'mostrar_despesas*{usuario_id}*{month}*{year}'
            flag = self.request_server(solicit)
            print(flag)
            try:
                if flag[0]:
                    expense_data = []
                    for i in range(0, len(flag[1:]), 6):
                        nome = flag[i]
                        ano = int(flag[i + 1])
                        mes = int(flag[i + 2])
                        dia = int(flag[i + 3])
                        valor = float(flag[i + 4])
                        categoria = flag[i + 5]
                        data = datetime.date(ano, mes, dia)
                        expense_data.append([nome, data, valor, categoria])

                        columns = ["Nome", "Data", "Quantia", "Categoria"]
                        df = pd.DataFrame(expense_data, columns=columns)
                        model = PandasModel(df)
                        self.telaDespesasMes.tableView.setModel(model)
                else:
                    noti = self.concatenar(flag[1:])
                    QMessageBox.information(None, 'Buscar Despesas', noti)
            except:
                empty_model = PandasModel(pd.DataFrame())
                self.telaDespesasMes.tableView.setModel(empty_model)
                QMessageBox.information(None, 'Despesas', 'Nenhuma despesa deste mês.')

    def BotaoBuscarSaldo(self):
        selected_date = self.telaSaldo.dateEdit.date()
        mes = selected_date.month()
        ano = selected_date.year()
        if self.usuario_id is not None:
            usuario_id = self.usuario_id
            solicit = f'receita*{usuario_id}*{mes}*{ano}'
            flag = self.request_server(solicit)
            solicit2 = f'despesas*{usuario_id}*{mes}*{ano}'
            flag2 = self.request_server(solicit2)
            solicit3 = f'saldo*{usuario_id}*{mes}*{ano}'
            flag3 = self.request_server(solicit3)
            if flag[0] and flag2[0] and flag3[0]:
                self.telaSaldo.lineEditReceita.setText(str(flag[0]))
                self.telaSaldo.lineEditDespesas.setText(str(flag2[0]))
                self.telaSaldo.lineEditSaldo.setText(str(flag3[0]))
            else:
                noti = self.concatenar(flag[1:])
                QMessageBox.information(None, 'Buscar Saldo', noti)
        if self.usuario_id is not None:
            usuario_id = self.usuario_id
            solicit = f'mostrar_receita*{usuario_id}*{mes}*{ano}'
            flag = self.request_server(solicit)
            print(flag)
            try:
                if flag[0]:
                    expense_data = []
                    for i in range(0, len(flag[1:]), 4):
                        receita = float(flag[i])
                        ano = int(flag[i + 1])
                        mes = int(flag[i + 2])
                        dia = int(flag[i + 3])
                        data = datetime.date(ano, mes, dia)
                        expense_data.append([receita, data])

                        columns = ["Receita", "Data"]
                        df = pd.DataFrame(expense_data, columns=columns)
                        model = PandasModel(df)
                        self.telaSaldo.tableView.setModel(model)
                else:
                    noti = self.concatenar(flag[1:])
                    QMessageBox.information(None, 'Receita', noti)
            except:
                empty_model = PandasModel(pd.DataFrame())
                self.telaSaldo.tableView.setModel(empty_model)
                QMessageBox.information(None, 'Receita', 'Nenhuma receita deste mês.')
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())