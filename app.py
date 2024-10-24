import pygame
import sys
import random
import time
from pygame.locals import *



from pygame.sprite import Group

# Inicialização do Pygame
pygame.init()

# Resolução
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Castellan")

# Cores
WHITE = (255, 255, 255)
DOOR_COLOR = (0, 255, 0)  # Cor da porta (verde)


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
            self.rect.x += 18
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


# configs da carta / livro ( OBS : Somente ilustração )
letter_image = pygame.image.load('./imgs/fullletterimg.jpg')
letter_image = pygame.transform.scale(letter_image, [360, 640])

letter_rect = letter_image.get_rect()

letter_rect.x = 500
letter_rect.y = HEIGHT - 725
# variáveis de estado

#porta abrir para liberar a próxima fase (por enquanto não funciona)
door_open = False
door_open2 = False
#transição - carta
opacidade = 0
aumentando_opacidade = False

#andar
isWing = False

#carta necessária pra primeirafase:
lettersaw = False
# porta
door_rect = pygame.Rect(1350, 650, 90, 160)  # Definindo a porta

#projeto da terceira fase
obstacle_image = pygame.image.load('./imgs/arvore].png')
obstacle_image = pygame.transform.scale(obstacle_image, [50, 100])
obstacles = []
obstacle_speed = 5

# Funções


def opacity(aumentar_opacidade, opacidade, imagem, posimage):
    # Aumenta a opacidade se estiver no modo de transição
    if aumentar_opacidade and opacidade < 255:
        opacidade += 5  # Aumenta a opacidade gradualmente
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

        screen.blit(letter_image, [500, 725])


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
secondphaseimageimage = pygame.transform.scale(secondphaseimage, (700, 800))


def show_image(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(image, (0, 0))


def creds():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                if verposicao(mousepos, 73, 620, 130, 100) == 1:
                    main_menu()

        screen.fill(WHITE)  # Cor de fundo
        show_image('./imgs/credsimg.jpg')  # Imagem de fundo do menu

        pygame.display.flip()


def main_menu():
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
                    game_pages()
                elif verposicao(mousepos, 73, 626, 130, 100) == 1:
                    creds()

        screen.fill(WHITE)  # Cor de fundo
        show_image('./imgs/menu.jpg')  # Imagem de fundo do menu

        pygame.display.flip()


def verificar_input(texto, a):
    global p
    if texto == a:
        p = True
        return 1


def game_pages():
    page_images = [
        './imgs/pagone.jpg',
        './imgs/pagtwo.jpg',
        './imgs/pagthree.jpg',
        './imgs/pagfour.jpg',
        './imgs/pagfive.jpg',
        './imgs/pagsix.jpg',
        './imgs/pagseven.jpg',
        './imgs/pageight.jpg'
    ]

    i = 0
    while i < 7:
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

            if i == 7:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    first_level()


def first_level():
    castellanm.resetchar2()
    global door_open
    global isWing
    answer = random.randint(1, 10) + random.randint(1, 10)
    user_input = ""
    user_input = user_input.lower()
    input_timer = time.time()
    lettersaw = 0
    global aumentando_opacidade
    global opacidade
    teclas_presse = []

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
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                if verposicao(mousepos, 575, 450, 600, 300) == 1:
                    openlettero = 1
                    if openlettero == 1:
                        lettersaw = 1
                if lettersaw == True:
                    if verposicao(mousepos, 780, 103, 60, 45) == 1:
                        lettersaw = 2

        # Movimentação do personagem(Sem uso até então)
        keys = pygame.key.get_pressed()

        # Resetar o input a cada 5 segundos
        if time.time() - input_timer > 5:
            user_input = ""
            input_timer = time.time()

        screen.fill(WHITE)
        show_image('./imgs/firstfasepage.jpg')

        if lettersaw == 1:
            letter_image.set_alpha(opacidade)
            screen.blit(letter_image, letter_rect)
            if opacidade < 255:
                opacidade += 3
                print("ta rodando")

                pygame.time.delay(20)

        letter_image.set_alpha(opacidade)

        if lettersaw == 2:
            letter_image.set_alpha(opacidade)
            screen.blit(letter_image, letter_rect)
            if opacidade > 0:
                opacidade -= 3
                print("ta rodando")

                pygame.time.delay(20)

        letter_image.set_alpha(opacidade)

        # Desenha a imagem com a opacidade ajustada

        # Desenha a porta
        pygame.draw.rect(screen, DOOR_COLOR, door_rect)

        movementocastellan.draw(screen)
        movementocastellan.update()
        pygame.display.flip()

        pygame.time.delay(30)
        if castellanm.atualpos() >= 1350 and door_open == True :

            break

    second_level()


def second_level():
    global aumentando_opacidade
    diminuindoopacidade = 0
    opacidadesecond = 255
    global door_open2
    global isWing
    user_input = ""
    input_timer = time.time()
    door_open = False
    print(door_open)
    castellanm.resetchar2()
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input == "joule":
                        door_open2 = True  # Porta liberada
                        print(door_open2, "acertou")
                        break
                    else:
                        user_input = ""
                elif event.unicode.isprintable():
                    user_input += event.unicode.lower()

        # Resetar o input a cada 5 segundos
        if time.time() - input_timer > 5:
            user_input = ""
            input_timer = time.time()

        # Movimentação do personagem

        screen.fill(WHITE)
        if castellanm.atualpos() >= 1350 and door_open2 == True:
            audiotransition2.play(0)
            castellanm.movetofar()
            secondphaseimage.set_alpha(opacidadesecond)
            screen.blit(secondphaseimage, (0, 0))
            if opacidadesecond > 0:
                opacidadesecond -= 1.5
                print("ta rodando")
                screen.set_alpha(opacidadesecond)
                pygame.time.delay(15)
            if opacidadesecond <= 0:
                break
        else:
            show_image('./imgs/pagsix.jpg')

        screen.set_alpha(opacidadesecond)

        pygame.draw.rect(screen, DOOR_COLOR, door_rect)

        movementocastellan.draw(screen)
        movementocastellan.update()
        pygame.display.flip()

    game_over()


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


# fase final em desenvolvimento