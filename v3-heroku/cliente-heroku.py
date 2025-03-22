import requests

# Configuração do cliente
url = "https://cn-calculadora-distribuida-acd2eb356d43.herokuapp.com/calcular"

print("Digite uma operação matemática (ex: 3 + 4) ou 'sair' para encerrar.")

while True:
    expressao = input("Operação: ")
    if expressao.lower() == "sair":
        break

    # Envia a requisição POST com o corpo JSON
    response = requests.post(url, json={"expressao": expressao})

    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        resultado = response.json().get("resultado", "Erro ao obter resultado")
        print(f"Resultado: {resultado}")
    else:
        erro = response.json().get("erro", "Erro desconhecido")
        print(f"Erro: {erro}")
