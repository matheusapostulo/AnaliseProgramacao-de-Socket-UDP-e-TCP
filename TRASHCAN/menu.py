import pygame, sys, random, socket, time, threading

#DEFININDO CONEXÕES
PORT = 5050
FORMATO = 'utf-8'
SERVER = "192.168.0.192" #Endereço do server
ADDR = (SERVER, PORT)

#PEGANDO O IP DA MAQUINA
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#VARIAVEIS DE CONTROLE PRA COMEÇAR O GAME
inimigo_conectado = False
vida_inimiga = 3
pontuacao_inimiga = 0



########################################################################################################################################################################################################################################################################
def matchInicio():
    global inimigo_conectado
    msg = client.recv(1024).decode()
    if (msg == 'COMECE'):
      inimigo_conectado = True
    else:
      inimigo_conectado = False

def verificarInicio():
    thread_inicio = threading.Thread(target=matchInicio)
    thread_inicio.start()

def handle_mensagens():
    while(True):
        global vida_inimiga
        global pontuacao_inimiga

        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        ip_recebido = mensagem_splitada[0]
        aux = mensagem_splitada[1].split("-")
        pontuacao_recebida = aux[0]
        vida_inimiga_recebida =  aux[1]

        if (ip_recebido != socket.gethostbyname(socket.gethostname())):
          pontuacao_inimiga = int(pontuacao_recebida)
          vida_inimiga = int(vida_inimiga_recebida)


def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem(pontuacao_vida):
    thread1 = threading.Thread(target=handle_mensagens)
    thread1.start()
    mensagem = "msg=" + str(pontuacao_vida)
    enviar(mensagem)

def enviar_IP():
    nome = socket.gethostbyname(socket.gethostname())
    enviar("IP=" + nome)

def iniciar_envio():
    enviar_IP()
    

def iniciar():
    thread2 = threading.Thread(target=iniciar_envio)
    thread2.start()



########################################################################################################################################################################################################################################################################
pygame.init()    
screen = pygame.display.set_mode((1280, 632))
pygame.display.set_caption("Trash Can Game")
screen.fill((255,255,255))

#CORES
AMARELO  = (234, 196, 58)
BRANCO = (255, 255, 255)

#FONTES USADAS
import pygame.freetype
pygame.freetype.init()
fonteTexto = pygame.freetype.Font("Fontes/upheavtt.ttf", 45)

def get_pygame_events():
  pygame_events = pygame.event.get()
  return pygame_events



########################################################################################################################################################################################################################################################################
#TECLAS
keys_pressed = get_pygame_events()

#SONS
musica_inicio = pygame.mixer.Sound("Sons/inicio.wav")
musica_inicio_abafado = pygame.mixer.Sound("Sons/inicio_abafado.wav")
musica_jogo = pygame.mixer.Sound("Sons/jogo.wav")
click = pygame.mixer.Sound("Sons/click.wav")
start_som = pygame.mixer.Sound("Sons/start.wav")
gameover_som = pygame.mixer.Sound("Sons/gameover.wav")
gameover_musica = pygame.mixer.Sound("Sons/gameover_musica.wav")
vitoria_musica = pygame.mixer.Sound("Sons/vitoria.wav")
p_bem_vindo = pygame.mixer.Sound("Sons/bem-vindo.wav")
p_500 = pygame.mixer.Sound("Sons/500.wav")
p_1000 = pygame.mixer.Sound("Sons/1000.wav")
p_gameover = pygame.mixer.Sound("Sons/gameover_som.wav")
acerto_lixeira = pygame.mixer.Sound("Sons/acerto_lixeira.wav")
erro_lixeira = pygame.mixer.Sound("Sons/erro_lixeira.wav")
som_500 = pygame.mixer.Sound("Sons/som_500.wav")
som_1000 = pygame.mixer.Sound("Sons/som_1000.wav")
som_2000 = pygame.mixer.Sound("Sons/som_2000.wav")
inimigoconectado = pygame.mixer.Sound("Sons/conectado.wav")
contagemporta = pygame.mixer.Sound("Sons/contagemporta.wav")
comecoujogo = pygame.mixer.Sound("Sons/comecoujogo.wav")
somfundomatch = pygame.mixer.Sound("Sons/fundomatch.wav")

#VIDAS ALIADAS
vida_1 = pygame.image.load('Props/vida_1.gif')
vida_2 = pygame.image.load('Props/vida_2.gif')
vida_3 = pygame.image.load('Props/vida_3.gif')

#VIDAS INIMIGAS
vidainimiga_1 = pygame.image.load('Props/vidainimiga_1.gif')
vidainimiga_2 = pygame.image.load('Props/vidainimiga_2.gif')
vidainimiga_3 = pygame.image.load('Props/vidainimiga_3.gif')

#PROPS 
organico = pygame.image.load('Props/item-organico.gif')
plastico = pygame.image.load('Props/item-plastico.gif')
papel = pygame.image.load('Props/item-papel.gif')
vidro = pygame.image.load('Props/item-vidro.gif')
metal = pygame.image.load('Props/item-metal.gif')

#BARRAS ALIADAS
barra = pygame.image.load('Props/barra_aliada.gif')
barra_200 = pygame.image.load('Props/Barra/200.gif')
barra_400 = pygame.image.load('Props/Barra/400.gif')
barra_600 = pygame.image.load('Props/Barra/600.gif')
barra_800 = pygame.image.load('Props/Barra/800.gif')
barra_1000 = pygame.image.load('Props/Barra/1000.gif')
barra_1200 = pygame.image.load('Props/Barra/1200.gif')
barra_1400 = pygame.image.load('Props/Barra/1400.gif')
barra_1600 = pygame.image.load('Props/Barra/1600.gif')
barra_1800 = pygame.image.load('Props/Barra/1800.gif')
barra_2000 = pygame.image.load('Props/Barra/2000.gif')

#BARRAS INIMIGAS
barrainimiga = pygame.image.load('Props/barra_inimiga.gif')
barrainimiga_200 = pygame.image.load('Props/Barra/200inimiga.gif')
barrainimiga_400 = pygame.image.load('Props/Barra/400inimiga.gif')
barrainimiga_600 = pygame.image.load('Props/Barra/600inimiga.gif')
barrainimiga_800 = pygame.image.load('Props/Barra/800inimiga.gif')
barrainimiga_1000 = pygame.image.load('Props/Barra/1000inimiga.gif')
barrainimiga_1200 = pygame.image.load('Props/Barra/1200inimiga.gif')
barrainimiga_1400 = pygame.image.load('Props/Barra/1400inimiga.gif')
barrainimiga_1600 = pygame.image.load('Props/Barra/1600inimiga.gif')
barrainimiga_1800 = pygame.image.load('Props/Barra/1800inimiga.gif')
barrainimiga_2000 = pygame.image.load('Props/Barra/2000inimiga.gif')

#FUNDO DO MENU
fundo_inicio_img = [pygame.image.load("Inicio/1.jpg"),pygame.image.load("Inicio/2.jpg"),pygame.image.load("Inicio/3.jpg"),pygame.image.load("Inicio/4.jpg"),pygame.image.load("Inicio/5.jpg"),
                    pygame.image.load("Inicio/6.jpg"),pygame.image.load("Inicio/7.jpg")]

#FUNDO DO JOGO
fundo_jogo_img = [pygame.image.load("Fundo/1.gif"),pygame.image.load("Fundo/2.gif"),pygame.image.load("Fundo/3.gif"),pygame.image.load("Fundo/4.gif"),pygame.image.load("Fundo/5.gif"),
                  pygame.image.load("Fundo/6.gif"),pygame.image.load("Fundo/7.gif"),pygame.image.load("Fundo/8.gif"),pygame.image.load("Fundo/9.gif"),pygame.image.load("Fundo/10.gif"),
                  pygame.image.load("Fundo/11.gif"),pygame.image.load("Fundo/12.gif"),pygame.image.load("Fundo/13.gif"),pygame.image.load("Fundo/14.gif"),pygame.image.load("Fundo/15.gif"),
                  pygame.image.load("Fundo/16.gif"),pygame.image.load("Fundo/17.gif"),pygame.image.load("Fundo/18.gif"),pygame.image.load("Fundo/19.gif"),pygame.image.load("Fundo/20.gif"),
                  pygame.image.load("Fundo/21.gif"),pygame.image.load("Fundo/22.gif"),pygame.image.load("Fundo/23.gif"),pygame.image.load("Fundo/24.gif"),pygame.image.load("Fundo/25.gif"),
                  pygame.image.load("Fundo/26.gif"),pygame.image.load("Fundo/27.gif"),pygame.image.load("Fundo/28.gif"),pygame.image.load("Fundo/29.gif"),pygame.image.load("Fundo/30.gif"),
                  pygame.image.load("Fundo/31.gif"),pygame.image.load("Fundo/32.gif"),pygame.image.load("Fundo/33.gif"),pygame.image.load("Fundo/34.gif"),pygame.image.load("Fundo/35.gif"),
                  pygame.image.load("Fundo/36.gif"),pygame.image.load("Fundo/37.gif"),pygame.image.load("Fundo/38.gif"),pygame.image.load("Fundo/39.gif"),pygame.image.load("Fundo/40.gif"),
                  pygame.image.load("Fundo/41.gif"),pygame.image.load("Fundo/42.gif"),pygame.image.load("Fundo/43.gif")]

#FUNDO DO MATCH
fundo_match_img = [pygame.image.load("Match/1.jpg"),pygame.image.load("Match/2.jpg"),pygame.image.load("Match/3.jpg"),pygame.image.load("Match/4.jpg"),pygame.image.load("Match/5.jpg"),
                    pygame.image.load("Match/6.jpg"),pygame.image.load("Match/7.jpg"),pygame.image.load("Match/8.jpg"),pygame.image.load("Match/9.jpg"),pygame.image.load("Match/10.jpg"),
                    pygame.image.load("Match/11.jpg")]

#FUNDOS LETRAS E BOTÕES
gameover_menu = pygame.image.load('Props/gameover.gif')
vitoria_menu = pygame.image.load('Props/victory.gif')
jogar_novamente = pygame.image.load('Match/jogar-novamente.gif')

#BOTÕES E BASES
lixeiras = pygame.image.load('Props/lixeiras.gif')
creditos = pygame.image.load('Props/botao-creditos.png')
jogar = pygame.image.load('Props/botao-jogar.png')
ajuda = pygame.image.load('Props/botao-ajuda.png')
fechar = pygame.image.load('Props/botao-sair.png')
som = pygame.image.load('Props/botao-som.png')
conectando = pygame.image.load('Match/conectando.gif')
conectado = pygame.image.load('Match/conectado.gif')

#TESTE
botaoteste_conectado = pygame.image.load('Props/botaoteste_conectado.gif')

#CARREGAMENTO DE PARTIDA
contagem = [pygame.image.load('Match/contagem5.gif'),pygame.image.load('Match/contagem4.gif'),pygame.image.load('Match/contagem3.gif'),pygame.image.load('Match/contagem2.gif'),pygame.image.load('Match/contagem1.gif'),
            pygame.image.load('Match/contagem0.gif')]

contagem_jgnv = [pygame.image.load('Contagem/10.gif'),pygame.image.load('Contagem/9.gif'),pygame.image.load('Contagem/8.gif'),pygame.image.load('Contagem/7.gif'),pygame.image.load('Contagem/6.gif'),
                 pygame.image.load('Contagem/5.gif'),pygame.image.load('Contagem/4.gif'),pygame.image.load('Contagem/3.gif'),pygame.image.load('Contagem/2.gif'),pygame.image.load('Contagem/1.gif')]



########################################################################################################################################################################################################################################################################
p_bem_vindo.play()

#tela_inicial_menu
def fundo_inicio():
    somfundomatch.stop()
    gameover_musica.stop()
    musica_inicio_abafado.stop()
    musica_inicio.play(-1)
    musica_jogo.stop()
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #area_botao_jogo
                    if x > 446 and x < 813:
                        if y > 342 and y < 407:
                            click.play()
                            match_partida()
                            # Inicia conexão

                    #area_botao_sair
                    if x > 639 and x < 815:
                        if y > 428 and y < 474:
                            click.play()
                            botao_sair()

                    #area_botao_ajuda
                    if x > 449 and x < 624:
                        if y > 428 and y < 476:
                            click.play()
                            botao_ajuda()

                    #area_botao_creditos
                    if x > 1066 and x < 1246:
                        if y > 504 and y < 545:
                            click.play()
                            botao_creditos()

                    #area_botao_ligar_som
                    if x > 1176 and x < 1204:
                        if y > 572 and y < 595:
                            click.play()
                            musica_inicio.stop()
                            musica_inicio.play(-1)

                    #area_botao_desligar_som
                    if x > 1219 and x < 1246:
                        if y > 573 and y < 599:
                            click.play()
                            musica_inicio.stop()

                if event.type == pygame.QUIT:
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-jogar
            screen.blit(jogar,(0,0))

            #botao-ajuda
            screen.blit(ajuda,(0,0))

            #botao-fechar
            screen.blit(fechar,(0,0))

            #botao-creditos
            screen.blit(creditos,(0,0))

            #botao-som
            screen.blit(som,(0,0))
            
            pygame.time.delay(10)
            pygame.display.update()
            i += 1



########################################################################################################################################################################################################################################################################
#tela_match
def match_partida():
    global inimigo_conectado
    
    iniciar()

    client.connect(ADDR)

    gameover_musica.stop()
    musica_inicio_abafado.stop()
    musica_inicio.stop()
    musica_jogo.stop()
    somfundomatch.play()
    sair = False 
    while not sair:      
        i = 0
        verificarInicio()
        while i < 10:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

              #TESTE PARA QUANDO SE CONECTAR
                if event.type == pygame.MOUSEBUTTONDOWN:
                  if x > 1219 and x < 1246:
                      if y > 573 and y < 599:
                            click.play()
                            botao_sair()

                  if event.type == pygame.QUIT:
                      pygame.quit()
                    
            screen.blit(fundo_match_img[i],(0, 0))
            screen.blit(botaoteste_conectado,(0,0))
            #botao-fechar
            if inimigo_conectado == False:
              screen.blit(conectando,(0, 0))
            else:
              c = 0
              screen.blit(conectado,(0, 0))
              inimigoconectado.play()
              pygame.display.update()
              pygame.time.delay(2000)

              contagemporta.play()
              somfundomatch.stop()
              while c < 6:
                screen.blit(contagem[c],(0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
                c += 1
              comecoujogo.play()
              fundo_jogo()
              pygame.display.update()
 
            pygame.time.delay(100)
            pygame.display.update()
            i += 1


########################################################################################################################################################################################################################################################################
#tela_jogo_jogar
def fundo_jogo():
    global vida_inimiga
    global pontuacao_inimiga
    gameover_musica.stop()
    vitoria_musica.stop()
    musica_inicio.stop()
    musica_jogo.stop()
    start_som.play()
    somfundomatch.stop()
    musica_jogo.play(-1)

    #PONTUACAO ALIADA    
    vida = 3
    pontuacao = 0
    pontuacao_vida = str(pontuacao) + "-" + str(vida)

    sair = False
    i = 0
    while not sair:
        while i < 43:
            pygame.display.update()
            screen.blit(fundo_jogo_img[i],(0, 0))

            for event in pygame.event.get():
              #Caso saia
              if event.type == pygame.QUIT:
                  pygame.quit()

              #MOUSEMOTION PARA CAPTURA DE POSIÇÕES
              if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]            
          
            #MOVIMENTAÇÃO OBJETO            
            #POSIÇÕES DA TELA
            posX = 610
            posY = 20

            #CRIAÇÃO DE OBJETO ALEATÓRIO
            numero = random.randint(1,5)
            if numero == 1:
              objeto = plastico        
              
            elif numero == 2:
              objeto = papel

            elif numero == 3:
              objeto = metal                

            elif numero == 4:
              objeto = vidro
                                        
            elif numero == 5:
              objeto = organico     

            while posY < 460:             
              #Fica blitando o fundo animado (?)
              if i > 41:
                i = 0
                screen.blit(fundo_jogo_img[i],(0, 0))
                
              else: 
                i += 1
                screen.blit(fundo_jogo_img[i],(0, 0))
              
              #Blita as lixeiras e a barra               
              screen.blit(lixeiras,(0,0))
              screen.blit(barra,(0,0))
              screen.blit(barrainimiga,(0,0))

              # blitar vida ALIADA
              if(vida == 3):
                screen.blit(vida_3,(0,0))
 
              elif(vida == 2):
                screen.blit(vida_2,(0,0))
 
              else:
                screen.blit(vida_1,(0,0))

              # blitar vida INIMIGA
              if(vida_inimiga == 3):
                screen.blit(vidainimiga_3,(0,0))
 
              elif(vida_inimiga == 2):
                screen.blit(vidainimiga_2,(0,0))
 
              elif(vida_inimiga == 1):
                screen.blit(vidainimiga_1,(0,0))

              else:
                vitoria(pontuacao)

              # blitar estagios da barra ALIADA
              if(pontuacao >= 0 and pontuacao < 200):
                screen.blit(barra,(0,0))
              elif(pontuacao >= 200 and pontuacao < 400):
                screen.blit(barra_200,(0,0))
              elif(pontuacao >= 400 and pontuacao < 600):
                screen.blit(barra_400,(0,0))
              elif(pontuacao >= 600 and pontuacao < 800):
                screen.blit(barra_600,(0,0))
              elif(pontuacao >= 800 and pontuacao < 1000):
                screen.blit(barra_800,(0,0))
              elif(pontuacao >= 1000 and pontuacao < 1200):
                screen.blit(barra_1000,(0,0))
              elif(pontuacao >= 1200 and pontuacao < 1400):
                screen.blit(barra_1200,(0,0))
              elif(pontuacao >= 1400 and pontuacao < 1600):
                screen.blit(barra_1400,(0,0))
              elif(pontuacao >= 1600 and pontuacao < 1800):
                screen.blit(barra_1600,(0,0))
              elif(pontuacao >= 1800 and pontuacao < 2000):
                screen.blit(barra_1800,(0,0))
              else:
                vitoria(pontuacao)
                pygame.display.update()

              # blitar estagios da barra INIMIGA
              if(pontuacao_inimiga >= 0 and pontuacao_inimiga < 200):
                screen.blit(barrainimiga,(0,0))
              elif(pontuacao_inimiga >= 200 and pontuacao_inimiga < 400):
                screen.blit(barrainimiga_200,(0,0))
              elif(pontuacao_inimiga >= 400 and pontuacao_inimiga < 600):
                screen.blit(barrainimiga_400,(0,0))
              elif(pontuacao_inimiga >= 600 and pontuacao_inimiga < 800):
                screen.blit(barrainimiga_600,(0,0))
              elif(pontuacao_inimiga >= 800 and pontuacao_inimiga < 1000):
                screen.blit(barrainimiga_800,(0,0))
              elif(pontuacao_inimiga >= 1000 and pontuacao_inimiga < 1200):
                screen.blit(barrainimiga_1000,(0,0))
              elif(pontuacao_inimiga >= 1200 and pontuacao_inimiga < 1400):
                screen.blit(barrainimiga_1200,(0,0))
              elif(pontuacao_inimiga >= 1400 and pontuacao_inimiga < 1600):
                screen.blit(barrainimiga_1400,(0,0))
              elif(pontuacao_inimiga >= 1600 and pontuacao_inimiga < 1800):
                screen.blit(barrainimiga_1600,(0,0))
              elif(pontuacao_inimiga >= 1800 and pontuacao_inimiga < 2000):
                screen.blit(barrainimiga_1800,(0,0))
              else:
                ## AQUI A GENTE MANDA PRO OUTRO QUE ELE PERDEU
                gameover(pontuacao)
                pygame.display.update()
                


              #Blita pontuacao #### TIRAR AQUI DEPOIS
              #fonteTexto.render_to(screen, (50, 50), str(pontuacao), AMARELO) 
            
              #Lógica do aumento da dificuldade
              if (pontuacao == 0 or pontuacao < 100):      
                posY += 1

              elif pontuacao <500:
                posY += 1.25

              elif pontuacao <1000:
                posY += 1.5

              elif pontuacao < 1500:
                posY += 1.75

              elif pontuacao < 2000:
                posY += 2

              else:
                posY += 15

              # Movimentação do X e aceleração do Y
              for event in pygame.event.get():
                v = 0 
                
              comandos = pygame.key.get_pressed()
              if comandos[pygame.K_LEFT]:
                posX -= 5
              if comandos[pygame.K_RIGHT]:
                posX += 5
              if comandos[pygame.K_DOWN]:
                posY += 5


              #Vai blitando o objeto aleatório de acordo com a posição
              screen.blit(objeto, (posX,posY))
              pygame.display.update()

            #COLISÕES
            #Colisão lixeira plastico 
            if objeto == plastico:
              if(posX > 180 and posX < 305):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 180 or posX >305):
                if(vida!=1):
                  # decrementa vida
                  vida -= 1
                  erro_lixeira.play()
                else: 
                  vida = 0 
                  pontuacao_vida = str(pontuacao) + "-" + str(vida)
                  enviar_mensagem(pontuacao_vida)
                  gameover(pontuacao)

            #Colisão lixeira papel
            if objeto == papel:
              if(posX > 370 and posX < 505):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 370 or posX > 505):
                if(vida!=1):
                  # decrementa vida
                  vida -= 1
                  erro_lixeira.play()

                else:
                  vida = 0 
                  pontuacao_vida = str(pontuacao) + "-" + str(vida)
                  enviar_mensagem(pontuacao_vida)
                  gameover(pontuacao)
                

            #Colisão lixeira metal
            if objeto == metal:
              if(posX > 560 and posX < 700):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 560 or posX > 700):
                if(vida!=1):
                  #decrementa vida
                  vida -= 1
                  erro_lixeira.play()

                else: 
                  vida = 0 
                  pontuacao_vida = str(pontuacao) + "-" + str(vida)
                  enviar_mensagem(pontuacao_vida)
                  gameover(pontuacao)

            #Colisão lixeira vidro
            if objeto == vidro:
              if(posX > 750 and posX < 895):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 750 or posX > 895):
                if(vida!=1):
                  #decrementa vida
                  vida -= 1
                  erro_lixeira.play()

                else: 
                  vida = 0 
                  pontuacao_vida = str(pontuacao) + "-" + str(vida)
                  enviar_mensagem(pontuacao_vida)
                  gameover(pontuacao)

            #Colisão lixeira organico
            if objeto == organico:
              if(posX > 950 and posX < 1090):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 950 or posX > 1090):
                if(vida!=1):
                  #decrementa vida
                  vida -= 1
                  erro_lixeira.play()

                else: 
                  vida = 0 
                  pontuacao_vida = str(pontuacao) + "-" + str(vida)
                  enviar_mensagem(pontuacao_vida)
                  gameover(pontuacao)

            if pontuacao == 500:
                som_500.play()
                pygame.time.delay(200)
                p_500.play()
                
            if pontuacao == 1000:
                som_1000.play()
                pygame.time.delay(200)
                p_1000.play()

            if pontuacao == 2000:
                som_2000.play()
                pygame.time.delay(200)
            
            pontuacao_vida = str(pontuacao) + "-" + str(vida)
            enviar_mensagem(pontuacao_vida)
            #enviar_mensagem(pontuacao) ## colocar no loop do item
                

      
########################################################################################################################################################################################################################################################################              
#botao_sair
def botao_sair():
    pygame.quit()

def botao_ajuda():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-voltar
            voltar = pygame.image.load('Props/botao-voltar.png')
            screen.blit(voltar,(0,0))

            #botao-voltar
            como_jogar = pygame.image.load('Props/como_jogar.png')
            screen.blit(como_jogar,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1



########################################################################################################################################################################################################################################################################
def botao_creditos():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-voltar
            voltar = pygame.image.load('Props/botao-voltar.png')
            screen.blit(voltar,(0,0))

            #desenvolvedores
            desenvolvedores = pygame.image.load('Props/desenvolvedores.png')
            screen.blit(desenvolvedores,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1



########################################################################################################################################################################################################################################################################
def gameover(pontuacao):
    musica_jogo.stop()
    gameover_som.play()
    p_gameover.play()
    gameover_musica.play(-1)
    sair = False 
    global vida
    global pontuacao_vida
    while not sair:      
        i = 0
        while i < 12:            
            screen.blit(jogar_novamente,(0, 0))
            #gameover_menu
            fonteTexto.render_to(screen, (377, 418), str(pontuacao), BRANCO)
            screen.blit(gameover_menu,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            vida = 3
            pontuacao = 0
            pontuacao_vida = str(pontuacao) + "-" + str(vida)
            enviar_mensagem(pontuacao_vida)
            i += 1
            d = 0
            c = 0
            pygame.display.update()

            while d < 10:
                for event in pygame.event.get():
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if event.type == pygame.MOUSEBUTTONDOWN:
                      if x > 726 and x < 905:
                          if y > 483 and y < 525:
                              click.play()
                              pygame.quit()

                    if event.type == pygame.QUIT:
                        pygame.quit()

                screen.blit(contagem_jgnv[d],(0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
                d += 1
                
            screen.blit(jogar_novamente,(0, 0))
            pygame.display.update()
            contagemporta.play()
            gameover_musica.stop()
            while c < 6:
                screen.blit(contagem[c],(0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
                c += 1
            comecoujogo.play()
            fundo_jogo()
            pygame.display.update()



########################################################################################################################################################################################################################################################################
def vitoria(pontuacao):
    som_2000.play()
    musica_jogo.stop()
    vitoria_musica.play()
    sair = False 
    global vida
    global pontuacao_vida
    while not sair:      
        i = 0
        while i < 12:
            screen.blit(jogar_novamente,(0, 0))
            #gameover_menu
            fonteTexto.render_to(screen, (377, 418), str(pontuacao), BRANCO)
            screen.blit(vitoria_menu,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1
            d = 0
            c = 0
            pygame.display.update()

            while d < 10:
                for event in pygame.event.get():
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if event.type == pygame.MOUSEBUTTONDOWN:
                      if x > 726 and x < 905:
                          if y > 483 and y < 525:
                              click.play()
                              pygame.quit()

                    if event.type == pygame.QUIT:
                        pygame.quit()

                screen.blit(contagem_jgnv[d],(0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
                d += 1
                
            screen.blit(jogar_novamente,(0, 0))
            pygame.display.update()
            contagemporta.play()
            vitoria_musica.stop()
            while c < 6:
                screen.blit(contagem[c],(0, 0))
                pygame.display.update()
                pygame.time.delay(1000)
                c += 1
            comecoujogo.play()
            fundo_jogo()
            pygame.display.update()




########################################################################################################################################################################################################################################################################
def main():
    fundo_inicio()
main()
