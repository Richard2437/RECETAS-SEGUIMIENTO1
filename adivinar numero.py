import tkinter as tk
from tkinter import messagebox
import random

class AdivinaNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número 🔢")
        self.root.geometry("350x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#e9f5f9")

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        
        self.crear_widgets()

    def crear_widgets(self):
        # Marco principal
        frame = tk.Frame(self.root, bg="#e9f5f9", padx=20, pady=20)
        frame.pack(expand=True)

        # Título del juego
        self.label_titulo = tk.Label(frame, text="Adivina el número (1-100)", font=("Arial", 14, "bold"), bg="#e9f5f9", fg="#2a52be")
        self.label_titulo.pack(pady=10)

        # Etiqueta de instrucción
        self.label_instruccion = tk.Label(frame, text="Ingresa un número:", font=("Arial", 10), bg="#e9f5f9")
        self.label_instruccion.pack()

        # Entrada del usuario
        self.entrada_numero = tk.Entry(frame, width=15, font=("Arial", 12), justify="center")
        self.entrada_numero.pack(pady=5)
        self.entrada_numero.bind("<Return>", lambda event: self.verificar_adivinanza())

        # Botón para verificar
        self.boton_verificar = tk.Button(frame, text="Verificar", command=self.verificar_adivinanza, font=("Arial", 10, "bold"), bg="#4caf50", fg="white", activebackground="#45a049")
        self.boton_verificar.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(frame, text="", font=("Arial", 10, "italic"), bg="#e9f5f9")
        self.label_resultado.pack(pady=5)

    def verificar_adivinanza(self):
        try:
            intento_usuario = int(self.entrada_numero.get())
            self.intentos += 1

            if intento_usuario < 1 or intento_usuario > 100:
                self.label_resultado.config(text="⚠️ Por favor, ingresa un número entre 1 y 100.", fg="#ffc107")
            elif intento_usuario < self.numero_secreto:
                self.label_resultado.config(text=f"El número es más alto. ¡Intenta de nuevo!", fg="#f44336")
            elif intento_usuario > self.numero_secreto:
                self.label_resultado.config(text=f"El número es más bajo. ¡Intenta de nuevo!", fg="#f44336")
            else:
                self.label_resultado.config(text=f"🎉 ¡Felicidades! Adivinaste el número en {self.intentos} intentos.", fg="#4caf50")
                self.boton_verificar.config(state="disabled")
                self.entrada_numero.config(state="disabled")
                messagebox.showinfo("¡Ganaste!", f"¡Correcto! El número era {self.numero_secreto}. Lo adivinaste en {self.intentos} intentos.")
                self.reiniciar_juego()

        except ValueError:
            self.label_resultado.config(text="⛔️ Entrada inválida. Ingresa un número válido.", fg="#dc3545")
        
        self.entrada_numero.delete(0, tk.END)

    def reiniciar_juego(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.entrada_numero.config(state="normal")
        self.boton_verificar.config(state="normal")
        self.label_resultado.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaNumeroApp(root)
    root.mainloop()
