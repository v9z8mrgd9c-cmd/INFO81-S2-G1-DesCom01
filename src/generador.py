import datetime as dt
import random
# La versión uniforme:
# P: Población
# Cpm:    P * 0.2 / MINUTOS

POBLACION = 100_000

HORAS = dt.time(20, 0).hour - dt.time(7, 0).hour
MINUTOS = HORAS * 60
print(MINUTOS)

CPM = POBLACION * 0.2 / MINUTOS


class Cliente:
    def __init__(self, hora_creacion: dt.datetime):
        self.hora_creacion = hora_creacion
        self.destino = ...
        self.origen = ...
        self.delay = ...  # Cuándo vuelve.
        self.id = ...
        self.nombre = ...
        self.edad = ...


class Generador:
    def __init__(self, hora_inicio: dt.time, hora_final: dt.time):
        ...
        ...
        self.rdm = random.Random(123)

    def generar_clientes(self, minutos: int):
        size = int(minutos * CPM)
        return [Cliente(dt.datetime.now())] * size


class Estacion:
    def __init__(self, nombre: str, hora_inicio: dt.time, hora_final: dt.time):
        self.nombre = nombre
        self.generador = Generador(hora_inicio, hora_final)


if __name__ == "__main__":
    estacion1 = Estacion("Ferroviario Valdivia", dt.time(7, 0), dt.time(20, 0))
    generador = estacion1.generador
    res = generador.generar_clientes(10)
    print("Clientes:", len(res))

    res = generador.generar_clientes(MINUTOS)
    print("Min:", POBLACION * 0.19)
    print("Clientes:", len(res))
    print("Max:", POBLACION * 0.21)
    assert POBLACION * 0.19 <= len(res) <= POBLACION * 0.21
