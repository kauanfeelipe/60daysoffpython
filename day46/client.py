import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
porta = 12345

cliente_socket.connect((host, porta))

mensagem = "Oi, servidor!"
cliente_socket.send(mensagem.encode())

response = cliente_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

cliente_socket.close()