from restaurante import Restaurante


class Estadio():
    def __init__(self, id: str,name: str,city: str,capacity: list[int],restaurantes: list[Restaurante]) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurantes = restaurantes
    
    def __str__(self):
        return f'name: {self.name}'
    
    def get_productos(self):
        productos = []
        for restaurante in self.restaurantes:
            for producto in restaurante.productos:
                productos.append(producto)

        return productos