import socket
import threading

# Função para calcular expressões matemáticas
def calcular(expressao):
    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        return str(resultado)
    except Exception as e:
        return f"Erro: {str(e)}"

# Função que lida com cada cliente em uma thread separada
def tratar_cliente(conn, addr):
    print(f"Cliente {addr} conectado.")
    
    while True:
        try:
            dados = conn.recv(1024).decode()
            if not dados:
                break  # Cliente desconectou
            
            print(f"Recebido de {addr}: {dados}")
            resposta = calcular(dados)
            conn.send(resposta.encode())  # Envia a resposta ao cliente
        except:
            break

    print(f"Cliente {addr} desconectado.")
    conn.close()

# Configuração do servidor
def iniciar_servidor(host="0.0.0.0", porta=5000):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)  # Permite até 5 conexões pendentes
    print(f"Servidor rodando em {host}:{porta}")

    while True:
        conn, addr = servidor.accept()  # Aceita nova conexão
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()

# Iniciar o servidor
if __name__ == "__main__":
    iniciar_servidor()
