# with open = sirven para abrir y al mismo tiempo leer el archivo 
#o mostrar su contenido en consola 
def app():
    with open('archivo.txt') as archivo: #as no ayuda acrear un alias en este caso es archivo
        for contenido in archivo:
            print(contenido.rstrip())  #rstrip quita los saltos de linea del archico

app()