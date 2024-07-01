from boleto import Boleto


def asistencia_al_partido(boletos: list[Boleto]):
    while True:
        try:
            boleto = preguntar_id_boleto(boletos)
            if boleto is None:
                break

            print(f"Su asistencia al partido {boleto.cliente_ci.number} a sido confirmada exitosamente")
            break
        except:
            print("Ha ocurrido un error en asistencia al partido")

def preguntar_id_boleto(boletos: list[Boleto]):
    while True:
        try:
            id = int(input("Ingrese id de su boleto: "))
            for boleto in boletos:
                if id == boleto.id and not boleto.asistio:
                    boletos.remove(boleto)
                    boleto.asistio = True
                    boletos.append(boleto)
                    return boleto
            
            probar_otra_vez=input('''Boleto no encontrado o ya usado ¿Probaras con otro id?
1.- Si
2.- No
> ''')
            if probar_otra_vez == "2":
                return None

        except:
            print("error")
