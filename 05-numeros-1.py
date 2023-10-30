"""funcción para sumar diferentes numeros aquí creamos la funcción 
y le pasamos los parametro a y b pero le asignamos un valor por defecto
 en caso de no asignarle ningun valor y pues siempre que la llamemos 
  podemos reasignarle un valor  """

#suma
def suma(a=0,b=0):
    print(a+b)

suma(3,4)
suma(2)

#resta
def resta(a=0,b=0):
    print(a-b)

resta(4,3)

#multiplicación
def mult(a=0,b=0):
    print(a*b)

mult(2,4)

#división
def div(a=0,b=0):
    print(a/b)

div(30,3)
