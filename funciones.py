from partido import Partido


def get_partido(partidos: list[Partido], id_partido):
    for p in partidos:
        if p.id == id_partido:
            return p
