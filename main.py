import pygame
import sys
from ruleta import Ruleta
from jugador import Jugador
from tablero import Tablero

pygame.init()

ANCHO, ALTO = 1200, 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ruleta Americana - Dos Jugadores")

ruleta = Ruleta()
jugador1 = Jugador("Jugador 1", 1000)
jugador2 = Jugador("Jugador 2", 1000)
tablero1 = Tablero(jugador1, posicion=(50, 400))
tablero2 = Tablero(jugador2, posicion=(650, 400))

boton_girar = pygame.Rect(1050, 100, 120, 40)
boton_limpiar = pygame.Rect(1050, 160, 120, 40)
boton_repetir = pygame.Rect(1050, 220, 120, 40)
boton_salir = pygame.Rect(1050, 280, 120, 40)

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    pantalla.fill((34, 139, 34))

    ruleta.dibujar(pantalla)
    tablero1.dibujar(pantalla)
    tablero2.dibujar(pantalla)

    pygame.draw.rect(pantalla, (0, 0, 0), boton_girar)
    pygame.draw.rect(pantalla, (0, 0, 0), boton_limpiar)
    pygame.draw.rect(pantalla, (0, 0, 0), boton_repetir)
    pygame.draw.rect(pantalla, (0, 0, 0), boton_salir)

    fuente = pygame.font.SysFont("Arial", 20)
    pantalla.blit(
        fuente.render("GIRAR", True, (255, 255, 255)),
        (boton_girar.x + 30, boton_girar.y + 10),
    )
    pantalla.blit(
        fuente.render("LIMPIAR", True, (255, 255, 255)),
        (boton_limpiar.x + 20, boton_limpiar.y + 10),
    )
    pantalla.blit(
        fuente.render("REPETIR", True, (255, 255, 255)),
        (boton_repetir.x + 20, boton_repetir.y + 10),
    )
    pantalla.blit(
        fuente.render("SALIR", True, (255, 255, 255)),
        (boton_salir.x + 40, boton_salir.y + 10),
    )

    saldo1 = fuente.render(f"Saldo J1: {jugador1.saldo}", True, (255, 255, 255))
    saldo2 = fuente.render(f"Saldo J2: {jugador2.saldo}", True, (255, 255, 255))
    pantalla.blit(saldo1, (50, 50))
    pantalla.blit(saldo2, (650, 50))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_girar.collidepoint(evento.pos):
                numero, color = ruleta.girar()
                tablero1.resolver_apuestas(numero, color)
                tablero2.resolver_apuestas(numero, color)
            elif boton_limpiar.collidepoint(evento.pos):
                tablero1.limpiar_apuestas()
                tablero2.limpiar_apuestas()
            elif boton_repetir.collidepoint(evento.pos):
                tablero1.repetir_apuestas()
                tablero2.repetir_apuestas()
            elif boton_salir.collidepoint(evento.pos):
                ejecutando = False
            else:
                tablero1.manejar_evento(evento)
                tablero2.manejar_evento(evento)
        else:
            tablero1.manejar_evento(evento)
            tablero2.manejar_evento(evento)
            ruleta.manejar_evento(evento, [tablero1, tablero2])

    ruleta.actualizar()
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
