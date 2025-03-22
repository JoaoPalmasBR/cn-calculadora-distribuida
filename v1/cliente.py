import socket

# Configuração do cliente
host = "127.0.0.1"
porta = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))

print("Digite uma operação matemática (ex: 3 + 4) ou 'sair' para encerrar.")

while True:
    expressao = input("Operação: ")
    if expressao.lower() == "sair":
        break
    
    cliente.send(expressao.encode())  # Envia a operação
    resposta = cliente.recv(1024).decode()  # Recebe a resposta
    print(f"Resultado: {resposta}")

cliente.close()
