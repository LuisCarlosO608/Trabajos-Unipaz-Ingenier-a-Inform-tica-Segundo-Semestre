import tkinter as tk
from tkinter import messagebox
from Backend_SGI import invent

inv = invent()

def registro_p():
    try:
        inv.registro_P(
            textbox_id.get(),
            textbox_N_P.get(),
            textbox_Cat.get(),
            int(textbox_cant.get()),
            float(textbox_Pre.get())
        )
        messagebox.showinfo("Éxito", "Producto registrado")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def edit_p():
    try:
        inv.edit_P(
            textbox_id.get(),
            textbox_N_P.get(),
            textbox_Cat.get(),
            int(textbox_cant.get()),
            float(textbox_Pre.get())
        )
        messagebox.showinfo("Éxito", "Producto editado")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def ag_C():
    try:
        inv.añadir_C(textbox_Cat.get())
        messagebox.showinfo("Éxito", "Categoría agregada")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def gen_F():
    try:
        orden_dict = {}
        for linea in orden_entry.get().split(","):
            id_prod, cantidad = linea.strip().split(":")
            orden_dict[id_prod] = int(cantidad)
        factura, total = inv.gen_F(orden_dict)
        factura_text.delete("1.0", tk.END)
        factura_text.insert(tk.END, "Factura:\n")
        for nombre, cantidad, precio, subtotal in factura:
            factura_text.insert(tk.END, f"{nombre} x{cantidad} valor: ${precio:.2f} = ${subtotal:.2f}\n")
        factura_text.insert(tk.END, f"\nTotal: ${total:.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_productos():
    productos_text.delete("1.0", tk.END)
    productos_text.insert(tk.END, "Productos en inventario:\n\n")
    for id_prod, datos in inv.P.items():
        productos_text.insert(tk.END, f"ID: {id_prod}\n")
        productos_text.insert(tk.END, f"Nombre: {datos['nombre']}\n")
        productos_text.insert(tk.END, f"Categoría: {datos['categoria']}\n")
        productos_text.insert(tk.END, f"Cantidad: {datos['cantidad']}\n")
        productos_text.insert(tk.END, f"Precio: ${datos['precio']:.2f}\n")
        productos_text.insert(tk.END, "-"*40 + "\n")

ventana = tk.Tk()
ventana.title("Sistema De Gestión De Inventario")
ventana.geometry("1024x728")
ventana.config(bg="gray")

tk.Label(ventana, text="Bienvenido, ¿Qué desea hacer?", bg="gray", font=("Arial", 14)).grid(row=0, column=0, columnspan=4, pady=10)


tk.Label(ventana, text="ID del producto").grid(row=1, column=0)
textbox_id = tk.Entry(ventana)
textbox_id.grid(row=2, column=0)

tk.Label(ventana, text="Nombre del producto").grid(row=1, column=1)
textbox_N_P = tk.Entry(ventana)
textbox_N_P.grid(row=2, column=1)

tk.Label(ventana, text="Categoría del producto").grid(row=1, column=2)
textbox_Cat = tk.Entry(ventana)
textbox_Cat.grid(row=2, column=2)

tk.Label(ventana, text="Cantidad").grid(row=1, column=3)
textbox_cant = tk.Entry(ventana)
textbox_cant.grid(row=2, column=3)

tk.Label(ventana, text="Precio").grid(row=1, column=4)
textbox_Pre = tk.Entry(ventana)
textbox_Pre.grid(row=2, column=4)


tk.Button(ventana, text="Registrar Producto", command=registro_p).grid(row=3, column=1, pady=10)
tk.Button(ventana, text="Editar Producto", command=edit_p).grid(row=3, column=2)
tk.Button(ventana, text="Agregar Categoría", command=ag_C).grid(row=3, column=0)


tk.Label(ventana, text="Orden (ID:cantidad,...)").grid(row=4, column=0, pady=10)
orden_entry = tk.Entry(ventana, width=40)
orden_entry.grid(row=5, column=0, columnspan=2)
tk.Button(ventana, text="Generar Factura", command=gen_F).grid(row=6, column=0, pady=10)


factura_text = tk.Text(ventana, height=10, width=60)
factura_text.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

tk.Button(ventana, text="Ver Productos", command=mostrar_productos).grid(row=8, column=0, pady=10)
productos_text = tk.Text(ventana, height=10, width=80)
productos_text.grid(row=9, column=0, columnspan=5, padx=10, pady=10)

ventana.mainloop()






























ventana.mainloop()