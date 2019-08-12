import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def leer_tecla():
  while True:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def mostrar_caja(pantalla, mensaje):
#muestra una caja en el medio de la pantalla
  fuente1 = pygame.font.Font("fuentes/EraserDust.ttf",18)
  pygame.draw.rect(pantalla, (0,0,0),
                   ((pantalla.get_width() / 2) - 100,
                    (pantalla.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(pantalla, (255,255,255),
                   ((pantalla.get_width() / 2) - 102,
                    (pantalla.get_height() / 2) - 12,
                    204,24), 1)
  if len(mensaje) != 0:
    pantalla.blit(fuente1.render(mensaje, 1, (255,255,255)),
                ((pantalla.get_width() / 2) - 100, (pantalla.get_height() / 2) - 10))
  pygame.display.flip()

def preguntar(pantalla, pregunta):
#preguntar(pantalla, pregunta) -> respuesta
  pygame.font.init()
  string_actual = []
  mostrar_caja(pantalla, pregunta + ": " + string.join(string_actual,""))
  while 1:
    tecla_leida = leer_tecla()
    if tecla_leida == K_BACKSPACE:
      string_actual = string_actual[0:-1]
    elif tecla_leida == K_RETURN:
      break
    elif tecla_leida == K_MINUS:
      string_actual.append("_")
    elif tecla_leida <= 127:
      string_actual.append(chr(tecla_leida))
    mostrar_caja(pantalla, pregunta + ": " + string.join(string_actual,""))
  return string.join(string_actual,"")




