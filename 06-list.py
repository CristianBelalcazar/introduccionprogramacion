"""en python los arreglos sé les conoce como List a diferencia de otros lenguajes de 
programación pero funciona igualmente y siempre se hacen dentro de llaves[]"""


lenguajes = ['Python','Kotlin','Java','Javascript'] #este es un arreglo o list
print(lenguajes) 

# Los arrays (list) comienzan en la posición numero 0

print(lenguajes[0]) #nos mostrara python porque esta en la posición numero 0

# Ordena los elemtos de la list en orden alfabetica con .sort()

lenguajes.sort()
print(lenguajes) # nos mostrara java de primero ya que es en el orden alfabetico

#Vamos a crear una variable y le pasamos un dato de nuestro arreglo

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificando valores en un arreglo 
lenguajes[2] = 'PHP' #vamos a reemplazar kotlin por php
print(lenguajes)

#añadir o agregar un nuevo elemento a un arreglo usamos .append() y dentro ponemos el dato que vamos a añadir
lenguajes.append('Ruby')

#Eliminar datos de un arreglo(list) ponemos del el nombre de la list y la posición a eliminar

del lenguajes[1] # Eliminamos javascript ya que esta en la pusición 1 del arreglo lenguajes
print(lenguajes)

#Eliminar el ultimo elemento de un arreglo (list) con .pop()
lenguajes.pop() #elimina el ultimo elemento
print(lenguajes)

"""Eliminar una posición especifica con pop pasandole la posición a eliminar"""
lenguajes.pop(0) #le pasamos la posición especifica que va eliminar en este caso es java que es la posición 0
print(lenguajes)

#Eliminar por nombre usando .remove()
lenguajes.remove('PHP')# eliminara php ya que le estamos diciendo que elimine ese elemento
print(lenguajes)