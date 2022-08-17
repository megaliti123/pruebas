from tkinter import*
import pyglet
import os
import fnmatch

import tkinter
from tkinter import*
from tkinter import messagebox

import pymysql 


connect=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
fcursor =connect.cursor()

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("1920x1080")
    pantalla.title("bienvenido")
    pantalla.iconbitmap("software.ico")

    image= PhotoImage(file = "software.gif")
    image = image.subsample(2,2)
    label = Label(image=image)
    label.pack()

    Label(text="Accseso", bg="navy", fg="white", width="300", height="3", font=("Calibir",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30",command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrarse",height="3", width="30",command=registrarse).pack()

    pantalla.mainloop()

def inicio_sesion():
    
    global pantalla1

    pantalla1 = Toplevel()
    pantalla1.geometry("400x250")
    pantalla1.iconbitmap("software.ico")
    pantalla1.title("inicio de sesion")

    Label(pantalla1,text="por favor ingrese su Usuario y Contrasena", bg="navy", fg="white", width="300", height="3", font=("Calibir",15)).pack()
    Label(pantalla1,text="").pack()

    global nombre_usuario_verify
    global contrasena_usuario_verify

    nombre_usuario_verify=StringVar()
    contrasena_usuario_verify=StringVar()

    global nombre_ususario_entry
    global contrasena_ususario_entry

    Label(pantalla1 ,text="Usuario").pack()
    nombre_ususario_entry = Entry(pantalla1, textvariable=nombre_usuario_verify)
    nombre_ususario_entry.pack()
    Label(pantalla1).pack()
    

    Label(pantalla1 ,text="contrasena").pack()
    contrasena_ususario_entry = Entry(pantalla1, textvariable=contrasena_usuario_verify)
    contrasena_ususario_entry.pack()
    Label (pantalla1).pack()

    Button(pantalla1, text="iniciar sesion").pack()


def registrarse():

    global pantalla2
    pantalla2 = Toplevel()
    pantalla2.geometry("400x250")
    pantalla2.iconbitmap("software.ico")
    pantalla2.title("registro")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry =StringVar()
    contrasena_entry = StringVar()

    Label(pantalla2,text="Por favor ingrese un usuario y contrasena de su eleccion, para el registro de sistema",bg="navy", fg="white", width="300", height="3", font=("Calibir",15)).pack()
    Label(pantalla2,text="").pack()


    Label(pantalla2 ,text="Usuario").pack()
    nombreususario_entry = Entry(pantalla2)
    nombreususario_entry.pack()
    Label(pantalla2).pack()


    
    Label(pantalla2 ,text="contrasena").pack()
    contrasena_entry = Entry(pantalla2)
    contrasena_entry.pack()
    Label (pantalla2).pack()

    Button(pantalla2, text="registrar",command=insertar_datos).pack()

def insertar_datos():


    sql = "INSERT INTO login (nombre, contrasena) VAlUES('{0}','{1}')".format(nombreusuario_entry.get(),contrasena_entry.get())
    fcursor.execute(sql)
    try:
     
     connect.commit()
     messagebox.showinfo(message="registro exitoso")
   
    except:
        connect.rollback()
        messagebox.showinfo(message="no registrado")

    connect.close()


menu_pantalla()