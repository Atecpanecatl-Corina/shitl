import tkinter as tk
from tkinter import messagebox
class JuegoGato:
    def __init__(self, root): 
        self.root = root
        self.root.title("Juego de Gato")
        self.root.configure(bg = "gold")
        self.turno = "X"
        self.ganadas = {"X": 0, "O": 0}
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.label_turno = tk.Label(root, text="Turno: X", font=("Arial", 14))
        self.label_turno.pack(pady=10)
        self.label_marcador = tk.Label(root, text="X: 0 | O: 0", font=("Arial", 14))
        self.label_marcador.pack()
        self.frame = tk.Frame(root)
        self.frame.pack()
        for i in range(3):
            for j in range(3):
                boton = tk.Button(self.frame, text="", width=10, height=4,
                                  font=("Arial", 20),
                                  command=lambda i=i, j=j: self.jugar(i, j))
                boton.grid(row=i, column=j)
                self.botones[i][j] = boton 
        self.boton_reiniciar = tk.Button(root, text="Reiniciar Tablero", command=self.reiniciar_tablero)
        self.boton_reiniciar.pack(pady=10)
    def jugar(self, i, j):
        if self.botones[i][j]["text"] == "":
            self.botones[i][j]["text"] = self.turno
            self.tablero[i][j] = self.turno
            if self.revisar_ganador():
                self.ganadas[self.turno] += 1
                messagebox.showinfo("¡Fin del juego!", f"¡{self.turno} gana!")
                self.actualizar_marcador()
                self.reiniciar_tablero()
            elif self.tablero_lleno():
                messagebox.showinfo("Empate", "¡Empate!")
                self.reiniciar_tablero()
            else:
                self.turno = "O" if self.turno == "X" else "X"
                self.label_turno.config(text=f"Turno: {self.turno}")
    def revisar_ganador(self):
        t = self.tablero
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != "":
                return True
            if t[0][i] == t[1][i] == t[2][i] != "":
                return True
        if t[0][0] == t[1][1] == t[2][2] != "":
            return True
        if t[0][2] == t[1][1] == t[2][0] != "":
            return True
        return False
    def tablero_lleno(self):
        return all(self.tablero[i][j] != "" for i in range(3) for j in range(3))
    def reiniciar_tablero(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botones[i][j]["text"] = ""
        self.turno = "X"
        self.label_turno.config(text="Turno: X")
    def actualizar_marcador(self):
        self.label_marcador.config(text=f"X: {self.ganadas['X']} | O: {self.ganadas['O']}")
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoGato(root)
    root.mainloop()