import pygame


class Ficha:
    def __init__(self, valor, imagen_path):
        self.valor = valor
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect()
