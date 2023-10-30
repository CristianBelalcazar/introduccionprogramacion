class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio
       

    def mostrar_informacion(self):
        print(f'Nombre: { self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')
        


#Instanciar la clase
restaurant =  Restaurant('pizzas marce', 'Comida italiana',26000)
restaurant.mostrar_informacion()

#aquí creamos otra clase con los datos del 1 objeto ya que para eso son los objetos
restaurant2 =  Restaurant('Hamburguesas cris', 'Comida rapida',12000)
restaurant2.mostrar_informacion()
    
"""La astracción es saber que datos sno necesitarios en esa clase ejemplo
 def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio
          y que datos son necesarios en esos objetos 
          restaurant =  Restaurant('pizzas marce', 'Comida italiana',26000)
restaurant.mostrar_informacion()

#aquí creamos otra clase con los datos del 1 objeto ya que para eso son los objetos
restaurant2 =  Restaurant('Hamburguesas cris', 'Comida rapida',12000)
restaurant2.mostrar_informacion()"""

