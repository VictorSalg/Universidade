import mysql.connector as mysql
import threading
import datetime

class Despesas():
    def __init__(self):
        """
        Inicializa a conexão com o banco de dados e cria as tabelas se não existirem.
        """
        self.conexao = mysql.connect(host='localhost', db='usur', user='root', passwd='Salgueiros3016', autocommit=True)
        self.cursor = self.conexao.cursor()
        self.sinc = threading.Lock()
        
        # Cria a tabela de usuários se não existir
        sql_usuarios = '''
            CREATE TABLE IF NOT EXISTS usuarios(
                id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                usuario VARCHAR(12) NOT NULL,
                senha VARCHAR(200) NOT NULL
            )
        '''
        self.cursor.execute(sql_usuarios)
        
        # Cria a tabela de despesas se não existir
        sql_despesas = '''
            CREATE TABLE IF NOT EXISTS despesas(
                id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                data DATE NOT NULL,
                quantia FLOAT NOT NULL,
                categoria VARCHAR(12) NOT NULL,
                usuario_id INT NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        '''
        self.cursor.execute(sql_despesas)
        
        # Cria a tabela de receitas se não existir
        sql_receita = '''
            CREATE TABLE IF NOT EXISTS receita(
                id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
                data DATE NOT NULL,
                receita FLOAT NOT NULL,
                usuario_id INT NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        '''
        self.cursor.execute(sql_receita)
        
    def add_conta(self, nome, cpf, usuario, senha):
        """
        Adiciona uma nova conta de usuário ao banco de dados.

        Parameters
        ----------
        nome : str
            O nome do usuário.
        cpf : str
            O CPF do usuário.
        usuario : str
            O nome de usuário.
        senha : str
            A senha do usuário.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano indicando se o cadastro foi realizado com sucesso e uma mensagem de retorno.
        """
        if " " in usuario:
            return False, "O nome de usuário não pode conter espaços."
        
        if not self.verificarCPF(cpf):
            if not self.verificarUsuario(usuario):
                query = f'INSERT INTO usuarios(nome, cpf, usuario, senha) VALUES ("{nome}", "{cpf}","{usuario}", MD5("{senha}"))'
                self.sinc.acquire()
                self.cursor.execute(query)
                self.sinc.release()
                return True, "Cadastro realizado com sucesso."
            else:
                return False, 'Usuário já está cadastrado.'
        else:
            return False, 'CPF já está cadastrado.'
    
    def cad_desp(self, usuario_id, nome, data, quantia, categoria):
        """
        Registra uma nova despesa no banco de dados.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        nome : str
            O nome da despesa.
        data : str
            A data da despesa no formato 'YYYY-MM-DD'.
        quantia : float
            A quantia da despesa.
        categoria : str
            A categoria da despesa.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano indicando se a despesa foi cadastrada com sucesso e uma mensagem de retorno.
        """
        query = f'INSERT INTO despesas(usuario_id, nome, data, quantia, categoria) VALUES ("{usuario_id}", "{nome}", "{data}", "{quantia}", "{categoria}")'
        self.sinc.acquire()
        self.cursor.execute(query)
        self.sinc.release()
        return True, 'Despesa cadastrada com sucesso.'
    
    def login(self, usuario, senha):
        """
        Realiza o login de um usuário no sistema.

        Parameters
        ----------
        usuario : str
            O nome de usuário.
        senha : str
            A senha do usuário.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano indicando se o login foi realizado com sucesso e uma mensagem de retorno.
        """
        flag = self.obterIdUsuario(usuario)
        
        if flag:
            resultado2 = self.verificarUsuario(usuario, senha, False)
            self.cursor.execute(f'SELECT usuario, senha FROM usuarios WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
            resultado3 = self.cursor.fetchone()
            
            if resultado2 and resultado3:
                self.usuario_id = self.obterIdUsuario(usuario)
                return True, self.usuario_id
        
        return False, "Usuário ou senha incorretos."
    
    def obterIdUsuario(self, nome_usuario):
        """
        Obtém o ID de um usuário com base no nome de usuário.

        Parameters
        ----------
        nome_usuario : str
            O nome de usuário.

        Returns
        -------
        int or None
            O ID do usuário se encontrado, ou None caso contrário.
        """
        self.cursor.execute(f'SELECT id FROM usuarios WHERE usuario = "{nome_usuario}"')
        result = self.cursor.fetchone()
        
        if result:
            return result[0]
        else:
            return None
    
    def obterIdUsuario2(self, nome_usuario):
        """
        Obtém o ID de um usuário com base no nome de usuário.

        Parameters
        ----------
        nome_usuario : str
            O nome de usuário.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano indicando se o usuário foi encontrado e o ID do usuário ou uma mensagem de retorno.
        """
        self.cursor.execute(f'SELECT id FROM usuarios WHERE usuario = "{nome_usuario}"')
        result = self.cursor.fetchone()
        
        if result:
            return 'True', result[0]
        else:
            return 'False', 'Usuário não encontrado.'
    
    def verificarCPF(self, cpf):
        """
        Verifica se um CPF já está cadastrado no banco de dados.

        Parameters
        ----------
        cpf : str
            O CPF a ser verificado.

        Returns
        -------
        bool
            True se o CPF já está cadastrado, False caso contrário.
        """
        self.cursor.execute(f'SELECT cpf FROM usuarios WHERE cpf = "{cpf}"')
        exists = self.cursor.fetchall()
        
        if exists:
            return True
        return False
    
    def verificarUsuario(self, usuario, senha=None, UserPassword=True):
        """
        Verifica se um nome de usuário já está cadastrado no banco de dados.

        Parameters
        ----------
        usuario : str
            O nome de usuário.
        senha : str, optional
            A senha do usuário, por padrão None.
        UserPassword : bool, optional
            Indica se também deve ser verificada a senha do usuário, por padrão True.

        Returns
        -------
        bool
            True se o nome de usuário já está cadastrado (ou se o nome de usuário e senha correspondem), False caso contrário.
        """
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
        
    def inserir(self, usuario_id, data, valor):
        """
        Insere uma nova receita no banco de dados.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        data : str
            A data da receita no formato 'YYYY-MM-DD'.
        valor : float
            O valor da receita.

        Returns
        -------
        tuple
            Uma tupla contendo um valor booleano indicando se a receita foi cadastrada com sucesso e uma mensagem de retorno.
        """
        valor = float(valor)
        
        if valor <= 0:
            return False, "Não foi possível adicionar o valor."
        else:
            query = f'INSERT INTO receita(usuario_id, data, receita) VALUES ("{usuario_id}", "{data}", "{valor}")'
            self.sinc.acquire()
            self.cursor.execute(query)
            self.sinc.release()
            return True, 'Receita cadastrada com sucesso.'
    
    def mostrar_despesas(self, usuario_id, mes, ano):
        """
        Obtém as despesas de um usuário para um determinado mês e ano.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        mes : int
            O número do mês.
        ano : int
            O ano.

        Returns
        -------
        list
            Uma lista contendo as despesas do usuário para o mês e ano especificados.
        """
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
        """
        Obtém as receitas de um usuário para um determinado mês e ano.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        mes : int
            O número do mês.
        ano : int
            O ano.

        Returns
        -------
        list
            Uma lista contendo as receitas do usuário para o mês e ano especificados.
        """
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
        """
        Calcula o saldo de um usuário para um determinado mês e ano.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        mes : int
            O número do mês.
        ano : int
            O ano.

        Returns
        -------
        float
            O saldo do usuário para o mês e ano especificados.
        """
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
        """
        Obtém o total de receitas de um usuário para um determinado mês e ano.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        mes : int
            O número do mês.
        ano : int
            O ano.

        Returns
        -------
        float
            O total de receitas do usuário para o mês e ano especificados.
        """
        query_receita = f'SELECT SUM(receita) FROM receita WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'
        self.sinc.acquire()
        self.cursor.execute(query_receita)
        receita = self.cursor.fetchone()[0] or 0
        self.sinc.release()
        return receita
    
    def despesas(self, usuario_id, mes, ano):
        """
        Obtém o total de despesas de um usuário para um determinado mês e ano.

        Parameters
        ----------
        usuario_id : int
            O ID do usuário.
        mes : int
            O número do mês.
        ano : int
            O ano.

        Returns
        -------
        float
            O total de despesas do usuário para o mês e ano especificados.
        """
        query_despesas = f'SELECT SUM(quantia) FROM despesas WHERE usuario_id = {usuario_id} AND MONTH(data) = {int(mes):02d} AND YEAR(data) = {ano}'
        self.sinc.acquire() 
        self.cursor.execute(query_despesas)
        despesas = self.cursor.fetchone()[0] or 0
        self.sinc.release()
        return despesas
