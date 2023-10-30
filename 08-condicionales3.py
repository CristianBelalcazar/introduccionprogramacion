# Operadores and y or (y) & (o)

usuario_logueado = False
usuario_admin =  False

# and sirve para evaluar las condicciones y se tiene que cumplir las 2 para ser verdaderas

if usuario_logueado and usuario_admin:
    print('Acceso Total')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar seccion')

# o Con solo que se cumpla una de las condiciones es verdadera

if usuario_logueado or usuario_admin:
    print('Acceso Total')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar seccion')