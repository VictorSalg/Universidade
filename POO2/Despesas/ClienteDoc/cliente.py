import socket 

def cliente():
    """
    Cria e retorna um objeto de socket cliente conectado a um servidor.

    Returns
    -------
    socket.socket
        Objeto de socket cliente conectado a um servidor.
    """
    ip = 'localhost'
    port = 5001
    addr = ((ip, port)) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket
