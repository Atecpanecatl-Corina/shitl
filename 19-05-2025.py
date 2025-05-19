import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
datos_alumnos = []
def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()
def mostrar_pantalla_inicio():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Seas bienvenido/a", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Bienvenido/a")).pack()
def mostrar_pantalla_datos_alumno():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Ingresa los datos del alumno", font=("Arial", 14)).pack(pady=10)
    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_nombre = tk.Entry(area_dinamica)
    campo_nombre.pack(pady=5)
    tk.Label(area_dinamica, text="Turno:").pack()
    turno_seleccionado = tk.StringVar(value="Mañana")
    tk.Radiobutton(area_dinamica, text="Mañana", variable=turno_seleccionado, value="Mañana").pack()
    tk.Radiobutton(area_dinamica, text="Tarde", variable=turno_seleccionado, value="Tarde").pack()
    tk.Label(area_dinamica, text="Grado:").pack()
    combo_grado = ttk.Combobox(area_dinamica, values=["2°", "4°", "6°"])
    combo_grado.pack()
    combo_grado.current(0)
    def guardar_datos():
        nombre = campo_nombre.get()
        turno = turno_seleccionado.get()
        grado = combo_grado.get()
        if nombre:
            datos_alumnos.append({"nombre": nombre, "turno": turno, "grado": grado})
            messagebox.showinfo("Datos guardados", f"Nombre: {nombre}\nTurno: {turno}\nGrado: {grado}")
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa el nombre del alumno.")
    def mostrar_datos_guardados():
        if datos_alumnos:
            texto = "Alumnos guardados:\n\n"
            for i, alumno in enumerate(datos_alumnos, start=1):
                texto += f"{i}. {alumno['nombre']} - {alumno['turno']} - {alumno['grado']}\n"
            messagebox.showinfo("Lista de alumnos", texto)
        else:
            messagebox.showinfo("Sin datos", "No hay alumnos guardados aún.")
    tk.Button(area_dinamica, text="Guardar datos", command=guardar_datos).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar alumnos guardados", command=mostrar_datos_guardados).pack(pady=5)
def mostrar_pantalla_configuracion():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Personaliza los colores de fondo", font=("Arial", 14)).pack(pady=10)
    colores = ["white", "brown", "purple", "lightgreen"]
    tk.Label(area_dinamica, text="Selecciona un color:").pack()
    def cambiar_color_fondo(color):
        ventana_principal.config(bg=color)
        menu_lateral.config(bg=color)
        area_dinamica.config(bg=color)
    for color in colores:
        tk.Button(area_dinamica, text=color, bg=color, width=20, command=lambda c=color: cambiar_color_fondo(c)).pack(pady=2)
def mostrar_pantalla_ayuda():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Guía de uso para el alumno", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación educativa")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")
area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")
tk.Button(menu_lateral, text="Inicio", command=mostrar_pantalla_inicio, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos del alumno", command=mostrar_pantalla_datos_alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Configuración", command=mostrar_pantalla_configuracion, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=mostrar_pantalla_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)
mostrar_pantalla_inicio()
ventana_principal.mainloop()