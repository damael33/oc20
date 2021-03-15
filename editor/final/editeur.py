from editeur_class import *

pygame.init()


img.load()
img_list.append(img)
#boucle editeur
running = True
while running:

    screen.fill(ScreenBackground)
        
    for event in pygame.event.get():
        #exit
        if event.type == QUIT:
            running = False
        #change de mode d'édition
        if event.type == KEYDOWN:
            if event.key in key_dict1:
                if event.mod & KMOD_SHIFT:
                    forme = 'move ' + key_dict1[event.key]
                    
                else:
                    forme = key_dict1[event.key]
           
        #dessine et édite les rectangles
        if forme == 'rectangle':
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Shapes(Rect(start, size), forme, RECT_COLOR, RECT_WIDTH)
                rect_list.append(rect)
                drawing = False
                
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                
            if len(rect_list) > 0:
                rect_list[-1].do_event(event)
            
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    rect_list.pop(-1)
        #dessine et édite les ellipses
        if forme == 'ellipse':
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Shapes(Rect(start, size), forme, RECT_COLOR, RECT_WIDTH)
                rect_list.append(rect)
                drawing = False
                
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                
            if len(rect_list) > 0:
                rect_list[-1].do_event(event)
            
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    rect_list.pop(-1)
                    
        #dessine et édite un polygone
        if forme == 'polygone':
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()

            elif event.type == MOUSEBUTTONDOWN:
                points.append(event.pos)
                drawing = True

            elif event.type == MOUSEBUTTONUP:
                drawing = False

            elif event.type == MOUSEMOTION and drawing:
                points[-1] = event.pos

            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_WIDTH:
                    POLYGON_WIDTH = key_dict_POLYGON_WIDTH[event.key]
            
            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_COLOR:
                    POLYGON_COLOR = key_dict_POLYGON_COLOR[event.key]

        #édite l'image
        if forme == 'image':
            img_list[-1].do_event(event)
    
        #déplace l'image
        if forme == 'move image':
            if event.type == MOUSEBUTTONDOWN:
                if img.rect_img.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                img.rect_img.move_ip(event.rel)

        #déplace les rectangles
        if forme == 'move rectangle':
            if event.type == MOUSEBUTTONDOWN:
                if rect.rect_shape.collidepoint(event.pos):
                    moving = True
                    

            elif event.type == MOUSEBUTTONUP:
                moving = False
                

            elif event.type == MOUSEMOTION and moving:
                rect.rect_shape.move_ip(event.rel)
                
        #déplace les ellipses      
        if forme == 'move ellipse':       
            if event.type == MOUSEBUTTONDOWN:
                if rect.rect_shape.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                rect.rect_shape.move_ip(event.rel)
                       
        #déplace le polygone      
        if forme == 'move polygone':         
            if event.type == MOUSEBUTTONDOWN:
                if rect_poly.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                rect_poly.move_ip(event.rel)
 
    #affiche les formes
    for img in img_list:
        screen.blit(img.image, img.rect_img)
        pygame.draw.rect(screen, RED, img.rect_img, 1)
    
    for rect in rect_list:
        rect.draw()
  
    if len(points)>1:
        rect_poly = pygame.draw.lines(screen, POLYGON_COLOR, True, points, POLYGON_WIDTH)
    
    #affiche l'aide aux commandes
    if pygame.key.get_pressed() [pygame.K_a] == True:
        Help()

    pygame.display.update()
    
pygame.quit()