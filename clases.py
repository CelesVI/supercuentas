import pygame

class Boton:
    def __init__(self,corXbase,corYbase,corXfin,corYfin,texto,tamanio,color,fuente = None):
        self.fuente = pygame.font.Font(fuente, tamanio)
        self.texto = self.fuente.render(texto,0,color)
        self.xA = corXbase
        self.xB = corXfin
        self.yA = corYbase
        self.yB = corYfin

    def es_presionado(self):
        x = False
        if pygame.mouse.get_pos()[0] in range(self.xA,self.xB) and pygame.mouse.get_pos()[1] in range(self.yA,self.yB):
            x = True
        return x

    def update(self,pantalla):
        pantalla.blit(self.texto,(self.xA,self.yA))

    def set_texto(self,texto,color = (255,255,255)):
        self.texto = self.fuente.render(texto,0,color)
        
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        (self.left,self.top)=pygame.mouse.get_pos()