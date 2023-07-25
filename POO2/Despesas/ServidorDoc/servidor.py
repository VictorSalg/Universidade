import socket
from despesas import Despesas
import threading

class ClienteThread(threading.Thread):
    def __init__(self, clientSock, clientAddress):
        """
        Inicializa a thread do cliente.

        Parameters
        ----------
        clientSock : socket.socket
            O socket do cliente.
        clientAddress : tuple
            O endereço do cliente (IP, porta).
        """
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
        """
        Executa a thread do cliente.
        """
        try:
            while True:
                solicitacao = self.clientSock.recv(2048).decode().split("*")
                metodo = solicitacao.pop(0)
                if metodo == 'sair':
                    self.clientSock.close()
                    break
                despesas = Despesas()
                func = getattr(despesas, metodo)
                retorno = func(*solicitacao)
                self.clientSock.send(f'{retorno}'.encode()) 
        except AttributeError:
            print('Error')

class Servidor():
    def __init__(self):
        """
        Inicializa o servidor.
        """
        host = '0.0.0.0'
        port = 5001
        addr = (host, port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria o socket
        self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reinicia o socket
        self.serv_socket.bind(addr) # define as portas e quais IPs podem se conectar com o servidor
        self.serv_socket.listen(4) # define o limite de conexões

    def start(self):
        """
        Inicia o servidor e aguarda conexões dos clientes.
        """
        while True:
            print("Aguardando conexão...")
            client_sock, client_address = self.serv_socket.accept() 
            print(f'Cliente {client_address[0]} conectado.')
            print("Aguardando solicitação...")

            novaThread = ClienteThread(client_sock, client_address)

            print("Thread iniciada")
            novaThread.start()

c = Servidor()
c.start()
