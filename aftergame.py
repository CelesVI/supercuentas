import pygame
import ranking
import rankScreen
import preguntarNombre
from clases import Cursor,Boton

def aftergame(score,racha,fallos):
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    fuente1=pygame.font.Font("fuentes/EraserDust.ttf", 30)
    fuente2=pygame.font.Font("fuentes/EraserDust.ttf", 20)
    boton_volver = Boton(300,300,400,330,"Volver",30,(255,255,255),"fuentes/EraserDust.ttf")
    nombre = preguntarNombre.preguntar(pantalla,"Nombre ")
    if ranking.updateRanking(nombre,score):
        texto1=fuente1.render("WOW Nuevo record!",0,(200,255,200))
    elif fallos < score/10 + racha:
        texto1=fuente1.render("Buen trabajo!",0,(200,255,200))
    elif fallos == 0 and score == 0:
        texto1=fuente1.render("Zzzzzzz..",0,(200,255,200))
    elif fallos == score/10 + racha:
        texto1=fuente1.render("Solo un poco mas de practica!",0,(200,255,200))
    else:
        texto1=fuente1.render("Que horror!",0,(200,255,200))
    texto2=fuente2.render("Tu puntaje es " + str(score) + " tu maxima racha fue de " + str(racha) + " aciertos, Fallos: " + str(fallos),0,(255,230,230))
    

    
    

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.es_presionado():
                    salir = True


        reloj1.tick(15)
        
        pantalla.fill((30,30,200))
        pantalla.blit(fondo,(0,0))
        pantalla.blit(texto1,(240,50))
        pantalla.blit(texto2,(20,150))
        boton_volver.update(pantalla)
        pygame.display.update()
