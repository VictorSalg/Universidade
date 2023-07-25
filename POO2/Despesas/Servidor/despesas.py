import mysql.connector as mysql
import threading
import datetime

class Despesas():
    def __init__(self):
        self.conexao = mysql.connect(host = 'localhost', db = 'usur', user = 'root', passwd = 'Salgueiros3016',autocommit=True)
        sql = ('''CREATE TABLE IF NOT EXISTS usuarios(
                        id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                        nome TEXT NOT NULL,
                        cpf VARCHAR(11) NOT NULL,
                        usuario VARCHAR(12) NOT NULL,
                        senha VARCHAR(200) NOT NULL)''')
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        self.cursor.execute(sql)
        sql1 = ('''CREATE TABLE IF NOT EXISTS despesas(
                        id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                        nome TEXT NOT NULL,
                        data DATE NOT NULL,
                        quantia FLOAT NOT NULL,
                        categoria VARCHAR(12) NOT NULL,
                        usuario_id INT NOT NULL,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')     
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        self.cursor.execute(sql1)
        sql2 = ('''CREATE TABLE IF NOT EXISTS receita(
                        id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                        data DATE NOT NULL,
                        receita FLOAT NOT NULL,
                        usuario_id INT NOT NULL,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')     
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        self.cursor.execute(sql2)
        
    def add_conta(self,nome, cpf, usuario, senha):
        if " " in usuario:
            return False, "O nome de usuário não pode conter espaços."
        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                query = f'INSERT INTO usuarios(nome,cpf, usuario, senha) VALUES ("{nome}", "{cpf}","{usuario}", MD5("{senha}"))'
                self.sinc.acquire()
                self.cursor.execute(query)
                self.sinc.release()
                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'Usuario já esta cadastrado.'
        else:
            return False, 'CPF já esta cadastrado.'
        
    def cad_desp(self, usuario_id, nome, data, quantia, categoria):
        query = f'INSERT INTO despesas(usuario_id, nome, data, quantia, categoria) VALUES ("{usuario_id}", "{nome}","{data}","{quantia}","{categoria}")'
        self.sinc.acquire()
        self.cursor.execute(query)
        self.sinc.release()
        return True, 'Despesa cadastrada com sucesso.'
    
    def login(self, usuario, senha):
        flag = self.obterIdUsuario(usuario)
        if flag:
            resultado2 = self.verificarUsuario(usuario, senha, False)
            self.cursor.execute(f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            resultado3 = self.cursor.fetchone()
            if resultado2 and resultado3:
                self.usuario_id = self.obterIdUsuario(usuario)
                return True, self.usuario_id
        return False, " Usuário Senha ou Usuário incorretos."
        
    def obterIdUsuario(self, nome_usuario):
        self.cursor.execute(f'SELECT id FROM usuarios WHERE usuario = "{nome_usuario}"')
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    def obterIdUsuario2(self, nome_usuario):
        self.cursor.execute(f'SELECT id FROM usuarios WHERE usuario = "{nome_usuario}"')
        result = self.cursor.fetchone()
        if result:
            return 'True', result[0]
        else:
            return 'False', 'Usuário não encontrado.'
            
    def verificarCPF(self, cpf):
        self.cursor.execute(f'SELECT cpf FROM usuarios WHERE cpf = "{cpf}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        return False
    
    def verificarUsuario(self, usuario, senha = None, UserPassword = True):
        if UserPassword:
            self.cursor.execute(f'SELECT usuario FROM usuarios WHERE usuario = "{usuario}"')
            exists = self.cursor.fetchall()
            if exists:
                return True  
            return False
        else:
            self.cursor.execute(f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            exists = self.cursor.fetchone()
            if exists:
                return True
            return False
        '''else:
            self.cursor.execute(f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            if self.cursor.fetchall():
                return True, 'Existe.'
            return False, 'Usuário ou senha não encontrado.' '''
        
    def inserir(self, usuario_id, data, valor):
        valor = float(valor)
        if valor <= 0:
            return False, "Não foi possível adicionar o valor."
        else:
            query = f'INSERT INTO receita(usuario_id, data, receita) VALUES ("{usuario_id}","{data}", "{valor}")'
            self.sinc.acquire()
            self.cursor.execute(query)
            self.sinc.release()
            return True, 'Receita cadastrada com sucesso.'

    def mostrar_despesas(self, usuario_id, mes, ano):
        query = f'''
            SELECT nome, data, quantia, categoria
            FROM despesas
            WHERE usuario_id = {usuario_id}
            AND MONTH(data) = {int(mes):02d}
            AND YEAR(data) = {ano}
        '''
        self.sinc.acquire()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.sinc.release()
        return result

    def mostrar_receita(self, usuario_id, mes, ano):
        query = f'''
            SELECT receita, data
            FROM receita
            WHERE usuario_id = {usuario_id}
            AND MONTH(data) = {int(mes):02d}
            AND YEAR(data) = {ano}
        '''
        self.sinc.acquire()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.sinc.release()
        return result
    
    def saldo(self, usuario_id, mes, ano):
        query_receita = f'SELECT SUM(receita) FROM receita WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'
        query_despesas = f'SELECT SUM(quantia) FROM despesas WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'

        self.sinc.acquire()
        self.cursor.execute(query_receita)
        receita = self.cursor.fetchone()[0] or 0

        self.cursor.execute(query_despesas)
        despesas = self.cursor.fetchone()[0] or 0

        self.sinc.release()

        saldo = receita - despesas
        return saldo
    
    def receita(self, usuario_id, mes, ano):
        query_receita = f'SELECT SUM(receita) FROM receita WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'
        self.sinc.acquire()
        self.cursor.execute(query_receita)
        receita = self.cursor.fetchone()[0] or 0
        self.sinc.release()
        return receita
    
    def despesas(self, usuario_id, mes, ano):
        query_despesas = f'SELECT SUM(quantia) FROM despesas WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'
        self.sinc.acquire() 
        self.cursor.execute(query_despesas)
        despesas = self.cursor.fetchone()[0] or 0
        self.sinc.release()
        return despesas