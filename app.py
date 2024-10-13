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
jumping = False
jump_speed = 10
gravity = 0.5
y_velocity = 0

# Variáveis de estado
door_open = False

#Porta
door_rect = pygame.Rect(1350, 650, 90, 160)  # Definindo a porta


# Funções
def resetchar ():
    character_rect.x = 100
    character_rect.y = HEIGHT - 150


def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def show_image(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(image, (0, 0))

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

        screen.fill(WHITE)  # Cor de fundo
        show_image('imgs/fullletterimg.jpg')  # Imagem de fundo do menu
        draw_text("Menu Principal", 64, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2 - 100)
        draw_text("Pressione Enter para Jogar", 36, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2)
        draw_text("Pressione C para Créditos", 36, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2 + 50)
        pygame.display.flip()

def game_pages():
    page_images = [
        'imgs/fullletterimg.jpg',
        'imgs/fullletterimg.jpg',
        'imgs/fullletterimg.jpg',
        'imgs/fullletterimg.jpg',
        'imgs/fullletterimg.jpg',
    ]

    i = 0
    while i < 5:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Avançar para a próxima página
                        i += 1

            if i == 5:
                break
            screen.fill(WHITE)
            show_image(page_images[i])
            draw_text(f"Página {i + 1}", 64, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2)
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
        draw_text("Resolva: {} + {} = ?".format(answer, answer), 48, (0, 0, 0), screen, WIDTH // 2 - 200, HEIGHT // 2 - 50)
        draw_text(user_input, 48, (0, 0, 0), screen, WIDTH // 2 - 100, HEIGHT // 2)
        
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
        draw_text("Digite 'joule':", 48, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        draw_text(user_input, 48, (0, 0, 0), screen, WIDTH // 2 - 100, HEIGHT // 2)
        
        pygame.draw.rect(screen, DOOR_COLOR, door_rect)
        
        screen.blit(character_image, character_rect)  # Desenha o personagem
        pygame.display.flip()
    
        if character_rect.x >= 1350:
            break
    final_game()

def final_game():
    resetchar()
    global door_open
    start_time = time.time()

    while True:
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
            jumping = True
            y_velocity = -jump_speed

        # Lógica do pulo
        if jumping:
            character_rect.y += y_velocity
            y_velocity += gravity
            if character_rect.y >= HEIGHT - 150:  # Quando o personagem atinge o chão
                character_rect.y = HEIGHT - 150
                jumping = False

        current_time = time.time()
        if current_time - start_time > 20:
            break

        screen.fill(WHITE)
        show_image('caminho/para/sua/imagem/final_game_background.jpg')
        screen.blit(character_image, character_rect)  # Desenha o personagem
        draw_text("Jogo Final! 20 segundos para sobreviver!", 48, (0, 0, 0), screen, WIDTH // 2 - 300, HEIGHT // 2 - 50)
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
            draw_text(f"Final Page {i + 1}", 64, (0, 0, 0), screen, WIDTH // 2 - 150, HEIGHT // 2)
            pygame.display.flip()

    main_menu()

# Iniciar o jogo
main_menu()
