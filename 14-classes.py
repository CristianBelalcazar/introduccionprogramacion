class Restaurant:
    
    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo

    def mostrar_informacion(self):
        print(f'Nombre: { self.nombre}')
        


#Instanciar la clase
restaurant =  Restaurant()
restaurant.agregar_restaurant('pizzas marce')
restaurant.mostrar_informacion()

#aquí creamos otra clase con los datos del 1 objeto ya que para eso son los objetos
restaurant2 =  Restaurant()
restaurant2.agregar_restaurant('Hamburguesas cris')
restaurant2.mostrar_informacion()
    

#Mostrar la información de otra manera
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')