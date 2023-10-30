# dictionary son lo que conocemos como objetos en otros lenguajes 
"""Se usa siempre con {} y dentro ponemos los datos y asignamos su valor
en este caso las llaves son artista separada de su valor que es Generación12 si vamos añadir
más ponemos una coma y seguimos escribiendo, y se pueden poner diferentes valores """

cancion = {
    'artista' : 'Generacion 12', # llave y valor
    'cancion' : 'Obra  de tu amor',
    'lanzamiento': 2023,
    'linkes': 5.6
}

print(cancion) # nos mostrara todos los datos 
"""Accederemos a la llave en este caso es artista y nos dara el valor 
Guardado en artista en este caso es Generación 12"""
print(cancion['artista']) 

"""Mezclar con un String  el dictionary y para ello debemos de asinar 
los datos del diccionario en una nueva variable"""

musica = cancion['artista'] #pasamo directamente el dato del diccionario a la variable
print(f'Estoy escuchando a {musica}') #convinamos el string con el dato de la nueva variable del diccionario
print(cancion) 

#agregar nuevos valores

cancion ['nueva'] = 'Jesus mesias' #usamos el nombre del diccinario y entre[] ponemos la llava y el = asignamos su valor
print(cancion)

# Reemplazar un valor

cancion ['cancion'] = 'Cristo te amo' # debe existir la llave para poderlo remplazar en este caso si existe la llave cancion
print(cancion)

# Eliminar un valor 
del cancion['lanzamiento']
print(cancion)

