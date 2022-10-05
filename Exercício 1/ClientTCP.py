import socket #importa modulo socket

TCP_IP = "192.168.0.110" # endereço IP do servidor 
TCP_PORTA = 25000    # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

MENSAGEM  = input("Digite sua mensagem para o servidor: ")

# envia mensagem para servidor 
cliente.send(MENSAGEM.encode('UTF-8'))

# recebe dados do servidor 
data, addr = cliente.recvfrom(1024)

# fecha conexão com servidor
cliente.close()

print ("received data:", data)
