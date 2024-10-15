# Importaciones
import tkinter as tk

# Configurar ventana
ventana = tk.Tk()
ventana.title("Hamburguesería IT")
ventana.config(width=500, height=500)

# Configuración de label del título "Pedidos" 
titulo = tk.Label(ventana, text="------ Pedidos ------")
titulo.place(relx=0.5, rely=0.1, anchor="center")

# Configuración de label Encargado
encargado_label = tk.Label(ventana, text="Nombre Encargado:", justify="left")
encargado_label.place(relx=0.3, rely=0.25, anchor="center")

# Configuración de entry Encargado
encargado_input = tk.Entry(ventana)
encargado_input.place(relx=0.7, rely=0.25, anchor="center")


# Configuración de label COMBO S
combo_S_label = tk.Label(ventana, text="Combo S cantidad:", justify="left")
combo_S_label.place(relx=0.3, rely=0.35, anchor="center")

# Configuración de entry COMBO S
combo_S_input = tk.Entry(ventana)
combo_S_input.place(relx=0.7, rely=0.35, anchor="center")


# Configuración de label COMBO D
combo_D_label = tk.Label(ventana, text="Combo D cantidad:", justify="left")
combo_D_label.place(relx=0.3, rely=0.45, anchor="center")

# Configuración de entry COMBO D
combo_D_input = tk.Entry(ventana)
combo_D_input.place(relx=0.7, rely=0.45, anchor="center")


# Configuración de label COMBO T
combo_T_label = tk.Label(ventana, text="Combo T cantidad:", justify="left")
combo_T_label.place(relx=0.3, rely=0.55, anchor="center")

# Configuración de entry COMBO T
combo_T_input = tk.Entry(ventana)
combo_T_input.place(relx=0.7, rely=0.55, anchor="center")


# Configuración de label Postre
postre_label = tk.Label(ventana, text="Postre cantidad:", justify="left")
postre_label.place(relx=0.3, rely=0.65, anchor="center")

# Configuración de entry Postre
postre_input = tk.Entry(ventana)
postre_input.place(relx=0.7, rely=0.65, anchor="center")


# Configuración de label Cliente
cliente_label = tk.Label(ventana, text="Nombre del cliente:", justify="left")
cliente_label.place(relx=0.3, rely=0.75, anchor="center")

# Configuración de entry Cliente
cliente_input = tk.Entry(ventana)
cliente_input.place(relx=0.7, rely=0.75, anchor="center")

######### BOTONES #########
# Botón de SALIR
salir_button = tk.Button(ventana, text="Salir Seguro")
salir_button.place(relx=0.2, rely=0.9, anchor="center", width=130, height=40)

# Botón de CANCELAR PEDIDO
cancelar_pedido_button = tk.Button(ventana, text="Cancelar Pedido")
cancelar_pedido_button.place(relx=0.5, rely=0.9, anchor="center", width=130, height=40)

# Botón de HACER PEDIDO
hacer_pedido_button = tk.Button(ventana, text="Hacer Pedido")
hacer_pedido_button.place(relx=0.8, rely=0.9, anchor="center", width=130, height=40)




ventana.mainloop()
