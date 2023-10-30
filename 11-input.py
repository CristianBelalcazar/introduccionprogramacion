# input = es una función para que el usuario escriba 
#nombre = input('Cuale es tu nombre: \r\n') # \r\n sirven para salto de linea

#print(f'Hola {nombre}')

#entrada de numeros
edad = input('Cual es su edad: ') 
#siempre que necesitemos los datos en numero debemos usar un convertidor ya que input espera un string

# Convertidor a entero o numero
edad = int(edad)

if edad >=18:
    print('Ya Puedes votar')
else:
    print('Aun no puedes votar ')

# Mezclarlo con operadores

numero = input('Agrega un numero y te dire si es par o impar:  \r\n')
numero = int(numero)

if numero % 2 == 0: # el % sirve para quitar el reciduo de una división
    print(f'El número {numero} es par')
else:
    print( f'El número {numero } es impar ')
