import pygame
import sys
import random
import time

# Inicialização do Pygame
pygame.init()

# Resolução
WIDTH, HEIGHT = 1440, 810
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo em Pygame")

# Cores
WHITE = (255, 255, 255)
DOOR_COLOR = (0, 255, 0)  # Cor da porta (verde)

# Configurações do Personagem
character_image = pygame.image.load('imgs/gojo.png')
character_rect = character_image.get_rect()
character_rect.x = 100
character_rect.y = HEIGHT - 150  # Ajuste para a altura do chão
jumping = 0
jump_start_time = 0
jump_duration = 0.5  # Duração do pulo em segundos
jump_height = 20  # Altura máxima do pulo
jump_speed = 20
gravity = 2.8
y_velocity = 0

# Variáveis de estado
door_open = False

# Porta
door_rect = pygame.Rect(1350, 650, 90, 160)  # Definindo a porta


obstacle_image = pygame.image.load('imgs/arvore].png')
obstacle_image = pygame.transform.scale(obstacle_image, [50, 100])
obstacles = []
obstacle_speed = 5

# Funções


def resetchar():
    character_rect.x = 100
    character_rect.y = HEIGHT - 150

def verposicao (mouse , x , y , w , h):
    if x < mouse[0] < (x + w) and y < mouse[1] < y + h:
        return 1
    else:
        return 0

def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


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
                    if verposicao (mousepos , 575 , 450 , 300  , 100) == 1:
                        main_menu()
                    


        screen.fill(WHITE)  # Cor de fundo
        show_image('imgs/fullletterimg.jpg')  # Imagem de fundo do menu

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
                    credits()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    print(mousepos)
                    if verposicao (mousepos , 575 , 450 , 300  , 100) == 1:
                        game_pages()
                    elif verposicao (mousepos , 75 , 613 , 184  , 124) == 1:
                        creds()


        screen.fill(WHITE)  # Cor de fundo
        show_image('imgs/menu.jpg')  # Imagem de fundo do menu

        pygame.display.flip()


def game_pages():
    page_images = [
        'imgs/pagone.jpg',
        'imgs/pagtwo.jpg',
        'imgs/pagthree.jpg',
        'imgs/pagfour.jpg',
        'imgs/pagfive.jpg',
        'imgs/pagsix.jpg',
        'imgs/pagseven.jpg',
        'imgs/pageight.jpg'
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
                    if verposicao (mousepos , 1260 , 650 , 130  , 100) == 1:
                        i += 1

                if i >= 1 :
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        print(mousepos)
                        if verposicao (mousepos , 70 , 650 , 130  , 100) == 1:
                            i -= 1


                       


            if i == 7:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            pygame.display.flip()

    first_level()


def first_level():
    global door_open
    answer = random.randint(1, 10) + random.randint(1, 10)
    user_input = ""
    input_timer = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit() and int(user_input) == answer:
                        door_open = True  # Porta liberada
                        break
                    else:
                        user_input = ""
                elif event.unicode.isprintable():
                    user_input += event.unicode.lower()

        # Movimentação do personagem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            character_rect.x += 5

        # Resetar o input a cada 5 segundos
        if time.time() - input_timer > 5:
            user_input = ""
            input_timer = time.time()

        screen.fill(WHITE)
        show_image('imgs/fullletterimg.jpg')
        draw_text("Resolva: {} + {} = ?".format(answer, answer), 48,
                  (0, 0, 0), screen, WIDTH // 2 - 200, HEIGHT // 2 - 50)
        draw_text(user_input, 48, (0, 0, 0), screen,
                  WIDTH // 2 - 100, HEIGHT // 2)

        # Desenha a porta
        pygame.draw.rect(screen, DOOR_COLOR, door_rect)

        screen.blit(character_image, character_rect)  # Desenha o personagem
        pygame.display.flip()

        if character_rect.x >= 1350:
            break

    second_level()


def second_level():
    resetchar()
    global door_open
    user_input = ""
    input_timer = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input == "joule":
                        door_open = True  # Porta liberada
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            character_rect.x += 5

        screen.fill(WHITE)
        show_image('imgs/fullletterimg.jpg')
        draw_text("Digite 'joule':", 48, (0, 0, 0), screen,
                  WIDTH // 2 - 150, HEIGHT // 2 - 50)
        draw_text(user_input, 48, (0, 0, 0), screen,
                  WIDTH // 2 - 100, HEIGHT // 2)

        pygame.draw.rect(screen, DOOR_COLOR, door_rect)

        screen.blit(character_image, character_rect)  # Desenha o personagem
        pygame.display.flip()

        if character_rect.x >= 1350:
            break
    final_game()


def final_game():
    resetchar()
    global door_open
    global jumping
    start_time = time.time()
    obstacle_timer = time.time()

    while True:

        if time.time() - obstacle_timer > 2:
            new_obstacle = obstacle_image.get_rect()
            new_obstacle.x = WIDTH
            new_obstacle.y = HEIGHT - 100  # Mesma altura do personagem
            obstacles.append(new_obstacle)
            obstacle_timer = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação do personagem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            character_rect.x += 5
        if keys[pygame.K_UP] and not jumping:  # Pular
            jumping = 1
            jump_start_time = time.time()
            y_velocity = -jump_height / (jump_duration / 2)
            y_velocity = -jump_speed

        # Lógica do pulo
        if jumping == 1:
            elapsed_time = time.time() - jump_start_time
            if elapsed_time < jump_duration:
                character_rect.y += y_velocity
                # Atualiza a velocidade
                y_velocity += gravity * (jump_duration / 60)
            else:
                jumping = 0
                character_rect.y = HEIGHT - 150  # Coloca o personagem de volta ao chão

        current_time = time.time()
        if current_time - start_time > 20:
            break

        for obstacle in obstacles[:]:
            obstacle.x -= obstacle_speed
            # Remove o obstáculo se sair da tela
            if obstacle.x < -obstacle.width:
                obstacles.remove(obstacle)

            # Verifica colisão
            if character_rect.colliderect(obstacle):
                game_over()  # Chama a função de game over

        screen.fill(WHITE)
        show_image('imgs/fullletterimg.jpg')
        screen.blit(character_image, character_rect)  # Desenha o personagem
        for obstacle in obstacles:
            screen.blit(obstacle_image, obstacle)  # Desenha os obstáculos

        draw_text("Jogo Final! 20 segundos para sobreviver!", 48,
                  (0, 0, 0), screen, WIDTH // 2 - 300, HEIGHT // 2 - 50)
        pygame.display.flip()

    final_pages()


def final_pages():
    for i in range(5):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Avançar para a próxima página
                        break

            screen.fill(WHITE)
            show_image(f'caminho/para/sua/imagem/final_page_{i + 1}.jpg')
            draw_text(f"Final Page {i + 1}", 64, (0, 0, 0),
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
