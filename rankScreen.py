from clases import Cursor,Boton
import ranking
import pygame

def rankScreen():
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    fuente1=pygame.font.Font("fuentes/EraserDust.ttf", 30)
    fuente2=pygame.font.Font("fuentes/EraserDust.ttf", 20)
    boton_volver = Boton(300,500,400,530,"Volver",30,(255,255,255),"fuentes/EraserDust.ttf")
    boton_titulo = Boton(130,20,211,158,"Ranking",45,(200,200,50),"fuentes/EraserDust.ttf")
    rank = ranking.get_Ranking()
    rank.reverse()
    y = 0
    listaBotones = []
    for x in rank:
        listaBotones.append(Boton(100,100+y,100,50+y,x[0],30,(255,255,255),"fuentes/EraserDust.ttf"))
        y+=30
    y = 0
    for x in rank:
        listaBotones.append(Boton(500,100+y,100,50+y,str(x[1]),30,(255,255,255),"fuentes/EraserDust.ttf"))
        y+=30

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
        boton_volver.update(pantalla)
        boton_titulo.update(pantalla)
        for x in listaBotones:
            x.update(pantalla)
        pygame.display.update()

