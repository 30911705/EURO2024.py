from partido import Partido


class Boleto:
    def __init__(self, id: int, asiento: int, cliente_ci: int, partido: Partido) -> None:
        self.id = id
        self.precio = 0
        self.asiento = asiento
        self.cliente_ci = cliente_ci
        self.partido = partido
        self.asistio = False

class Boleto_vip(Boleto):
    def __init__(self, id: int, asiento: int, cliente_ci: int, partido: Partido) -> None:
        super().__init__(id, asiento, cliente_ci, partido)
        self.precio = 75
        self.asistio = False
        


class Boleto_general(Boleto):
    def __init__(self, id: int, asiento: int, cliente_ci: int, partido: Partido) -> None:
        super().__init__(id, asiento, cliente_ci, partido)
        self.precio = 35
        self.asistio = False
        