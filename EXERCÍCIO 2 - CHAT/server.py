import socket
import threading
import time 

# conexões
SERVER_IP = socket.gethostbyname(socket.gethostname()) #Pegar o endereço de ip
PORT = 32092 #pegar a porta
ADDR = (SERVER_IP, PORT) # IP do server e porta usada
FORMATO = 'utf-8' # decodificar a mensagem 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #classe do socket e tipo de entrada e saída (TCP)
server.bind(ADDR) 

# Arrays para mandar toda as mensagens para todas as conexoes e variável de controle de encerramento
conexoes = [] # registro de conexões
QUIT = False

# Envia a mensagem para todas as conexoes
def enviar_mensagem_todos(mensagem):  
    global conexoes
    for conexao in conexoes:
        print(f"[ENVIANDO] ENVIANDO MENSAGEM PARA -> {conexao['nome']} | ENDERECO = {conexao['addr']}")
        conexao['conn'].send(mensagem.encode())
        time.sleep(0.5)


def handle_clientes(conn, addr):
    global QUIT
    global server
    if not QUIT: # verifica se está aberto para mandar mensagens
        print(f"[CONECTADO] O USUÁRIO DO ENDEREÇO {addr} SE CONECTOU!") # imprime o endereço do cliente que se conectou
        global conexoes
        nome = False # nome do cliente

        while(True):
            msg = conn.recv(4096).decode(FORMATO) #tamanho máximo da mensagem
            if msg != "msg=QUIT":     
                if(msg): #verifica a mensagem
                    if(msg.startswith("nome=")): # se a mensagem for um nome
                        mensagem_separada = msg.split("=") # separa a mensagem em duas 
                        nome = mensagem_separada[1] # nome está no índice 1 do array
                        mapa_da_conexao = {  # objeto com todas as informações do mapa da conexão
                            "conn": conn,
                            "addr": addr,
                            "nome": nome,
                            "last": 0
                        }
                        conexoes.append(mapa_da_conexao) #adiciona ao array que guarda as conexões

                    elif(msg.startswith("msg=")): # se a mensagem for uma mensagem (Jogador)
                        mensagem_separada = msg.split("=") # separa o conteúdo da mensagem
                        mensagem = nome + ": " + mensagem_separada[1] 
                        #mensagens.append(mensagem) #adiciona ao array de mensagens
                        enviar_mensagem_todos(mensagem)
            
            else:
                print("O SERVER FOI ENCERRADO!")
                QUIT = True
                for conexao in conexoes:
                    mensagem = 'QUIT'
                    print(f"AVISANDO O ENCERRAMENTO PARA {conexao['nome']} | ENDERECO = {conexao['addr']}")
                    conexao['conn'].send(mensagem.encode())
                conn.close()
                server.close()
                         
            
def start():
    global QUIT
    print("INICIANDO O SOCKET!")
    server.listen() # socket ouvindo cliente
    while not QUIT:
        conn, addr = server.accept() # aceita entrada do cliente, fica esperando      
        #Chamando a função handle_clientes
        thread = threading.Thread(target=handle_clientes, args=(conn, addr)) #thread que chama a funçao handle clientes
        thread.start() #inicia a thread
             
start()




                

