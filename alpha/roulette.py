import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta Americana - Dos Jugadores")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BACKGROUND = (34, 139, 34)

# Fuente
font = pygame.font.SysFont("Arial", 24)

# Rueda de ruleta básica
ruleta_img = pygame.Surface((300, 300), pygame.SRCALPHA)
pygame.draw.circle(ruleta_img, (160, 82, 45), (150, 150), 150)
for i in range(38):  # 0-36 + 00
    ang = i * 360 / 38
    x = 150 + 140 * pygame.math.Vector2(1, 0).rotate(ang).x
    y = 150 + 140 * pygame.math.Vector2(1, 0).rotate(ang).y
    pygame.draw.circle(ruleta_img, WHITE if i % 2 == 0 else RED, (int(x), int(y)), 8)

# Jugadores
players = {"Jugador 1": {"saldo": 1000, "apuestas": []},
           "Jugador 2": {"saldo": 1000, "apuestas": []}}

# Ruleta (números y colores)
NUMEROS = [str(n) for n in range(0, 37)] + ["00"]
COLORES = {str(n): "Rojo" if n % 2 else "Negro" for n in range(1, 37)}
COLORES.update({"0": "Verde", "00": "Verde"})

# Variables de animación
angle = 0
clock = pygame.time.Clock()

# Función para girar la ruleta
def girar_ruleta():
    resultado = random.choice(NUMEROS)
    color = COLORES.get(resultado, "Verde")
    print(f"Resultado: {resultado} ({color})")
    return resultado, color

# Loop principal
running = True
while running:
    screen.fill(BACKGROUND)

    # Dibujar la ruleta
    rotated_ruleta = pygame.transform.rotate(ruleta_img, angle)
    rect = rotated_ruleta.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(rotated_ruleta, rect.topleft)

    # Saldos
    text1 = font.render(f"Jugador 1 Saldo: {players['Jugador 1']['saldo']}", True, WHITE)
    text2 = font.render(f"Jugador 2 Saldo: {players['Jugador 2']['saldo']}", True, WHITE)
    screen.blit(text1, (50, HEIGHT - 100))
    screen.blit(text2, (50, HEIGHT - 70))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                resultado, color = girar_ruleta()

    # Animación de giro
    angle = (angle + 2) % 360

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()