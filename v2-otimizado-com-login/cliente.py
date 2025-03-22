import socket

# Configuração do cliente
host = "127.0.0.1"
porta = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))

def receber_mensagem():
    """Recebe uma mensagem do servidor e imprime corretamente"""
    mensagem = cliente.recv(1024).decode().strip()
    print(mensagem)
    return mensagem

# Enviar usuário e senha
usuario_msg = receber_mensagem()  # Usuario:
cliente.send(input(usuario_msg + " ").encode() + b"\n")

senha_msg = receber_mensagem()  # Senha:
cliente.send(input(senha_msg + " ").encode() + b"\n")

# Verifica se a autenticação foi bem-sucedida
resposta = receber_mensagem()
if "falhou" in resposta.lower():
    cliente.close()
    exit()

# Loop para enviar operações matemáticas
while True:
    operacao_msg = receber_mensagem()  # Digite uma operação
    expressao = input(operacao_msg + " ")
    
    if expressao.lower() == "sair":
        break

    cliente.send(expressao.encode() + b"\n")
    receber_mensagem()  # Exibe o resultado

cliente.close()
