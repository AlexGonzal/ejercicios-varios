#este programa codifica al cliente por nombre , tipo y fecha

from datetime import datetime

while True :

    nombre_cliente = input( " por favor introduzca el nombre del cliente : ")

    if len(nombre_cliente) >= 3 :
        codigo_a = nombre_cliente[0:3]
        break
    else:
        print( " por favor introduzca un nombre con mas caracteres ")

now = str(datetime.now())

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


codigo = codigo_a.upper() + "-" + "01" + now[2:4] + "-" + codigo_b
print( f'tu codigo es {codigo}')

print (" te gusta mi codigo?")

print("Estas son pruebas para github")