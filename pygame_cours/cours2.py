import pygame

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GRAY

pygame.init()
screen = pygame.display.set_mode((640, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    pygame.draw.rect(screen, RED, (50, 20, 120, 100))
    pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
    pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))

    pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
    pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
    pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)
    pygame.display.update()
    
    
pygame.quit()
