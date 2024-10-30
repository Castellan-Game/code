import pygame
import sys
import random
import time
from pygame.locals import *




# Inicialização do Pygame
pygame.init()

# Resolução
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Castellan")

# Cores
BLACK = (0,0,0)
WHITE = (255, 255, 255)
DOOR_COLOR = (0, 255, 0)  # Cor da porta (verde)

vel = 1

vezes = 0
abertura = 0
#music
pygame.mixer.music.load("./imgs/intro.mp3")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

levelsound = pygame.mixer.Sound('./imgs/levelupsound.mp3')
levelsound.set_volume(0.4)

menubtnsound = pygame.mixer.Sound('./imgs/menubtnsound.mp3')
menubtnsound.set_volume(0.1)

class CastellanMove(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spritesd = []
        self.spritesd.append(pygame.image.load(
            "./charsprite/castellan.png"))
        self.spritesd.append(pygame.image.load(
            "./charsprite/castellanmovementright1.png"))
        self.spritesd.append(pygame.image.load(
            "./charsprite/castellanmovementright2.png"))
        self.spritesd.append(pygame.image.load(
            "./charsprite/castellanmovementthree.png"))
        self.spritesd.append(pygame.image.load(
            "./charsprite/castellanmovementfour.png"))
        self.atual = 0
        self.image = self.spritesd[self.atual]
        self.image = pygame.transform.scale(self.image, [90, 160])
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 600
        self.rect.x = 100
        self.rect.y = 550
        self.andard = False
        self.andare = False

    def andardireita(self):
        self.andard = True

    def andaresquerda(self):
        self.andare = True

    def atualpos(self):
        atual_pos = self.rect.x
        return atual_pos

    def update(self):
        if self.andard == True:
            self.rect.x += 18 * vel
            self.atual = self.atual + 0.8
            if self.atual >= len(self.spritesd):
                self.atual = 0
                self.andard = False
            self.image = self.spritesd[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [90, 160])
        if self.andare == True:
            self.rect.x -= 8
            self.atual = self.atual + 0.8
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.andard = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [90, 160])

    def resetchar2(self):
        self.rect.x = 100
        self.rect.y = 640
    def resetcharTuto(self):
        self.rect.x = 100
        self.rect.y = 610

    def movetofar(self):
        self.rect.x = 2000


movementocastellan = pygame.sprite.Group()
castellanm = CastellanMove()
movementocastellan.add(castellanm)

audiotransition2 = pygame.mixer.Sound('./audio/transitionaudio.mp3')

relogio = pygame.time.Clock

# configurações do Personagem
character_image = pygame.image.load('./charsprite/castellan.png')
character_image = pygame.transform.scale(character_image, [90, 160])
character_rect = character_image.get_rect()
character_rect.x = 100
character_rect.y = HEIGHT - 170  # Ajuste para a altura do chão
jumping = 0
jump_start_time = 0
jump_duration = 0.5  # Duração do pulo em segundos
jump_height = 20  # Altura máxima do pulo
jump_speed = 20
gravity = 2.8
y_velocity = 0


# configs das cartas / livro 
menormapaimage = pygame.image.load('./imgs/menormapa.png')
menormapaimage = pygame.transform.scale(menormapaimage, [1000, 750])

mapamenor_rect = menormapaimage.get_rect()

mapamenor_rect.x = 220
mapamenor_rect.y = HEIGHT - 780 

maiormapaimage = pygame.image.load('./imgs/maiormapa.png')
maiormapaimage = pygame.transform.scale(maiormapaimage, [1000, 750])

mapamaior_rect = maiormapaimage.get_rect()

mapamaior_rect.x = 220
mapamaior_rect.y = HEIGHT - 780 


minerioimg = pygame.image.load('./imgs/mineriomap.png') 
minerioimg = pygame.transform.scale(minerioimg, [1000, 750])

minerioimg_rect = minerioimg.get_rect()

minerioimg_rect.x = 220
minerioimg_rect.y = HEIGHT - 780


letter1_image = pygame.image.load('./imgs/carta1.png')
letter1_image = pygame.transform.scale(letter1_image, [480, 640])

letter_rect = letter1_image.get_rect()

letter_rect.x = 500
letter_rect.y = HEIGHT - 725

letter2_image = pygame.image.load('./imgs/carta2.png')
letter2_image = pygame.transform.scale(letter2_image, [480, 640])

letter2_rect = letter2_image.get_rect()

letter2_rect.x = 500
letter2_rect.y = HEIGHT - 725


letter3_image = pygame.image.load('./imgs/carta3.png')
letter3_image = pygame.transform.scale(letter3_image, [480, 640])

letter3_rect = letter3_image.get_rect()

letter3_rect.x = 500
letter3_rect.y = HEIGHT - 725
# variáveis de estado

# porta abrir para liberar a próxima fase (por enquanto não funciona)
door_open = False
door_open2 = False
# transição - carta
opacidade = 0
aumentando_opacidade = False
opacidade2 = 0
opacidade3 = 0

opacidadeMenorMapa = 0
opacidadeMaiorMapa = 0
# andar
isWing = False

# carta necessária pra primeirafase:
lettersaw = False
# porta
door_rect = pygame.Rect(1350, 650, 90, 160)  # Definindo a porta

# projeto da terceira fase
obstacle_image = pygame.image.load('./imgs/arvore].png')
obstacle_image = pygame.transform.scale(obstacle_image, [50, 100])
obstacles = []
obstacle_speed = 5

# Funções

def resetD(resetar):
    resetar = False

def opacity(aumentar_opacidade, opacidade, imagem, posimage):
    # Aumenta a opacidade se estiver no modo de transição
    if aumentar_opacidade and opacidade < 255:
        opacidade += 2  # Aumenta a opacidade gradualmente
    elif opacidade >= 255:
        aumentar_opacidade = False  # Para de aumentar ao atingir opacidade máxima

        # Aplica a opacidade na imagem
    imagem.set_alpha(opacidade)

    screen.blit(imagem, posimage)
    # Desenha a imagem com a opacidade ajustada


def openletter():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(letter1_image, [500, 725])


def verposicao(mouse, x, y, w, h):
    if x < mouse[0] < (x + w) and y < mouse[1] < y + h:
        return 1
    else:
        return 0


def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


# necessário pra repetição da imagem -> segunda fase
secondphaseimage = pygame.image.load('./imgs/pagsix.jpg')
secondphaseimage = pygame.transform.scale(secondphaseimage, (1440, 810))

menucimage = pygame.image.load('./imgs/menuc.jpg')
menucimage = pygame.transform.scale(menucimage, (1440, 810))

def show_image(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(image, (0, 0))


def creds():
    global vezes
    
    vezes = vezes + 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                print(vezes)
                if verposicao(mousepos, 73, 620, 130, 100) == 1:
                    main_menu()
                    

        screen.fill(WHITE)  # Cor de fundo
        show_image('./imgs/credsimg.jpg')  # Imagem de fundo do menu

        pygame.display.flip()


def main_menu():
    opacidademenu = 0
    global vezes
    global abertura

    if abertura == 0:
        pygame.time.delay(800)
        abertura = 1
    while True:

        
        
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Simula clicar em "Jogar"
                    game_pages()
                if event.key == pygame.K_c:  # Simula clicar em "Créditos"
                    creds()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                if verposicao(mousepos, 575, 450, 300, 100) == 1:
                    vezes = vezes + 1
                    menubtnsound.play(0)
                    game_pages()
                    
                elif verposicao(mousepos, 73, 626, 130, 100) == 1:
                    creds()
                    vezes = vezes + 1

        screen.fill(BLACK)  # Cor de fundo

        if vezes == 0:
            menucimage.set_alpha(opacidademenu)
            screen.blit(menucimage, (0, 0))
            if opacidademenu <= 100 :
                opacidademenu += 1
                print("ta rodando")
                screen.set_alpha(opacidademenu)
                pygame.time.delay(9)
            elif opacidademenu > 100 and opacidademenu < 255:
                opacidademenu += 1.5
                print("ta rodando")
                screen.set_alpha(opacidademenu)
                pygame.time.delay(7)
        
            else:
                show_image('./imgs/menuc.jpg')

            screen.set_alpha(opacidademenu)
        else:
            show_image('./imgs/menuc.jpg')

        pygame.display.flip()


def verificar_input(texto, a):
    global p
    if texto == a:
        p = True
        return 1


def secondgamepage():
    page2images = [
        './imgs/cast6.jpg',
        
    ]

    i = 0
    
    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 0, 0, WIDTH, HEIGHT) == 1:
                        i += 1

                if i >= 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        print(mousepos)
                        if verposicao(mousepos, 70, 650, 130, 100) == 1:
                            i -= 1

            if i == 1:
                break
            screen.fill(WHITE)
            show_image(page2images[i])
            pygame.display.flip()
    vezes = + 1
    first_level()


def thirdphase2_pages():
    page_images = [
        './imgs/27.png',
        './imgs/28.png',
        './imgs/29.png',
        './imgs/audrey1.png',
        './imgs/audrey2.png',
        
        

    ]

    i = 0
    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)

                    if i == 0:
                        if verposicao(mousepos, 585, 610, 119, 102) == 1:
                            i += 1
                    else:
                        if verposicao(mousepos, 0, 0, WIDTH, HEIGHT) == 1:
                            i += 1


                

            if i == 5:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    espacial_walking()

def final_pages():
    global vezes
    page_images = [
        './imgs/familia.png',
        './imgs/gameover.png'
       
        

    ]

    i = 0
    while i < 2:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)

                    if i == 0:
                        if verposicao(mousepos, 0, 0, WIDTH, HEIGHT) == 1:
                            i += 1
                    if i == 1:
                        if verposicao(mousepos, 133, 692, 351, 34) == 1:
                            i += 1


                

            if i == 2:
                vezes = 0
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    main_menu()

def thirdphase_pages():
    page_images = [
        './imgs/25.png',
       
        

    ]

    i = 0
    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 0, 0, WIDTH, HEIGHT) == 1:
                        i += 1

                

            if i == 1:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    third_level()

def game_pages():
    page_images = [
        './imgs/cast1.png',
        './imgs/cast1.2.png',
        './imgs/cast2.jpg',
        './imgs/cast3.png',
        './imgs/castsotao.png',
        './imgs/cast4.jpg',
        './imgs/cast4.1.jpg',
        './imgs/cast5.jpg',
        

    ]

    i = 0
    while i < 8:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 1260, 650, 130, 100) == 1:
                        i += 1

                if i >= 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        print(mousepos)
                        if verposicao(mousepos, 70, 650, 130, 100) == 1:
                            i -= 1

            if i == 8:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    tutorial_introduction()

def castlepages():
    
    castle_images = [
        './imgs/castelo.png',
        './imgs/fase2.png',
        './imgs/fase21.png',
        './imgs/fase22.png',
        

    ]
    i = 0
    while i < 4:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 0,0,WIDTH,HEIGHT) == 1:
                        i += 1

                if i >= 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        print(mousepos)
                        if verposicao(mousepos, 70, 650, 130, 100) == 1:
                            i -= 1

            if i == 4:
                break
            screen.fill(WHITE)
            show_image(castle_images[i])
            pygame.display.flip()

    second_level()


def level_up2():
    levelup2images = [
        './imgs/level_up2.png'
        

    ]

    i = 0
    levelsound.play(0)
    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 836, 257, 323, 320) == 1:
                        i += 1

               
            if i == 1:
                break
            screen.fill(WHITE)
            show_image(levelup2images[i])
            pygame.display.flip()

    thirdphase_pages()

def level_up():
    levelupimages = [
        './imgs/levelup.png'
        

    ]

    i = 0
    levelsound.play(0)
    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 225, 237, 317, 317) == 1:
                        i += 1

               
            if i == 1:
                break
            screen.fill(WHITE)
            show_image(levelupimages[i])
            pygame.display.flip()

    second_level()


def espacial_walking():
    castellanm.resetcharTuto()
    global vel
    vel = 1.3
    global isWing
    isWing = False
    global aumentando_opacidade
    global opacidade

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_d:
                    isWing = True
                    print('vc apertou')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    isWing = False
                    print('vc soltou')

            if isWing == True:
                print('w')
                print('to apertando')

                castellanm.andardireita()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)

            
        screen.fill(WHITE)
        show_image('./imgs/31.png')

        movementocastellan.draw(screen)
        movementocastellan.update()
        pygame.display.flip()

        pygame.time.delay(30)
        if castellanm.atualpos() >= 1250:
            vel = 1.2
            break
        
    final_pages()

def tutorial_introduction():
    castellanm.resetcharTuto()
    global vel
    vel = 1.2
    global isWing
    isWing = False
    global aumentando_opacidade
    global opacidade

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_d:
                    isWing = True
                    print('vc apertou')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    isWing = False
                    print('vc soltou')

            if isWing == True:
                print('w')
                print('to apertando')

                castellanm.andardireita()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)

            
        screen.fill(WHITE)
        show_image('./imgs/cast9.jpg')

        movementocastellan.draw(screen)
        movementocastellan.update()
        pygame.display.flip()

        pygame.time.delay(30)
        if castellanm.atualpos() >= 930:

            break
        
    secondgamepage()


def mappart():
    mappages = [
        './imgs/menormapa.png' ,
        './imgs/maiormapa.png'

    ]
    i = 0

    while i < 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao(mousepos, 714, 375, 135, 25) == 1 and i == 0:
                        i += 1
                    if verposicao(mousepos, 905, 289, 113, 25) == 1 and i == 1:
                        i += 1

               
            if i == 2:
                break
            screen.fill(WHITE)
            show_image(mappages[i])
            pygame.display.flip()

    main_menu()


def first_level():
    
    global door_open
    global isWing
    isWing = False
    answer = random.randint(1, 10) + random.randint(1, 10)
    user_input = ""
    user_input = user_input.lower()
    input_timer = time.time()
    lettersaw = 0
    letter2saw = 0
    letter3saw = 0
    global aumentando_opacidade
    global opacidade
    global opacidade2
    global opacidade3
    teclas_presse = []
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    isWing = True
                    print('vc apertou')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    isWing = False
                    print('vc soltou')

            if isWing == True:
                print('w')
                print('to apertando')

                castellanm.andardireita()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Remove o último caractere da string
                    user_input = user_input[:-1]
            # Verifica se a tecla pressionada é Enter
                elif event.key == pygame.K_RETURN:
                    # Verifica o input digitado

                    if verificar_input(user_input, "log") == 1:
                        door_open = True
                        print('abriu', door_open)
                    user_input = ""  # Limpa o input após verificar
                else:
                    # Adiciona a tecla pressionada ao texto digitado
                    user_input += event.unicode

                if verificar_input == 1:
                    door_open == True

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(isWing)
                mousepos = pygame.mouse.get_pos()
                print(mousepos,letter3saw)
                if verposicao(mousepos, 1141, 204, 80, 55) == 1:
                    openlettero = 1
                    if openlettero == 1:
                        lettersaw = 1
                if lettersaw == 1:
                    if verposicao(mousepos, 923, 105, 32, 28) == 1 and opacidade > 150:
                        lettersaw = 2
                    if verposicao(mousepos, 584, 272, 310, 59) == 1:
                        lettersaw = 2
                        
                        letter2saw = 1

                if letter2saw == 1:
                    letter3saw = 0
                    if verposicao(mousepos, 923, 105, 32, 28) == 1 and opacidade2>150:
                        letter2saw = 2

                    if verposicao(mousepos, 584, 473, 310, 59) == 1:
                        letter2saw = 2
                        
                        letter3saw = 1
                        

                if letter3saw == 1:
                    if verposicao(mousepos, 923, 105, 32, 28) == 1:
                        letter3saw = 2
                    if verposicao(mousepos, 584, 272, 310, 59) == 1:
                        door_open = True
                        
                   
                    
                        
                        

        


        # Movimentação do personagem(Sem uso até então)
        keys = pygame.key.get_pressed()

        # Resetar o input a cada 5 segundos
        if time.time() - input_timer > 5:
            user_input = ""
            input_timer = time.time()

        screen.fill(WHITE)
        show_image('./imgs/cast7.png')

        if lettersaw == 1:
            letter1_image.set_alpha(opacidade)
            screen.blit(letter1_image, letter_rect)
            if opacidade < 255:
                opacidade += 15
                print("ta rodando")

                pygame.time.delay(5)

        letter1_image.set_alpha(opacidade)

        if lettersaw == 2:
            letter1_image.set_alpha(opacidade)
            screen.blit(letter1_image, letter_rect)
            if opacidade > 0:
                opacidade -= 15
                print("ta rodando")

                pygame.time.delay(2)
            if opacidade == 0:
                lettersaw = 0
        

        letter1_image.set_alpha(opacidade)



        if letter2saw == 1:
            letter2_image.set_alpha(opacidade2)
            screen.blit(letter2_image, letter2_rect)
            if opacidade2 < 255:
                opacidade2 += 15
                print("ta rodando")
            
                pygame.time.delay(5)

        letter2_image.set_alpha(opacidade2)

        if letter2saw == 2:
            letter2_image.set_alpha(opacidade2)
            screen.blit(letter2_image, letter2_rect)
            if opacidade2 > 0:
                opacidade2 -= 15
                print("ta rodando")

                pygame.time.delay(2)
            if opacidade2 == 0:
                letter2saw = 0

        letter2_image.set_alpha(opacidade2)



        if letter3saw == 1:
            letter3_image.set_alpha(opacidade3)
            screen.blit(letter3_image, letter3_rect)
            if opacidade3 < 255:
                opacidade3 += 15
                print("ta rodando")
            
                pygame.time.delay(5)

        letter3_image.set_alpha(opacidade3)

        if letter3saw == 2:
            letter3_image.set_alpha(opacidade3)
            screen.blit(letter3_image, letter3_rect)
            if opacidade3 > 0:
                opacidade3 -= 15
                print("ta rodando")

                pygame.time.delay(2)
            if opacidade3 == 0:
                letter3saw = 0

        letter3_image.set_alpha(opacidade3)



        

       
    
        pygame.display.flip()

        pygame.time.delay(30)
        if door_open == True:
            letter3saw = 0
            opacidade3 = 0
            door_open = False
            break

    level_up()


def second_level():
    global aumentando_opacidade
    diminuindoopacidade = 0
    opacidadesecond = 255
    global door_open2
    global isWing
    global vel
    mapasaw = 0
    mapa2saw = 0
    opacidadeMenorMapa = 0
    opacidadeMaiorMapa = 0
    vel = 0.5
    isWing = False
    user_input = ""
    input_timer = time.time()
    abrir_mapa = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(isWing)
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                print(mapasaw, mapa2saw)
            
                if verposicao(mousepos, 980, 65, 240, 157) == 1 and mapasaw == 0 :
                    print('abrindo')
                    abrir_mapa = 1

                if verposicao(mousepos, 980, 65, 240, 157) == 1 and mapasaw == 3 :
                    print('abrindo')
                    abrir_mapa = 2    
                    
                if abrir_mapa == 1:
                    mapasaw = 1
                    abrir_mapa = 0

                if abrir_mapa == 2:
                    mapa2saw = 1 
                    abrir_mapa = 0  

                if mapasaw == 1:    
                    if verposicao(mousepos, 716, 381, 93, 20) == 1 and opacidadeMenorMapa > 150:
                        mapasaw = 3
                        print(mapasaw , mapa2saw)
                    if verposicao(mousepos, 1153, 45, 55, 50) == 1:
                        mapasaw = 2
                        
                        

                if mapa2saw == 1:
                    
                    if verposicao(mousepos, 847, 293, 87, 25) == 1 and opacidadeMaiorMapa>150:
                        mapa2saw = 3
                    if verposicao(mousepos, 1153, 45, 55, 50) == 1:
                        mapa2saw = 2
                        print('clicou')
                        

            
        # Resetar o input a cada 5 segundos
        
        # Movimentação do personagem

        screen.fill(WHITE)
       
        show_image('./imgs/mapaimg.png')



        if mapasaw == 1:
            menormapaimage.set_alpha(opacidadeMenorMapa)
            screen.blit(menormapaimage, mapamenor_rect)
            if opacidadeMenorMapa < 255:
                opacidadeMenorMapa += 7.5
                print("ta rodando")
                print(opacidadeMenorMapa)
                pygame.time.delay(2)

        menormapaimage.set_alpha(opacidadeMenorMapa)

        if mapasaw == 2:
            menormapaimage.set_alpha(opacidadeMenorMapa)
            screen.blit(menormapaimage, mapamenor_rect)
            if opacidadeMenorMapa > 0:
                opacidadeMenorMapa -= 15
                print("ta rodando")

                pygame.time.delay(4)
            if opacidadeMenorMapa == 0:
                mapasaw = 0
        

        menormapaimage.set_alpha(opacidadeMenorMapa)



        if mapa2saw == 1:
            maiormapaimage.set_alpha(opacidadeMaiorMapa)
            screen.blit(maiormapaimage, mapamaior_rect)
            if opacidadeMaiorMapa < 255:
                opacidadeMaiorMapa += 7.5
                print("ta rodando")
            
                pygame.time.delay(2)

        maiormapaimage.set_alpha(opacidadeMaiorMapa)

        if mapa2saw == 2:
            maiormapaimage.set_alpha(opacidadeMaiorMapa)
            screen.blit(maiormapaimage, mapamaior_rect)
            if opacidadeMaiorMapa > 0:
                opacidadeMaiorMapa -= 15
                print("ta rodando")
                
                pygame.time.delay(4)
            if opacidadeMaiorMapa == 0:
                mapa2saw = 0

        maiormapaimage.set_alpha(opacidadeMaiorMapa)

        if mapasaw == 3:
            menormapaimage.set_alpha(opacidadeMenorMapa)
            screen.blit(menormapaimage, mapamenor_rect)
            if opacidadeMenorMapa > 0:
                opacidadeMenorMapa -= 15
                print("ta rodando")

                pygame.time.delay(4)
            if opacidadeMenorMapa == 0:
                mapasaw = 3

        menormapaimage.set_alpha(opacidadeMenorMapa)

        if mapa2saw == 3:
            maiormapaimage.set_alpha(opacidadeMaiorMapa)
            screen.blit(maiormapaimage, mapamaior_rect)
            if opacidadeMaiorMapa > 0:
                opacidadeMaiorMapa -= 15
                print("ta rodando")
                
                pygame.time.delay(4)
            if opacidadeMaiorMapa == 0:
                mapa2saw = 3
                level_up2()

        

       
        pygame.display.flip()
        
    
def third_level():
    global aumentando_opacidade
    diminuindoopacidade = 0
    opacidadesecond = 255
    global door_open2
    global isWing
    global vel
    mineriosaw = 0
    
    opacidadeMinerioMapa = 0
    opacidadeMaiorMapa = 0
    vel = 0.5
    isWing = False
    user_input = ""
    input_timer = time.time()
    abrir_minerio = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(isWing)
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                print(mineriosaw)
            
                if verposicao(mousepos, 856, 605, 67, 60) == 1 and mineriosaw == 0 :
                    print('abrindo')
                    abrir_minerio = 1

                if verposicao(mousepos, 980, 65, 240, 157) == 1 and mineriosaw == 3 :
                    print('abrindo')
                    abrir_minerio = 2    
                    
                if abrir_minerio == 1:
                    mineriosaw = 1
                    abrir_minerio = 0

                if abrir_minerio == 2:
                     
                    abrir_minerio = 0

                if mineriosaw == 1:    
                    if verposicao(mousepos, 833, 426, 136, 71) == 1 and opacidadeMinerioMapa > 150:
                        mineriosaw = 3
                        print(mineriosaw)
                    if verposicao(mousepos, 1153, 45, 55, 50) == 1:
                        mineriosaw = 2
                        
                        

                

            
        # Resetar o input a cada 5 segundos
        
        # Movimentação do personagem

        screen.fill(WHITE)
       
        show_image('./imgs/26.png')



        if mineriosaw == 1:
            minerioimg.set_alpha(opacidadeMinerioMapa)
            screen.blit(minerioimg, minerioimg_rect)
            if opacidadeMinerioMapa < 255:
                opacidadeMinerioMapa += 7.5
                print("ta rodando")
                print(opacidadeMenorMapa)
                pygame.time.delay(2)

        minerioimg.set_alpha(opacidadeMinerioMapa)

        if mineriosaw == 2:
            minerioimg.set_alpha(opacidadeMinerioMapa)
            screen.blit(minerioimg, minerioimg_rect)
            if opacidadeMinerioMapa > 0:
                opacidadeMinerioMapa -= 15
                print("ta rodando")

                pygame.time.delay(4)
            if opacidadeMinerioMapa == 0:
                mineriosaw = 0
        

        minerioimg.set_alpha(opacidadeMinerioMapa)



       

       

        if mineriosaw == 3:
            minerioimg.set_alpha(opacidadeMinerioMapa)
            screen.blit(minerioimg, minerioimg_rect)
            if opacidadeMinerioMapa > 0:
                opacidadeMinerioMapa -= 15
                print("ta rodando")
                
                pygame.time.delay(4)
            if opacidadeMinerioMapa == 0:
                break
                

       
        pygame.display.flip()

    thirdphase2_pages()

    
    


def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reinicia o jogo
                    main_menu()
        screen.fill(WHITE)
        draw_text("Game Over!", 64, (255, 0, 0), screen,
                  WIDTH // 2 - 150, HEIGHT // 2 - 100)
        draw_text("Pressione R para Reiniciar", 36, (0, 0, 0),
                  screen, WIDTH // 2 - 150, HEIGHT // 2)
        pygame.display.flip()
    


def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reinicia o jogo
                    main_menu()
        screen.fill(WHITE)
        draw_text("Game Over!", 64, (255, 0, 0), screen,
                  WIDTH // 2 - 150, HEIGHT // 2 - 100)
        draw_text("Pressione R para Reiniciar", 36, (0, 0, 0),
                  screen, WIDTH // 2 - 150, HEIGHT // 2)
        pygame.display.flip()
    


main_menu()

# Iniciar o jogo
main_menu()

