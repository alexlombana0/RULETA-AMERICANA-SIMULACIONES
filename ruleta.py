import pygame
import random


class Ruleta:
    def __init__(self):
        self.numeros = [str(n) for n in range(0, 37)] + ["00"]
        self.colores = {str(n): "Rojo" if n % 2 else "Negro" for n in range(1, 37)}
        self.colores.update({"0": "Verde", "00": "Verde"})
        self.angulo = 0
        self.resultado = None
        self.img = pygame.Surface((300, 300), pygame.SRCALPHA)
        pygame.draw.circle(self.img, (160, 82, 45), (150, 150), 150)

    def girar(self):
        self.resultado = random.choice(self.numeros)
        return self.resultado, self.colores.get(self.resultado, "Verde")

    def dibujar(self, pantalla):
        rotada = pygame.transform.rotate(self.img, self.angulo)
        rect = rotada.get_rect(center=(600, 250))
        pantalla.blit(rotada, rect.topleft)

    def actualizar(self):
        self.angulo = (self.angulo + 2) % 360

    def manejar_evento(self, evento, tableros):
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            numero, color = self.girar()
            for tablero in tableros:
                tablero.resolver_apuestas(numero, color)
