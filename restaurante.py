from producto import Producto


class Restaurante():
    def __init__(self, name: str, productos: list[Producto]) -> None:
        self.name = name        
        self.productos = productos        