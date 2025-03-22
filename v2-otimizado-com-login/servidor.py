import socket
import threading
import logging

# Configuração de logs
logging.basicConfig(filename="server.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Usuários cadastrados (simulação de autenticação)
USUARIOS = {
    "joao": "1234",
    "maria": "abcd"
}

# Função para calcular expressões matemáticas
def calcular(expressao):
    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        return str(resultado)
    except Exception as e:
        return f"Erro: {str(e)}"

# Função de autenticação do usuário
def autenticar(conn):
    conn.send(b"Usuario: ")
    usuario = conn.recv(1024).decode().strip()

    conn.send(b"Senha: ")
    senha = conn.recv(1024).decode().strip()

    if USUARIOS.get(usuario) == senha:
        conn.send(b"Autenticado com sucesso!\n")
        logging.info(f"Usuario autenticado: {usuario}")
        return usuario
    else:
        conn.send(b"Falha na autenticacao!\n")
        logging.warning(f"Tentativa de login falhou para usuario: {usuario}")
        return None

# Função que lida com cada cliente em uma thread separada
def tratar_cliente(conn, addr):
    logging.info(f"Nova conexao de {addr}")
    print(f"Cliente {addr} conectado.")

    usuario = autenticar(conn)
    if not usuario:
        conn.close()
        return

    while True:
        try:
            conn.send(b"Digite uma operacao (ex: 2 + 3) ou 'sair': ")
            dados = conn.recv(1024).decode().strip()
            if not dados or dados.lower() == "sair":
                break

            logging.info(f"Usuario {usuario} enviou: {dados}")
            resposta = calcular(dados)
            conn.send(f"Resultado: {resposta}\n".encode())
        except:
            break

    logging.info(f"Usuario {usuario} desconectado")
    print(f"Cliente {addr} desconectado.")
    conn.close()

# Configuração do servidor
def iniciar_servidor(host="0.0.0.0", porta=5000):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)
    print(f"Servidor rodando em {host}:{porta}")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()

# Iniciar o servidor
if __name__ == "__main__":
    iniciar_servidor()
