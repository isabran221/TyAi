import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de GUI")
tk.Label(root, text="¡Hola, mundo!").pack()
tk.Button(root, text="Cerrar", command=root.quit).pack()
root.mainloop()