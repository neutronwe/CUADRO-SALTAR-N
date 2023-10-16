import pygame
 
 
# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
NARANJA = (255, 189, 89)
  
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("CUADRO SALTARIN")
  
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
 
  
# Se usa para establecer cuan rápido se actualiza la pantalla
 
reloj = pygame.time.Clock()

rect_x = 50

# Posición de partida del rectángulo
rect_x = 50
rect_y = 50
# Velocidad y rumbo del rectángulo
rect_cambio_x = 5
rect_cambio_y = 5
if rect_y > 450:
 rect_cambio_y = rect_cambio_y * -1
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(AZUL)
    pygame.draw.rect(pantalla, NARANJA, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(pantalla, BLANCO, [rect_x + 6, rect_y + 8 , 15, 15])
    pygame.draw.rect(pantalla, BLANCO, [rect_x + 28, rect_y + 8 , 15, 15])
    pygame.draw.rect(pantalla, NEGRO, [rect_x + 17, rect_y + 29 , 15, 5])
    pygame.draw.rect(pantalla, NEGRO, [rect_x + 12, rect_y + 16 , 3, 3])
    pygame.draw.rect(pantalla, NEGRO, [rect_x + 34, rect_y + 16, 3, 3])
    # Desplaza el punto de partida del rectángulo       
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y
    # Rebota el rectángulo si es necesario
    # Rebota al rectángulo si es necesario
    if rect_y > 450 or rect_y < 0:
       rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
       rect_cambio_x = rect_cambio_x * -1
    
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()