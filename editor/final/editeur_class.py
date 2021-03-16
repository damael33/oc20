from editeur_variables import *

class Shapes:
    def __init__(self, rect_shape, form, color=RECT_COLOR, width=RECT_WIDTH):
        self.rect_shape = rect_shape
        self.color = color
        self.width = width
        self.form = form
        
    def draw(self):
        if self.form == 'rectangle':
            pygame.draw.rect(screen, self.color, self.rect_shape, self.width)
        elif self.form == 'ellipse':
            pygame.draw.ellipse(screen, self.color, self.rect_shape, self.width)
    
    def edit_width(self, event):
        self.width = key_dict_RECT_WIDTH[event.key]
        
    def edit_color(self, event):
        self.color = key_dict_RECT_COLOR[event.key]
        
    def do_event(self, event):
        if event.type == KEYDOWN:
            if event.key in key_dict_RECT_WIDTH:
                self.edit_width(event)   
            if event.key in key_dict_RECT_COLOR:
                self.edit_color(event)


class Images:
    def __init__(self, nom):
        self.nom = nom
        self.image = None
        self.rect_img = None
        self.center = (800/2, 600/2)
        self.scale = 1
        self.angle = 0
        #self.load()
        
    def load(self):
        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)
        path = os.path.join(path, self.nom)
        self.image = pygame.image.load(self.nom)
        self.image.convert()
        self.rect_img = self.image.get_rect()
        self.rect_img.center = self.center

    def flip_h(self):
        self.image = pygame.transform.flip(self.image, True, False)
                    
    def flip_v(self):
        self.image = pygame.transform.flip(self.image, False, True)

    def edit_angle(self):
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect_img = self.image.get_rect()
    
    def edit_scale(self):
        self.image = pygame.transform.rotozoom(self.image, self.angle, self.scale)
        self.rect_img = self.image.get_rect()
        
    def do_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_h:
                self.flip_v()
            elif event.key == K_v:
                self.flip_h()
 
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    self.scale /= 1.1
                    self.edit_scale()
                else:
                    self.scale *= 1.1
                    self.edit_scale()
                    
            elif event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    self.angle -= 10
                    self.edit_angle()
                else:
                    self.angle += 10
                    self.edit_angle()
                    

def Help():
    screen.blit(helpPNG, (0, 0))
    