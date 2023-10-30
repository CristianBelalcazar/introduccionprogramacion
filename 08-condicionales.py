# Revisa si una condición es mayor a 

dinero = 100.000

if dinero >0:
    print('Puedes pagar el taxi')
else:
    print('No tienes dinero')

# Revisa si una condición es igual(==) a 

likes = 200  # el igual de aqui es para asgnar valor
if likes == 200: # los 2 iguales aquí son para comparar condiciones
    print('Excelente,200 Likes')

# Revisa si una condición es mayor o igual (>=) a

edad = 18
if edad >=18:
    print('Eres mayor de edad')
else:
    print('ya casi eres mayor de edad')

# IF con texto
lenguaje = 'Python'
if lenguaje == 'Python':
    print('Excelente desicion')

# Negación (not) de la condición

usas = 'PHP'
if not usas == 'PHP':
    print('Excelente lenguaje')
else:
    print('Elige otro lenguaje como PHP')

#Boolean Falso o verdadero (False o True)

usuario_autenticado =True
if usuario_autenticado: # no usamos == True ya que por defecto python ya evalua está condición
    print('Bienvenido al sistema')

else:
    print('Debes iniciar seccion')


# Evaluar un elemnto de una list

lenguajes = ['Python','Kotlin','Java','Javascript','PHP']
if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('No esta en la lista')

#IF Anidado
usuario_autenticado =False
usuario_admin = False
if usuario_autenticado: 
    if usuario_admin:
        print('Bienvenido Tienes Acceso Total')
    else:
         print('Bienvenido al sistema')

else:
     print('Debes iniciar seccion')