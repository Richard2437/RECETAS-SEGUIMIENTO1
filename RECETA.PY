import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

# Clase para representar una receta
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = [i.strip() for i in ingredientes]

# Clase para gestionar las recetas
class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        if 0 <= indice < len(self.recetas):
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        return None
    
    def obtener_receta(self, indice):
        if 0 <= indice < len(self.recetas):
            return self.recetas[indice]
        return None

# Clase principal de la aplicación con la interfaz gráfica
class RecetarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Recetas 👨‍🍳")
        self.root.geometry("550x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f9fa")

        self.gestor = GestorRecetas()

        # Configurar el menú
        self.configurar_menu()

        # Marcos principales
        self.frame_principal = tk.Frame(self.root, bg="#f8f9fa", padx=20, pady=20)
        self.frame_principal.pack(expand=True, fill="both")
        
        # Etiqueta de título
        tk.Label(self.frame_principal, text="Mi Recetario Personal", font=("Helvetica", 18, "bold"), bg="#f8f9fa", fg="#343a40").pack(pady=(0, 20))

        # Sección de entrada de datos
        frame_entradas = tk.Frame(self.frame_principal, bg="#f8f9fa")
        frame_entradas.pack(pady=10)

        tk.Label(frame_entradas, text="Nombre de la Receta:", bg="#f8f9fa", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entrada_nombre = tk.Entry(frame_entradas, width=45, font=("Arial", 10), bd=1, relief="solid")
        self.entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entradas, text="Ingredientes (separados por coma):", bg="#f8f9fa", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entrada_ingredientes = tk.Entry(frame_entradas, width=45, font=("Arial", 10), bd=1, relief="solid")
        self.entrada_ingredientes.grid(row=1, column=1, padx=5, pady=5)

        # Botón para agregar
        self.boton_agregar = tk.Button(self.frame_principal, text="➕ Agregar Receta", command=self.agregar_receta, bg="#28a745", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=2, activebackground="#218838")
        self.boton_agregar.pack(pady=10, ipadx=10, ipady=5)
        
        # Sección del Listbox
        frame_lista = tk.Frame(self.frame_principal, bg="#f8f9fa")
        frame_lista.pack(pady=10, fill="both", expand=True)

        tk.Label(frame_lista, text="Recetas Guardadas:", font=("Arial", 10, "bold"), bg="#f8f9fa").pack(pady=5)
        self.lista_recetas = tk.Listbox(frame_lista, width=60, height=10, font=("Arial", 10), bd=1, relief="solid", highlightthickness=0)
        self.lista_recetas.pack(fill="both", expand=True)

        # Sección de botones de acción
        frame_botones = tk.Frame(self.frame_principal, bg="#f8f9fa")
        frame_botones.pack(pady=10)

        self.boton_ver = tk.Button(frame_botones, text="👀 Ver Ingredientes", command=self.ver_receta, bg="#007bff", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=2, activebackground="#0056b3")
        self.boton_ver.pack(side="left", padx=10, ipadx=10, ipady=5)

        self.boton_eliminar = tk.Button(frame_botones, text="❌ Eliminar Receta", command=self.eliminar_receta, bg="#dc3545", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=2, activebackground="#c82333")
        self.boton_eliminar.pack(side="right", padx=10, ipadx=10, ipady=5)

    def configurar_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Menú "Archivo"
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)

        # Menú "Acerca de"
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Sobre mí", command=self.mostrar_sobre_mi)
        menubar.add_cascade(label="Acerca de", menu=help_menu)

    def mostrar_sobre_mi(self):
        messagebox.showinfo(
            "Sobre mí",
            "Gestor de Recetas v1.0\n\n"
            "Aplicación creada para organizar y gestionar tus recetas de forma sencilla.\n"
            "Desarrollada con Python y Tkinter."
        )

    def agregar_receta(self):
        nombre = self.entrada_nombre.get().strip().title()
        ingredientes_str = self.entrada_ingredientes.get().strip()
        
        if not nombre or not ingredientes_str:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre de la receta y los ingredientes.")
            return

        ingredientes_lista = [ingrediente.strip() for ingrediente in ingredientes_str.split(",")]
        
        self.gestor.agregar_receta(nombre, ingredientes_lista)
        self.lista_recetas.insert(tk.END, nombre)
        
        self.limpiar_entradas()
        messagebox.showinfo("Éxito", f"Receta '{nombre}' agregada con éxito.")

    def ver_receta(self):
        try:
            indice = self.lista_recetas.curselection()[0]
            receta = self.gestor.obtener_receta(indice)
            ingredientes_str = "\n- ".join(receta.ingredientes)
            messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"Ingredientes:\n\n- {ingredientes_str}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una receta de la lista para verla.")
    
    def eliminar_receta(self):
        try:
            indice = self.lista_recetas.curselection()[0]
            nombre_receta = self.lista_recetas.get(indice)
            
            if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar la receta '{nombre_receta}'?"):
                nombre_eliminado = self.gestor.eliminar_receta(indice)
                if nombre_eliminado:
                    self.lista_recetas.delete(indice)
                    messagebox.showinfo("Éxito", f"La receta '{nombre_eliminado}' ha sido eliminada.")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar la receta.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una receta de la lista para eliminarla.")

    def limpiar_entradas(self):
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_ingredientes.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecetarioApp(root)
    root.mainloop()
