from tkinter import *
from tkinter import ttk
import cx_Oracle
from ttkbootstrap import Style
from user import user


def createGUI():
    # Creacion del Login
    logstyle = Style(theme='superhero')
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
    ttk.Label(login, text='usuario', font=('Helvetica', 13), textvariable=userlog).place(x=80, y=70)
    ttk.Entry(login, width=45).place(x=83, y=93)

    # password
    passwrd = StringVar()
    ttk.Label(login, text='Contraseña', font=('Helvetica', 13), textvariable=passwrd).place(x=80, y=120)
    ttk.Entry(login, width=45, show="●").place(x=83, y=143)

    # Boton
    ttk.Button(login, text='Ingresar', style='warning.Outline.TButton',
               command=lambda: loginval(userlog, passwrd)).place(x=210, y=200)
    # init
    login.mainloop()


# Ingreso
def loginval(userlog, passwrd):
    # Coneccion a oracle
    error("Clave incorrecta")


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
    conn = cx_Oracle.connect(userlog+'/'+passwrd+'@xe')


# main
if __name__ == "__main__":

    createGUI()
