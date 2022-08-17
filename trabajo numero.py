


from tkinter import IntVar
import pyglet
import os
import fnmatch


import mysql.connector

conexion = mysql.connector.connect(user = 'root' , password = '', 
            host = 'localhost', database = 'almacen', port='3306')

cursor = conexion.cursor()

menu = '''\n****************************
*     MENÚ DE ARTICULOS    *
****************************
*                          *
*  a) Insertar articulo    *
*  b) Eliminar articulo    *
*  c) Imprimir articulos   *
*  x) Salir                *
*                          *
****************************'''


    

def consulta_datos():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM articulo"
    cursor.execute(consulta)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
      

def insertar_datos():
    id_articulo = int(input("ingresar id (8 digitos): "))
    nombre = input("ingresar nombre: ")
    tipo = input("ingresar tipo del articulo: ")
    cantidad = int(input("ingresar cantidad del producto: "))
    precio = float(input("ingresar precio del producto: "))

    datos = (id_articulo,nombre,tipo,cantidad,precio)
    cursor = conexion.cursor()
    sql = "insert into articulo(id_articulo,nombre,tipo,cantidad,precio) values (%s,%s,%s,%s,%s)"
    cursor.execute(sql,datos)


    conexion.commit()
    cursor.close()
    conexion.close()   


def articulo_borrar():

   

    id_cambiar =int(input("ingrese el id del articulo a borrar: "))

    sql= f"DELETE FROM articulo WHERE id_articulo='{id_cambiar}'"
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()  

    
def main():

 opcion="0"
 while opcion != 'x':
    print(menu)
    opcion = input("opcion: ")
    if opcion == 'a':
        print("****** insertar articulo ******")
        insertar_datos()


    if opcion == 'b':
        print("****** borrar articulo ******")
        articulo_borrar()


    if opcion == 'c':
        print("****** consulta de datos ******")
        consulta_datos()
    elif opcion == 'x':
        print("hasta la proxima usuario")
      


if __name__ == "__main__":
    main()