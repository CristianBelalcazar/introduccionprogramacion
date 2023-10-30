# open = nos sirve para crear archivo
def app():
    #Crear archivo
    archivo = open('archivo.txt', 'w') # w es escritura, sino existe lo creara

    #generar numeros en archivos
    for i in range(0,20): # iteramos para que nos muestre numero de 0 a 20
        archivo.write('Esta es la linea ' + str(i) + "\r\n")

    #cerrar el archivo
    archivo.close()

app()