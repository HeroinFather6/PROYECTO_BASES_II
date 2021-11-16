from tkinter import *

from tkinter import ttk
import cx_Oracle
from ttkbootstrap import Style
from user import user


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
    gerente.geometry('800x500')
    gerente.resizable(width=False, height=False)

    # Labels y entries
    ttk.Label(gerente, text='MODULO GERENCIAL', font=('Helvetica', 15)).pack()

    # init
    gerente.mainloop()

# main
if __name__ == "__main__":
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_12_2")
    createGUI()
