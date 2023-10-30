#supongamos que tenemos un juego pero no sabemos los datos del jugador

#iniciar un diccionario vacío

jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'cris'# se va llenando el objeto o diccionario
print(jugador) 

jugador['puntaje'] = 0
print(jugador) 

#incrementa el puntaje
jugador['puntaje'] = 100
print(jugador) 

#incrementa el puntaje
jugador['puntaje'] = 200
print(jugador) 

#Acceder a un valor
print(jugador.get('consola')) #si el valor no existe me sala none

print(jugador.get('consola', 'No existe ese valor')) #cambiamos el mensaje none por No existe ese valor

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)




