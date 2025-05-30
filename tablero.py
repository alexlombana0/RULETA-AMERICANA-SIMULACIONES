import pygame


class Tablero:
    def __init__(self, jugador, posicion):
        self.jugador = jugador
        self.posicion = posicion
        self.apuestas = []  # [(tipo, valor, monto)]
        self.apuestas_previas = []

    def dibujar(self, pantalla):
        fuente = pygame.font.SysFont("Arial", 20)
        pygame.draw.rect(pantalla, (0, 0, 0), (*self.posicion, 500, 200), 2)
        pantalla.blit(
            fuente.render(f"Apuestas de {self.jugador.nombre}", True, (255, 255, 255)),
            (self.posicion[0] + 10, self.posicion[1] - 30),
        )
        y_offset = 0
        for tipo, valor, monto in self.apuestas:
            texto = f"{tipo} {valor}: {monto}"
            pantalla.blit(
                fuente.render(texto, True, (255, 255, 255)),
                (self.posicion[0] + 10, self.posicion[1] + y_offset),
            )
            y_offset += 20

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if (
                self.posicion[0] < x < self.posicion[0] + 500
                and self.posicion[1] < y < self.posicion[1] + 200
            ):
                self.apuestas.append(("pleno", "17", 50))  # Ejemplo fijo

    def resolver_apuestas(self, numero, color):
        pagos = {"pleno": 35, "rojo/negro": 1, "par/impar": 1, "alto/bajo": 1}
        for tipo, valor, monto in self.apuestas:
            acierto = False
            if tipo == "pleno" and valor == numero:
                acierto = True
            elif tipo == "rojo/negro" and valor == color.lower():
                acierto = True
            if acierto:
                self.jugador.actualizar_saldo(monto * pagos[tipo])
            else:
                self.jugador.actualizar_saldo(-monto)
        self.apuestas_previas = self.apuestas.copy()
        self.apuestas.clear()

    def limpiar_apuestas(self):
        self.apuestas.clear()

    def repetir_apuestas(self):
        self.apuestas = self.apuestas_previas.copy()
