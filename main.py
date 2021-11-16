from tkinter import *
import tkinter as tk
from tkinter import ttk
import cx_Oracle
from ttkbootstrap import Style


# LOGIN
def createGUI():
    # Creacion del Login
    logstyle = Style(theme='superhero')
    global login
    login = logstyle.master

    # Formato
    login.title("Sistema de Control de Inventario - Logueo")
    login.iconbitmap("inv.ico")
    login.geometry('500x300')
    login.resizable(width=False, height=False)

    # Labels y entries
    ttk.Label(login, text='SISTEMA DE INVENTARIO', font=('Helvetica', 15)).pack()

    # user
    userlog = StringVar()
    ttk.Label(login, text='Usuario', font=('Helvetica', 13)).place(x=80, y=70)
    ttk.Entry(login, width=45, textvariable=userlog).place(x=83, y=93)

    # password
    passwrd = StringVar()
    ttk.Label(login, text='Contraseña', font=('Helvetica', 13)).place(x=80, y=120)
    ttk.Entry(login, width=45, show="●", textvariable=passwrd).place(x=83, y=143)

    # Boton
    ttk.Button(login, text='Ingresar', style='warning.Outline.TButton',
               command=lambda: loginval(userlog.get(), passwrd.get())).place(x=210, y=200)
    # init
    login.mainloop()


# Ingreso
def loginval(userlog, passwrd):
    # Coneccion a oracle
    if validacion(userlog, passwrd):
        login.destroy()
        if "cajero" in userlog:
            cajeroGUI()
        elif "gerente" in userlog:
            gerenteGUI()
        elif "admin" in userlog:
            adminGUI()


# error
def error(msg):
    global err
    err = Tk()
    err.title("Error")
    err.iconbitmap("inv.ico")
    ttk.Label(err, text=msg, font=('Helvetica', 10)).pack()
    ttk.Button(err, text='Ok', command=err.destroy).pack()
    err.mainloop()


# validacion
def validacion(userlog, passwrd):
    try:
        connection = cx_Oracle.connect(user=userlog, password=passwrd, dsn="localhost/xe",
                                       encoding='UTF-8')
        print("db version:", connection.version)
        return True
    except Exception as ex:
        error(ex)


# Menu cajero
def cajeroGUI():
    # creacion
    casherstyle = Style(theme='superhero')
    global casher
    casher = casherstyle.master

    # Formato
    casher.title("Sistema de Control de Inventario - Cajero")
    casher.iconbitmap("inv.ico")
    casher.geometry('800x500')
    casher.resizable(width=False, height=False)

    # Labels y entries
    ttk.Label(casher, text='CAJERO', font=('Helvetica', 15)).pack()
    ttk.Label(casher, text='PRODUCTOS', font=('Helvetica', 15)).place(x=92, y=30)

    # total
    total = IntVar()
    ttk.Label(casher, text='TOTAL:', font=('Helvetica', 15)).place(x=60, y=450)
    ttk.Entry(casher, width=20, textvariable=total).place(x=150, y=450)
    # codigo
    code = IntVar()
    ttk.Label(casher, text='Codigo', font=('Helvetica', 12)).place(x=520, y=45)
    ttk.Entry(casher, width=20, textvariable=code).place(x=600, y=45)
    # cantidad
    cant = IntVar()
    ttk.Label(casher, text='Cantidad', font=('Helvetica', 12)).place(x=520, y=90)
    ttk.Entry(casher, width=20, textvariable=cant).place(x=600, y=90)
    # listbox
    box = tk.Listbox(casher, width=35, height=20).place(x=40, y=60)
    # pago
    pago = IntVar()
    ttk.Label(casher, text='Paga con:', font=('Helvetica', 12)).place(x=520, y=300)
    ttk.Entry(casher, width=20, textvariable=pago).place(x=600, y=300)
    ttk.Button(casher, text='Pagar', width=12, style='danger.TButton').place(x=600, y=350)
    # carrito
    ttk.Button(casher, text='Agregar', width=12, style='warning.TButton').place(x=600, y=150)

    # init
    casher.mainloop()


# Menu gerente
def gerenteGUI():
    # creacion
    gerentestyle = Style(theme='superhero')
    global gerente
    gerente = gerentestyle.master

    # Formato
    gerente.title("Sistema de Control de Inventario - Modulo gerencial")
    gerente.iconbitmap("inv.ico")
    gerente.geometry('300x300')
    gerente.resizable(width=False, height=False)

    # Labels y entries
    ttk.Label(gerente, text='MODULO GERENCIAL', font=('Helvetica', 15)).pack()
    # opciones
    ttk.Button(gerente, text='Editar', width=20, style='warning.TButton',
               command=lambda: editGUI(gerente)).place(x=60, y=35)
    ttk.Button(gerente, text='Consultar', width=20, style='success.TButton',
               command=lambda: consultaGUI(gerente)).place(x=60, y=95)
    ttk.Button(gerente, text='Salir', width=20, style='danger.TButton',
               command=lambda: menu(gerente)).place(x=60, y=155)
    # init
    gerente.mainloop()


# menu admin
def adminGUI():
    # creacion
    adminstyle = Style(theme='superhero')
    global admin
    admin = adminstyle.master

    # Formato
    admin.title("Sistema de Control de Inventario - Modulo gerencial")
    admin.iconbitmap("inv.ico")
    admin.geometry('300x300')
    admin.resizable(width=False, height=False)

    # opciones
    ttk.Button(admin, text='Registrar nuevo producto', width=22, style='secondary.TButton',
               command=lambda: insertGUI(admin)).place(x=58)
    ttk.Button(admin, text='Consultar', width=22, style='success.TButton',
               command=lambda: consultaGUI(admin)).place(x=58, y=40)
    ttk.Button(admin, text='Editar', width=22, style='warning.TButton',
               command=lambda: editGUI(admin)).place(x=58, y=80)
    ttk.Button(admin, text='Borrar', width=22, style='primary.TButton',
               command=lambda: editGUI(admin)).place(x=58, y=120)
    ttk.Button(admin, text='Salir', width=22, style='danger.TButton',
               command=lambda: menu(admin)
               ).place(x=58, y=200)

    # init
    admin.mainloop()


# insertar
def insertGUI(gui):
    gui.destroy()
    instyle = Style(theme='superhero')
    global ins
    ins = instyle.master

    # Formato
    ins.title("Sistema de Control de Inventario - insertar producto")
    ins.iconbitmap("inv.ico")
    ins.geometry('300x400')
    ins.resizable(width=False, height=False)
    ttk.Label(ins, text='Inserte los datos del producto', font=('Helvetica', 15)).pack()

    # entries
    cod = StringVar()
    ttk.Label(ins, text='Ingrese el codigo del producto', font=('Helvetica', 10)).place(x=60, y=35)
    ttk.Entry(ins, width=20, textvariable=cod).place(x=72, y=60)

    desc = StringVar()
    ttk.Label(ins, text='Ingrese descripcion del producto', font=('Helvetica', 10)).place(x=59, y=92)
    ttk.Entry(ins, width=20, textvariable=desc).place(x=72, y=112)

    peso = StringVar()
    ttk.Label(ins, text='Ingrese peso del producto', font=('Helvetica', 10)).place(x=69, y=144)
    ttk.Entry(ins, width=20, textvariable=peso).place(x=72, y=164)

    cantidad = StringVar()
    ttk.Label(ins, text='Ingrese cantidad del producto', font=('Helvetica', 10)).place(x=69, y=184)
    ttk.Entry(ins, width=20, textvariable=cantidad).place(x=72, y=204)

    precio = StringVar()
    ttk.Label(ins, text='Ingrese precio del producto', font=('Helvetica', 10)).place(x=69, y=224)
    ttk.Entry(ins, width=20, textvariable=precio).place(x=72, y=244)

    cod_cat = StringVar()
    ttk.Label(ins, text='Ingrese codigo de categoria del producto', font=('Helvetica', 10)).place(x=39, y=266)
    ttk.Entry(ins, width=20, textvariable=cod_cat).place(x=72, y=289)

    ttk.Button(ins, text='Registrar', width=22, style='success.TButton').place(x=60, y=330)

    ins.mainloop()


# consultar
def consultaGUI(gui):
    gui.destroy()
    # creacion
    constyle = Style(theme='superhero')
    global cons
    cons = constyle.master

    # Formato
    cons.title("Sistema de Control de Inventario - Consulta")
    cons.iconbitmap("inv.ico")
    cons.geometry('300x300')
    cons.resizable(width=False, height=False)

    # label y entry
    cod = StringVar()
    ttk.Label(cons, text='Ingrese el codigo del producto', font=('Helvetica', 10)).place(x=60, y=35)
    ttk.Entry(cons, width=20, textvariable=cod).place(x=72, y=60)

    ttk.Button(cons, text='Consultar', width=22, style='success.TButton').place(x=60, y=60)


# editar
def editGUI(gui):
    gui.destroy()
    # creacion
    edityle = Style(theme='superhero')
    global edit
    edit = edityle.master

    # Formato
    edit.title("Sistema de Control de Inventario - Consulta")
    edit.iconbitmap("inv.ico")
    edit.geometry('300x500')
    edit.resizable(width=False, height=False)
    # label y entries
    cod = StringVar()
    ttk.Label(edit, text='Ingrese el codigo del producto', font=('Helvetica', 10)).place(x=60, y=35)
    ttk.Entry(edit, width=20, textvariable=cod).place(x=72, y=60)

    ttk.Button(edit, text='Consultar', width=22, style='success.TButton').place(x=60, y=100)
    # if metodobuscar(cod) :
    #   entry metodobuscar(cod).id
    #    *
    #    *
    #    *
    # else
    #    error("No se encuentra el producto")


# borrar
def delGUI(gui):
    gui.destroy()
    # creacion
    delstyle = Style(theme='superhero')
    global delt
    delt = delstyle.master
    # Formato
    delt.title("Sistema de Control de Inventario - Consulta")
    delt.iconbitmap("inv.ico")
    delt.geometry('300x300')
    delt.resizable(width=False, height=False)
    # labels y entries
    cod = StringVar()
    ttk.Label(edit, text='Ingrese el codigo del producto', font=('Helvetica', 10)).place(x=60, y=35)
    ttk.Entry(edit, width=20, textvariable=cod).place(x=72, y=60)
    ttk.Button(edit, text='Consultar', width=22, style='danger.TButton').place(x=60, y=100)

    delt.mainloop()


# exit
def menu(gui):
    gui.destroy()
    createGUI()


# main
if __name__ == "__main__":
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_12_2")
    createGUI()
