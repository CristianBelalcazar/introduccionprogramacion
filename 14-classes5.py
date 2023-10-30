class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio # Default: Public, PROTECTED, PRIVATE
       

    def mostrar_informacion(self):
        print(f'Nombre: { self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    #GETTERS y SETTERS - Get = Obtiene un valor, SET = Agrega un valor

    def get_precio(self): # nos permiten obtene el valor 
        print(self.precio)

    def set_precio(self, precio): #modifica el valor
        self.precio = precio
        
# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    
    #Reescribir un método (Debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: { self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')

        #Agregar un metodo que solo exista en hotel
    def get_alberca(self):
       return self.alberca

hotel = Hotel('Hotel Cris', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)

"""El polimorfismo es una manera de pasar datos y añadirle nuevas a un objeto dependiendo
de lo que necesites hacer, puedes añadirles nuevos datos en este caso nosotros lo hicimos 
con alberca"""



