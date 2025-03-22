# cn-calculadora-distribuida

## Objetivo:

Implementar um servidor que recebe operações matemáticas de múltiplos clientes, processa-as e retorna o resultado. O servidor deve usar multithreading para lidar com várias requisições ao mesmo tempo.

### Servidor

- Aceita conexões de múltiplos clientes.
- Cada cliente é tratado em uma thread separada.
- Recebe operações matemáticas (ex: 2 + 3 ou 10/2) dos clientes.
- Processa a operação e envia o resultado de volta ao cliente.

### Cliente

- Conecta-se ao servidor.
- Envia operações matemáticas para o servidor.
- Recebe e exibe o resultado.
