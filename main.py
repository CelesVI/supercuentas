import pygame
import random
import pickle
import aftergame
import rankScreen
from clases import Cursor,Boton
from generarProblema import generarProblema

def recibirResultado(resultado):
#recibe "correcto" o "incorrecto" y trabaja las variables de puntajes y tiempo
    tiempoDescontar = 5     #Tiempo a descontar si se gana el bonus
    scoreNormal = 10         #Puntos recibidos por un acierto normal
    scoreRacha = 30          #Puntos recibidos por acertar un bonus
    global rachaActual      #global indica que son variables globales
    global score
    global tiempo
    global tiempoBonus
    global racha
    global fallos
    global maxRacha
    if resultado == "correcto":
        if rachaActual == 3:
            score += scoreRacha
            rachaActual = 0
            tiempo += -tiempoDescontar
            tiempoBonus += tiempoDescontar
        else:
            score += scoreNormal
            rachaActual += 1
        racha += 1
    else:
        if racha > maxRacha:
            maxRacha = racha
        racha = 0
        rachaActual = 0
        fallos += 1



def game():

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    cursor1=Cursor()
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    blanco = (255,255,255)
    musicaCorrecto = pygame.mixer.Sound("sonidos/boton2.wav")
    musicaIncorrecto = pygame.mixer.Sound("sonidos/botonError.wav")
    musicaTiempo = pygame.mixer.Sound("sonidos/musicaTiempo.wav")
    global musica
    global modo
    global tiempo
    global score
    global sonido
    global fallos
    
    datos = generarProblema(modo)
    opciones = [(130,160),(130,330),(430,160),(430,330)]
    
    x = int(random.randrange(0,len(opciones),1))
    tupla1 = opciones[x]
    del opciones[x]
    
    x = int(random.randrange(0,len(opciones),1))
    tupla2 = opciones[x]
    del opciones[x]
    
    x = int(random.randrange(0,len(opciones),1))
    tupla3 = opciones[x]
    del opciones[x]

    x = int(random.randrange(0,len(opciones),1))
    tupla4 = opciones[x]
    del opciones[x]

    problema = Boton(240,70,tupla1[0]+20,tupla1[1]+20,str(datos[1])+" "+datos[3]+" "+str(datos[2]) ,50,(200,50,50))
    boton_1 = Boton(tupla1[0],tupla1[1],tupla1[0]+80,tupla1[1]+30,str(datos[0]),30,blanco,"fuentes/EraserDust.ttf")
    boton_2 = Boton(tupla2[0],tupla2[1],tupla2[0]+80,tupla2[1]+30,str(datos[4]),30,blanco,"fuentes/EraserDust.ttf")
    boton_3 = Boton(tupla3[0],tupla3[1],tupla3[0]+80,tupla3[1]+30,str(datos[5]),30,blanco,"fuentes/EraserDust.ttf")
    boton_4 = Boton(tupla4[0],tupla4[1],tupla4[0]+80,tupla4[1]+30,str(datos[6]),30,blanco,"fuentes/EraserDust.ttf")
    boton_tiempo = Boton(500,10,500,10,"Tiempo: " + str(int(tiempo)),20,blanco,"fuentes/EraserDust.ttf")
    if musica:
        boton_musica = Boton(680,10,760,30,"musica ON",20,(255,0,0),"fuentes/EraserDust.ttf")
    else:
        boton_musica = Boton(680,10,760,30,"musica OFF",20,(255,0,0),"fuentes/EraserDust.ttf")
    boton_titulo = Boton(1,10,0,0,"Supercuentas!",20,(255,200,40),"fuentes/EraserDust.ttf")
    boton_score = Boton(600,560,tupla1[0]+20,tupla1[1]+20,"Puntos: " + str(score),50,(200,50,50))
    boton_volver = Boton(250,500,500,530,"Abandonar partida",30,(255,255,255),"fuentes/EraserDust.ttf")


    if sonido:
        boton_sonido = Boton(680,30,760,50,"sonido ON",20,(255,0,0),"fuentes/EraserDust.ttf")
    else:
        boton_sonido = Boton(680,30,760,50,"sonido OFF",20,(255,0,0),"fuentes/EraserDust.ttf")
    while salir!=True and tiempo > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_1.es_presionado():
                    if sonido:
                        musicaCorrecto.play()
                    recibirResultado("correcto")
                    game()
                    salir = True
                elif boton_2.es_presionado() or boton_3.es_presionado() or boton_4.es_presionado():
                    if sonido :
                        musicaIncorrecto.play()
                    recibirResultado("incorrecto")
                    game()
                    salir = True
                if boton_musica.es_presionado():
                    if musica == True:
                        boton_musica.set_texto("musica OFF",(255,0,0))
                        pygame.mixer.music.stop()
                        musica = False
                    else:
                        boton_musica.set_texto("musica ON",(255,0,0))
                        pygame.mixer.music.play()
                        musica = True
                if boton_sonido.es_presionado():
                    if sonido:
                        sonido = False
                        boton_sonido = Boton(680,30,760,50,"sonido OFF",20,(255,0,0),"fuentes/EraserDust.ttf")
                    else:
                        sonido = True
                        boton_sonido = Boton(680,30,760,50,"sonido ON",20,(255,0,0),"fuentes/EraserDust.ttf")
                if boton_volver.es_presionado():
                    salir = True
        reloj1.tick(15)
        tiempo -= 0.1
        cursor1.update()
        pantalla.fill((30,30,200))
        pantalla.blit(fondo,(0,0))

        if tiempo == 5.00:
            musicaTiempo.play()
        if tiempo > 5:
            boton_tiempo = Boton(500,10,500,10,"Tiempo: " + str(int(tiempo)),20,blanco,"fuentes/EraserDust.ttf")
        else:
            boton_tiempo = Boton(500,10,500,10,"Tiempo: " + str(int(tiempo)),25,(255,30,30),"fuentes/EraserDust.ttf")
        boton_tiempo.update(pantalla)
        boton_1.update(pantalla)
        boton_2.update(pantalla)
        boton_3.update(pantalla)
        boton_4.update(pantalla)
        boton_musica.update(pantalla)
        problema.update(pantalla)
        boton_score.update(pantalla)
        boton_titulo.update(pantalla)
        boton_sonido.update(pantalla)
        boton_volver.update(pantalla)
            
        if not salir:
            pygame.display.update()


def reglas():
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    fuente1=pygame.font.Font("fuentes/EraserDust.ttf", 45)
    fuente2=pygame.font.Font("fuentes/EraserDust.ttf", 20)
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    

    boton_volver = Boton(300,300,400,330,"Volver",30,(255,255,255),"fuentes/EraserDust.ttf")
    texto1=fuente1.render("Reglas",0,(200,200,50))
    texto2=fuente2.render("El juego consiste en resolver cuentas, clickea el resultado correcto",0,(255,255,255))
    texto3=fuente2.render("antes de que acabe el tiempo, Tambien podes conseguir rachas",0,(255,255,255))
    texto4=fuente2.render("acertando 2 o mas resultados. Tenes un minuto!",0,(255,255,255))
    texto5=fuente2.render("",0,(255,255,255))
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
        pantalla.blit(texto1,(130,40))
        pantalla.blit(texto2,(20,150))
        pantalla.blit(texto3,(20,170))
        pantalla.blit(texto4,(20,190))
        pantalla.blit(texto5,(20,210))
        boton_volver.update(pantalla)
        pygame.display.update()
        


def main():

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Supercuentas")
    salir=False
    reloj1=pygame.time.Clock()
    cursor1=Cursor()
    fuente1=pygame.font.Font(None, 48)
    fuente2=pygame.font.Font(None, 24)
    fondo=pygame.image.load("imagenes/blackboard.jpeg")
    pygame.mixer.music.load("sonidos/tema1.mid")
    musica1 = pygame.mixer.Sound("sonidos/boton1.wav")
    blanco = (255,255,255)

    global musica
    global tiempo
    global score
    global modo
    global sonido
    global fallos
    global maxRacha
    global rachaActual

    boton_jugar = Boton(130,130,211,158,"Jugar",30,blanco,"fuentes/EraserDust.ttf")
    boton_reglas = Boton(130,170,228,198,"Reglas",30,blanco,"fuentes/EraserDust.ttf")
    boton_salir = Boton(130,290,200,315,"Salir",30,blanco,"fuentes/EraserDust.ttf")
    boton_rank = Boton(130,250,235,275,"Ranking",30,blanco,"fuentes/EraserDust.ttf")
    if musica:
        boton_musica = Boton(680,10,760,30,"musica ON",20,(255,0,0),"fuentes/EraserDust.ttf")
        pygame.mixer.music.play()
    else:
        boton_musica = Boton(680,10,760,30,"musica OFF",20,(255,0,0),"fuentes/EraserDust.ttf")
        pygame.mixer.music.stop()
    boton_titulo = Boton(100,50,100,50,"Supercuentas!",40,(255,200,0),"fuentes/EraserDust.ttf")
    boton_nivel = Boton(130,210,290,235,"Nivel: Facil",30,blanco,"fuentes/EraserDust.ttf")
    boton_sonido = Boton(680,30,760,50,"sonido ON",20,(255,0,0),"fuentes/EraserDust.ttf")

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.es_presionado():
                    if sonido:
                        musica1.play()
                    score = 0
                    fallos = 0
                    maxRacha = 0
                    racha = 0
                    rachaActual = 0
                    tiempo = 60
                    game()
                    pygame.mixer.music.stop()
                    musica = False
                    aftergame.aftergame(score,max(rachaActual,maxRacha),fallos)
                if boton_reglas.es_presionado():
                    if sonido:
                        musica1.play()
                    reglas()
                if boton_rank.es_presionado():
                    if sonido:
                        musica1.play()
                    rankScreen.rankScreen()
                if boton_salir.es_presionado():
                    musica1.play()
                    salir = True
                if boton_musica.es_presionado():
                    if sonido:
                        musica1.play()
                    if musica == True:
                        pygame.mixer.music.stop()
                        musica = False
                    else:
                        pygame.mixer.music.play()
                        musica = True
                if boton_nivel.es_presionado():
                    if sonido:
                        musica1.play()
                    if modo == "facil":
                        modo = "normal"
                        boton_nivel = Boton(130,210,330,235,"Nivel: Normal",30,blanco,"fuentes/EraserDust.ttf")
                    elif modo == "normal":
                        modo = "dificil"
                        boton_nivel = Boton(130,210,330,235,"Nivel: Dificil",30,blanco,"fuentes/EraserDust.ttf")
                    elif modo == "dificil":
                        modo = "facil"
                        boton_nivel = Boton(130,210,290,235,"Nivel: Facil",30,blanco,"fuentes/EraserDust.ttf")
                if boton_sonido.es_presionado():
                    if sonido:
                        musica1.play()
                    if sonido:
                        sonido = False
                        boton_sonido = Boton(680,30,760,50,"sonido OFF",20,(255,0,0),"fuentes/EraserDust.ttf")
                    else:
                        sonido = True
                        boton_sonido = Boton(680,30,760,50,"sonido ON",20,(255,0,0),"fuentes/EraserDust.ttf")
        reloj1.tick(15)
        cursor1.update()
        pantalla.fill((30,30,200))
        pantalla.blit(fondo,(0,0))

        if not musica:
            boton_musica.set_texto("musica OFF",(255,0,0))
        else:
            boton_musica.set_texto("musica ON",(255,0,0))
            
        boton_sonido.update(pantalla)
        boton_nivel.update(pantalla)
        boton_jugar.update(pantalla)
        boton_reglas.update(pantalla)
        boton_salir.update(pantalla)
        boton_musica.update(pantalla)
        boton_titulo.update(pantalla)
        boton_rank.update(pantalla)

        pygame.display.update()

    pygame.quit()




modo = "facil"
sonido = True
musica = False
rachaActual = 0
score = 0
tiempo = 0
tiempoBonus = 0
racha = 0
fallos = 0
maxRacha = 0
main()




