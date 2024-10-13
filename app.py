import pygame
import pyautogui

pygame.init()




display = pygame.display.set_mode([840,480])
pygame.display.set_caption("Castellan")

drawGroup = pygame.sprite.Group()

letter = pygame.sprite.Sprite(drawGroup)
letter.image = pygame.image.load("imgs/fullletterimg.jpg")
letter.image = pygame.transform.scale(letter.image, [288,404])
letter.rect = pygame.Rect(276,20,300,450)



def draw():
    display.fill([0 , 255 , 0])
gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    keys = pygame.key.get_pressed()
    
    display.fill([0,255,0])

    drawGroup.draw(display)
                           #x   y   w   h
    #question = pygame.Rect(370,100,100,100)

    

    



    


    
    pygame.display.update()


