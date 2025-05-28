import tkinter as tk
from tkinter import messagebox

alumnos = []

def agregar_alumno():
    nombre = entrada_nombre.get()
    try:
        cal1 = float(entrada_cal1.get())
        cal2 = float(entrada_cal2.get())
        cal3 = float(entrada_cal3.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa calificaciones válidas (números).")
        return

    promedio = round((cal1 + cal2 + cal3) / 3, 2)
    alumnos.append({"nombre": nombre, "promedio": promedio})
    actualizar_lista()

    entrada_nombre.delete(0, tk.END)
    entrada_cal1.delete(0, tk.END)
    entrada_cal2.delete(0, tk.END)
    entrada_cal3.delete(0, tk.END)

def actualizar_lista():
    lista_alumnos.delete(0, tk.END)
    alumnos_ordenados = sorted(alumnos, key=lambda x: x["promedio"], reverse=True)
    for a in alumnos_ordenados:
        lista_alumnos.insert(tk.END, f'{a["nombre"]} - Promedio: {a["promedio"]}')

# Interfaz
ventana = tk.Tk()
ventana.title("Control de Calificaciones")

tk.Label(ventana, text="Nombre del Alumno:").grid(row=0, column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Calificación 1:").grid(row=1, column=0)
entrada_cal1 = tk.Entry(ventana)
entrada_cal1.grid(row=1, column=1)

tk.Label(ventana, text="Calificación 2:").grid(row=2, column=0)
entrada_cal2 = tk.Entry(ventana)
entrada_cal2.grid(row=2, column=1)

tk.Label(ventana, text="Calificación 3:").grid(row=3, column=0)
entrada_cal3 = tk.Entry(ventana)
entrada_cal3.grid(row=3, column=1)

tk.Button(ventana, text="Agregar Alumno", command=agregar_alumno).grid(row=4, columnspan=2, pady=10)

lista_alumnos = tk.Listbox(ventana, width=40)
lista_alumnos.grid(row=5, columnspan=2, pady=10)

ventana.mainloop()