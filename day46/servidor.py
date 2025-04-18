import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345
server_socket.bind((host, port))

server_socket.listen(5)
print(f"Servidor esta espernado a conexao no host {host}: na porta {port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexao estabelecida com {addr}")
    
    message = client_socket.recv(1024).decode()
    print(f"Mensagem recebida: {message}")
    
    client_socket.sendall("Mensagem recebida com sucesso".encode())
    client_socket.close()
    