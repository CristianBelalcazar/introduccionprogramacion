pregunta = 'Agrega un numero y te diré si es par o impar:  \r\n'
pregunta += ' (Escribe "X" para salir de la plicación) \r\n'

preguntar = True

while preguntar:

  # Mezclarlo con operadores

   numero = input(pregunta)

   if numero == 'X':
       preguntar = False
   else:
        numero = int(numero)
       
        if numero % 2 == 0: # el % sirve para quitar el reciduo de una división
            print(f'El número {numero} es par')
        else:
             print( f'El número {numero } es impar ')
