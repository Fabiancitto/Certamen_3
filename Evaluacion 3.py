import os
os.system("cls")

listaCodigo = []
listaNombre = []
listaCategoria = ["Sobre","Paquete"]
listaPrecio = []
listaCantidad = []

nomUsuario = input("Ingrese Nombre: ")
apellUsuario = input("Ingrese Apellido: ")

menu = """------------------------
Bienvenido A SuperStore
------------------------
1. Registrar Producto
2. Buscar Producto
3. Lista De Productos
4. Salir
------------------------
"""


def IngresarF():
    while True:
        try:
                while True:
                    cod = int(input("Codigo del producto: "))
                    if len(str(cod)) < 6 or len(str(cod)) > 6:
                        print("Error al ingresar")
                    else:
                         listaCodigo.append(cod)
                         break
                while True:
                    nom = input("Nombre del producto: ")
                    if len(str(nom)) < 2 or len(str(nom)) > 50:
                         print("Error al ingresar")
                    else:
                        listaNombre.append(nom)
                        break
                while True:
                    cat = input("Categoria del producto: ")
                    if cat == "Sobre" or cat == "Paquete" or cat == "sobre" or cat == "paquete":
                        listaCategoria.append(cat)
                        break
                    else:
                        print("Error al ingresar")
                while True:
                    pre = int(input("Precio Del Producto: $"))
                    if pre > 0:
                        listaPrecio.append(pre)
                        break
                    else:
                        print("Error al ingresar")
                while True:
                    stok = int(input("Stock del producto: "))
                    if stok >= 0:
                        listaCantidad.append(stok)
                        break
                    elif stok < 0 or float:
                        print("Error al ingresar")     
        except:
            print("Ocurrio una excepcion")

def BuscarF():
    codi = input("Ingrese codigo a ingresar: ")
    print(f"Listar: {codi}")
    for i in range(len(listaCodigo)):
        if codi == listaCodigo:
            print("----------------------------------------------")
            print(f"{listaCodigo[i]:6d}{listaNombre[i]:50s}{listaCantidad[i]:30s}{listaPrecio[i]:10s}{listaCantidad[i]:6d}") 
            print("----------------------------------------------")

def ListarF():
        print("CODIGO|NOMBRE|CATEGORIA|PRECIO|STOCK")
        cant=0
        for i in range(len(listaCodigo)):
            if listaCodigo[i] < 5:
                stock = "SI"
                cant += 1
            else: 
                stock = "NO"
            print("----------------------------------------------")
            print(f"{listaCodigo[i]:6d}{listaNombre[i]:50s}{listaCantidad[i]:30s}{listaPrecio[i]:10s}{listaCantidad[i]:6d}") 
            print("----------------------------------------------")

while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            print(f"Gracias por visitarnos {nomUsuario} {apellUsuario}")
            print("Version 1.1.0")
            break
        elif opc == 1:
            IngresarF()
        elif opc == 2:
            BuscarF()
        elif opc == 3:
            ListarF()
        else:
            print("Error al ingresar")
    except:
        print("Ocurrio una excepcion")


input("\n Enter para terminar")