#Version 2.0 de este programa
#este programa codifica al cliente por nombre , tipo y fecha

from datetime import datetime


def code_client():
    """Esta funcion tiene la finalidad de pedir al usuario que introduzca el nombre del cliente del proyecto en desarrollo"""

    print("Buenas soy Daniel")

    while True :

        nombre_cliente = input( " por favor introduzca el nombre del cliente : ")

        if len(nombre_cliente) >= 3 :
            codigo_a = nombre_cliente[0:3]
            break
        else:
            print( " por favor introduzca un nombre con mas caracteres ")
    return codigo_a

def tipo_proyecto():
    """Esta funcion pide al usuario especificar el tipo de proyecto y genera siglas a partir de el"""
    while True :

        tipo = input( "que tipo de proyecto se desea realizar aqui? : \
        1- Planta de Harina         2- Planta ABA \
        3- Extraccion de Aceite     4- Frijoles \
        5- Almacenaje               6- Desarrollo de Equipos   ")

        if tipo=="1" :
            codigo_b = "PHP"
            break
        elif tipo=="2" :
            codigo_b = "ABA"
            break
        elif tipo == "3" :
            codigo_b = "EDA"
            break
        elif tipo == "4" :
            codigo_b = "FRJ"
            break
        elif tipo == "5" :
            codigo_b = "ALM"
            break
        elif tipo == "6" :
            codigo_b = "DDE"
            break
        else:
            print ("por favor introduzca una de las opciones (1,2,3,4,5,6)")

    return codigo_b

def datos (codigo):
    lista=[]
    archivo = open('clientes.txt','r')
    for linea in archivo.readlines():
        lista.append(linea.rstrip('\n'))
    archivo.close()
    if codigo in lista:
        print("El codigo para este proyecto ya existe")
 
    else:
        lista.append(codigo)
        print(lista)
        archivo = open('clientes.txt','w')
        for i in lista :
            archivo.write(i+'\n')
        archivo.close()
        



def run():
    now = str(datetime.now())
    codigo = code_client().upper() + "-" + "01" + now[2:4] + "-" + tipo_proyecto()
    print( f'tu codigo es {codigo}')
    datos(codigo)
    print (" te gusta mi codigo?")


run()

