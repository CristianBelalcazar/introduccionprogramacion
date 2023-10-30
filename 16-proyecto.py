# os es una libreria para crear carpetas o para mirar si existe 
import os 
CARPETA = 'contactos/' # Carpeta de Contactos
EXTENSION = '.txt' #EXtensión de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # revisa si la carpeta existe o no
    crear_directorio()

    #Muestra el menú de opciones
    mostrar_menu()

    #Preguntar al usuario la acción a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion ==1:
            agregar_contacto()
            preguntar = False
        elif opcion ==2:
            editar_contacto()
            preguntar = False
        elif opcion ==3:
            mostrar_contactos()
            preguntar = False
        elif opcion ==4:
            buscar_contacto()
            preguntar = False
        elif opcion ==5:
            eliminar_contacto()
            preguntar = False
        else:
            print('opción no válida, intente de nuevo')

def eliminar_contacto():
     nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

     try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado Corretamente')
     except IOError:
        
        print('No existe ese contacto \r\n ')

     #reinicair app
     app()
   

def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    try:
         with open(CARPETA + nombre + EXTENSION) as contacto:
          print('\r\n Información del Contacto: \r\n')
          for linea in contacto:
             print(linea.rstrip())
          print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #reiniciar la app
    app()

def  mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto: 
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())

                #Imprime un separador entre contactos
                print('\r\n')

        

def editar_contacto():
        print('Escribe el nombre del contacto a editar ')
        nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

        #Revisar si el archivo ya existe antes de editarlo
        existe = existe_contacto(nombre_anterior)  

        if existe:
            with open(CARPETA + nombre_anterior + EXTENSION, 'w' ) as archivo:
              #resto de los campos
              nombre_contacto = input('Agrega el Nuevo Nombre:\r\n')
              telefono_contacto = input(' Agrega el Nuevo Telefono : \r\n')
              categoria_contacto = input('Agrega la Nuevo Categoría : \r\n')

             #Instanciar la clase
              contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

             #Escribir el archivo
              archivo.write('Nombre: ' + contacto.nombre + '\r\n')
              archivo.write('Telefono: ' + contacto.telefono + '\r\n')
              archivo.write('Categoría: ' + contacto.categoria + '\r\n')

              #Cerrar el archivo
              archivo.close()


              #Renombrar archivo
              os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION) 

              #Mostrar mensaje de éxito
              print('\r\n Contacto creado Correctamente \r\n')


        else:
            print('Ese contacto no existe')


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto) 
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w' ) as archivo:

            #resto de los campos
            telefono_contacto = input('Agrega el Telefono: \r\n')
            categoria_contacto = input('Categoría Contacto: \r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #mostrar mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')

    else:
        print('Ese Contacto ya existe')

    # Reiniciar la app
    app()


def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        # crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)       
app()