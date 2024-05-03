# %%

from tkinter import *  # Importa todos los símbolos (funciones, clases, etc.) 
from tkinter import ttk

window = Tk()  # Crea una instancia de la ventana
window.title("Bienvenido ")  # Establece el título de la ventana
window.geometry('300x200')  # Establece las dimensiones de la ventana
window.configure(background="pink")  # Configura el color de fondo a rosa

# Establece lo que va a solicitar el formulario
a = Label(window, text="Nombre").grid(row=0, column=0) 
b = Label(window, text="Apellido").grid(row=1, column=0)
c = Label(window, text="Correo Electrónico").grid(row=2, column=0)
d = Label(window, text="Número de Contacto").grid(row=3, column=0)

# Crea campos de entrada
a1 = Entry(window).grid(row=0, column=1)
b1 = Entry(window).grid(row=1, column=1)
c1 = Entry(window).grid(row=2, column=1)
d1 = Entry(window).grid(row=3, column=1)

# Define una función que se ejecuta al hacer clic en el botón
def clicked():
   res = "Bienvenidos sean a" + txt.get()
   lbl.configure(text=res)

# Crea un botón
btn = ttk.Button(window, text="Enviar").grid(row=4, column=0)

window.mainloop()

# %%
from tkinter import *  # Importa todos los símbolos de tkinter

# Definición de los campos que serán mostrados en la interfaz
fields = ('Tasa Anual', 'Número de Pagos', 'Préstamo Principal', 'Pago Mensual', 'Préstamo Restante')

# Calcula el pago mensual
def pago_mensual(entradas):
    # Tasa de interés por período:
    r = (float(entradas['Tasa Anual'].get()) / 100) / 12
    print("r", r)
    # Préstamo principal:
    prestamo = float(entradas['Préstamo Principal'].get())
    n = float(entradas['Número de Pagos'].get())
    prestamo_restante = float(entradas['Préstamo Restante'].get())
    # Cálculo del factor de amortización
    q = (1 + r) ** n
    # Fórmula para calcular el pago mensual de un préstamo
    mensual = r * ((q * prestamo - prestamo_restante) / (q - 1))
    mensual = ("%8.2f" % mensual).strip()
    # Actualiza el campo de entrada con el resultado 
    entradas['Pago Mensual'].delete(0, END)  # Borra el contenido del campo 
    entradas['Pago Mensual'].insert(0, mensual)  # Inserta el resultado del cálculo 
    print("Pago Mensual: %f" % float(mensual))  # Imprime el pago mensual 


# Función para calcular el saldo final
def saldo_final(entradas):
    # Tasa de interés por período:
    r = (float(entradas['Tasa Anual'].get()) / 100) / 12
    print("r", r)
    # Préstamo principal:
    prestamo = float(entradas['Préstamo Principal'].get())
    n = float(entradas['Número de Pagos'].get())
    # Cálculo del factor de amortización
    q = (1 + r) ** n
    # Pago mensual:
    mensual = float(entradas['Pago Mensual'].get())
    # Fórmula para calcular el saldo restante de un préstamo
    restante = q * prestamo - ((q - 1) / r) * mensual
    restante = ("%8.2f" % restante).strip()
    # Actualiza el campo de entrada 'Préstamo Restante' con el resultado del cálculo
    entradas['Préstamo Restante'].delete(0, END)
    entradas['Préstamo Restante'].insert(0, restante)
    print("Préstamo Restante: %f" % float(restante))

# Función para crear ventana que vera el usuario
def crear_ventana(root, fields):
    entradas = {}
    # funcion for para poner campos definidos, crear etiquetas y los campos de entrada correspondientes
    for field in fields:
        fila = Frame(root)
        etiqueta = Label(fila, width=22, text=field+": ", anchor='w')
        entrada = Entry(fila)
        entrada.insert(0, "0")  # Inserta un valor predeterminado en los campos establecidos
        fila.pack(side=TOP, fill=X, padx=5, pady=5)
        etiqueta.pack(side=LEFT)
        entrada.pack(side=RIGHT, expand=YES, fill=X)
        entradas[field] = entrada
    return entradas

if __name__ == '__main__':
    root = Tk()
    root.title("Calculadora de Préstamos")  # Establece el título de la ventana
    root.geometry('500x300')  # Establece las dimensiones de la ventana
    root.configure(background="lightblue")  # Configura el color de fondo

    # Crea otra ventana con lo que ya creamos
    entradas = crear_ventana(root, fields)

    # Crea botones para calcular el saldo final, el pago mensual y salir de la aplicación
    b1 = Button(root, text='Calcular Saldo Final', bg='pink', fg='white', width=15,
                command=(lambda e=entradas: saldo_final(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Calcular Pago Mensual', bg='pink', fg='white', width=15,
                command=(lambda e=entradas: pago_mensual(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Salir', bg='pink', fg='white', width=15, command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()



