 #diferencia entre funcción y metodo

#este es una variable
nombre_usu = 'cris'

#creamos una funcción y le asignamos como parametro guardar los datos que tenga la variable nombre_usu
def mostrar_nombre(nombre_usu):
    print(f'Hola {nombre_usu}')

mostrar_nombre(nombre_usu) #Todo esto es una funcción

print(nombre_usu.upper()) #el metodo es lo que vemos seguido del . ya que es algo definido por el lenguaje

print(nombre_usu.title())



def mensaje():
    print( " Bienvenido")

mensaje()

def mensajes(nombre):
    return nombre

usuario = mensajes('cris')
print("Bienvenido " + usuario)
