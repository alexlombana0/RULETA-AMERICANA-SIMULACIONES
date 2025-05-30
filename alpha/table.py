import tkinter as tk
from tkinter import messagebox
import random

# Colores de la ruleta
COLORES = {
    "0": "Verde", "00": "Verde",
    "1": "Rojo", "2": "Negro", "3": "Rojo", "4": "Negro",
    "5": "Rojo", "6": "Negro", "7": "Rojo", "8": "Negro",
    "9": "Rojo", "10": "Negro", "11": "Negro", "12": "Rojo",
    "13": "Negro", "14": "Rojo", "15": "Negro", "16": "Rojo",
    "17": "Negro", "18": "Rojo", "19": "Rojo", "20": "Negro",
    "21": "Rojo", "22": "Negro", "23": "Rojo", "24": "Negro",
    "25": "Rojo", "26": "Negro", "27": "Rojo", "28": "Negro",
    "29": "Negro", "30": "Rojo", "31": "Negro", "32": "Rojo",
    "33": "Negro", "34": "Rojo", "35": "Negro", "36": "Rojo"
}

# Ruleta americana
NUMEROS = [str(n) for n in range(0, 37)] + ["00"]

class Ruleta:
    def __init__(self, master):
        self.master = master
        self.master.title("Ruleta Americana - Dos Jugadores")
        self.master.geometry("1000x600")
        self.saldo = {"Jugador 1": 1000, "Jugador 2": 1000}
        self.apuestas = {"Jugador 1": {}, "Jugador 2": {}}

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.master, text="RUELTA AMERICANA", font=("Arial", 18)).pack()

        self.tablero = tk.Frame(self.master)
        self.tablero.pack()

        self.crear_tablero()

        self.panel_apuestas = tk.Frame(self.master)
        self.panel_apuestas.pack()

        tk.Label(self.panel_apuestas, text="Apuesta Jugador 1:").grid(row=0, column=0)
        self.apuesta1 = tk.Entry(self.panel_apuestas)
        self.apuesta1.grid(row=0, column=1)

        tk.Label(self.panel_apuestas, text="Apuesta Jugador 2:").grid(row=1, column=0)
        self.apuesta2 = tk.Entry(self.panel_apuestas)
        self.apuesta2.grid(row=1, column=1)

        self.girar_btn = tk.Button(self.master, text="GIRAR RULETA", command=self.girar, bg="green", fg="white", font=("Arial", 14))
        self.girar_btn.pack(pady=10)

        self.resultado = tk.Label(self.master, text="", font=("Arial", 16))
        self.resultado.pack()

        self.saldos = tk.Label(self.master, text=f"Saldo J1: {self.saldo['Jugador 1']} | Saldo J2: {self.saldo['Jugador 2']}", font=("Arial", 14))
        self.saldos.pack()

    def crear_tablero(self):
        filas = [
            ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"],
            ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"],
            ["1", "4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"]
        ]

        for r, fila in enumerate(filas):
            for c, num in enumerate(fila):
                color = COLORES[num]
                bg = "red" if color == "Rojo" else "black" if color == "Negro" else "green"
                fg = "white" if bg != "green" else "black"
                tk.Button(self.tablero, text=num, width=4, height=2, bg=bg, fg=fg, command=lambda n=num: self.seleccionar_numero(n)).grid(row=r, column=c)

        # 0 y 00
        tk.Button(self.tablero, text="0", width=4, height=2, bg="green", command=lambda: self.seleccionar_numero("0")).grid(row=0, column=12, rowspan=2)
        tk.Button(self.tablero, text="00", width=4, height=2, bg="green", command=lambda: self.seleccionar_numero("00")).grid(row=2, column=12, rowspan=2)

    def seleccionar_numero(self, numero):
        messagebox.showinfo("Número Seleccionado", f"Seleccionaste: {numero}")

    def girar(self):
        numero = random.choice(NUMEROS)
        color = COLORES.get(numero, "Verde")
        self.resultado.config(text=f"Resultado: {numero} ({color})")

        for jugador, entrada in zip(["Jugador 1", "Jugador 2"], [self.apuesta1, self.apuesta2]):
            apuesta = entrada.get().strip().lower()
            if apuesta == numero or apuesta == color.lower():
                self.saldo[jugador] += 100
                messagebox.showinfo("GANASTE", f"{jugador} ganó la apuesta!")
            else:
                self.saldo[jugador] -= 50
                messagebox.showinfo("PERDISTE", f"{jugador} perdió la apuesta.")

        self.saldos.config(text=f"Saldo J1: {self.saldo['Jugador 1']} | Saldo J2: {self.saldo['Jugador 2']}")

ventana = tk.Tk()
ruleta = Ruleta(ventana)
ventana.mainloop()
