class Jugador:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def actualizar_saldo(self, cantidad):
        self.saldo += cantidad
