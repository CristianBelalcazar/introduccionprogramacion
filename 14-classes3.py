class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public, PROTECTED, PRIVATE
       

    def mostrar_informacion(self):
        print(f'Nombre: { self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    #GETTERS y SETTERS - Get = Obtiene un valor, SET = Agrega un valor

    def get_precio(self): # nos permiten obtene el valor 
        print(self.__precio)

    def set_precio(self, precio): #modifica el valor
        self.__precio = precio
        


#Instanciar la clase
restaurant =  Restaurant('pizzas marce', 'Comida italiana',50)

restaurant.__precio = 80 # No será posible modificarlo con PRIVATE
restaurant.mostrar_informacion()
restaurant.set_precio(90) #modifica el valor
restaurant.get_precio() #Nos mostrara el dato

#aquí creamos otra clase con los datos del 1 objeto ya que para eso son los objetos
restaurant2 =  Restaurant('Hamburguesas cris', 'Comida rapida',20)

restaurant2.__precio = 40
restaurant2.mostrar_informacion()
restaurant2.set_precio(50)  #modifica el valor
restaurant2.get_precio()#Nos mostrara el dato

"""El encasulamiento de codigo sirve para proteger tu codigo en ciertos lugares para que 
no puedan acceder a el, depende de como lo tengas declarada tu clase
si es public todos pueden acceder a ella, si es protected se le pone un un _ seguido
 del nombre en este caso es _precio hace exactamente que el public y el diferente seria private
 ya que ese si no permite que puedan  modificar  el dato guardado y se asigna con 2 __ 
 seguido del nombre en este caso es __precio  y siempre se llama para acceder a el de acuerdo como lo 
 declaramos """