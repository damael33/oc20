import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

pygame.init()
w, h = 640, 640
screen = pygame.display.set_mode((w, h))
running = True

img0 = pygame.image.load('img/bird.png')
img0.convert()

# draw a green border around img0
rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

img = img0
rect = img.get_rect()
rect.center = w//2, h//2
moving = False

angle = 0
scale = 0

mouse = pygame.mouse.get_pos()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
                
        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            
    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()
    
pygame.quit()