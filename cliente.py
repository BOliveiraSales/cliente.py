import socket 

port = 80 

while True:
    ip = input('digite o ip de conexao: ') 
    addr = ((ip,port)) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr) 
    #data = client_socket.recv(1024)
    # mensagem = input("digite uma mensagem para enviar ao servidor:") 
    mensagem = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
    client_socket.send(mensagem.encode())
    resposta = client_socket.recv(4096).decode()
    print ('resposta:', resposta)
    client_socket.close()