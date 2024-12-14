from modules.data_handler import nueva_cotizacion, agregar_producto, generar_pdf
import tkinter as tk
from tkinter import ttk, messagebox

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de Cotizaciones")
        self._setup_ui()

    def _setup_ui(self):
        # Variables
        self.descripcion_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.costo_var = tk.StringVar()

        # Widgets
        tk.Label(self.root, text="Descripción:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.descripcion_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Cantidad:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.cantidad_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Costo con IVA:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.costo_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Agregar Producto", command=self._agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Nueva Cotización", command=nueva_cotizacion).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="Generar PDF", command=generar_pdf).grid(row=4, column=1, pady=10)

    def _agregar_producto(self):
        agregar_producto(
            self.descripcion_var.get(),
            self.cantidad_var.get(),
            self.costo_var.get(),
        )
        # Limpiar campos
        self.descripcion_var.set("")
        self.cantidad_var.set("")
        self.costo_var.set("")

    def run(self):
        self.root.mainloop()
