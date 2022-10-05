import socket
import threading


PORT = 32092
FORMATO = 'utf-8'
SERVER = "192.168.56.1" #Endereço do server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("[CONECTADO AO SERVIDOR] Entre com seu nome e comece a enviar mensagens!")

SERVER_STATE = False

def handle_mensagens():
    global SERVER_STATE
    global client
    while True:
        msg = client.recv(4096).decode() 
        if(msg):
            if(msg != 'QUIT'):
                print(msg)
            else:
                print("Um usuário enviou o comando 'QUIT', a conexão está sendo encerrada!")
                SERVER_STATE = True
                client.shutdown(socket.SHUT_RDWR)
                client.close()
        else:
            break
        
def enviar(mensagem): 
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    global SERVER_STATE
    while True:
        mensagem = input()
        enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread1.start()
    thread2 = threading.Thread(target=iniciar_envio)
    thread2.start()       

iniciar()


