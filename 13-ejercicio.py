playlist = {} #diccionario vacio
playlist['canciones'] = [] #lista vacía de canciones 


#funcción principal 
def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist? \r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #ya tenemos un nombre desativar true


            agregar_playlist=False

            agregar_canciones()
def agregar_canciones():
   #Bandera para agregar canciones
   agregar_cancion = True
    
 

   while agregar_canciones:
        #pregunarle al usuario que canción desean agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agregue canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
             # Dejar de agregar canciones
             agregar_cancion = False
             mostrar_resumen()
             break
             
        else:
               # Agregar las canciones a las playlist
              playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')

    for cancion in playlist['canciones']:
        print(cancion)

app()




