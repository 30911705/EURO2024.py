class Producto:
    def __init__(self, name: str, quantity: int,price: str,stock: int,adicional: str) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional
    
    def __str__(self):
        return f"nombre: {self.name} precio: {self.price}"
    
    def descontar_una_unidad(self):
        if self.quantity > 0:
            self.quantity -= 1
        elif self.stock > 0:
            self.stock -= 1
        else:
            print("No hay stock")

    def obtener_precio(self):
        return self.price*0.16 + self.price

class Bebida(Producto):
    def __init__(self, name: str, quantity: int, price: str, stock: int, adicional: str) -> None:
        super().__init__(name, quantity, price, stock, adicional)

class Alimento(Producto):
    def __init__(self, name: str, quantity: int, price: str, stock: int, adicional: str) -> None:
        super().__init__(name, quantity, price, stock, adicional)