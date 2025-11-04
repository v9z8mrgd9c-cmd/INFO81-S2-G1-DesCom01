import datetime as dt
import random
from collections.abc import Callable


class Generador:
    def __init__(
        self,
        poblacion: int,
        seed=123,
        fecha_inicial: dt.datetime = dt.datetime(2025, 1, 1),
        hora_apertura: dt.time = dt.time(7, 0),
        hora_cierre: dt.time = dt.time(20, 0),
    ):
        self.poblacion = poblacion
        self.seed = seed
        self.rdm = random.Random(seed)

        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

        self.current_datetime: dt.datetime = fecha_inicial

    def minutos_de_funcionamiento(self):
        horas = self.hora_cierre.hour - self.hora_apertura.hour
        return horas * 60

    def generar_clientes(
        self,
        minutos: int,
        constructor: Callable[[int, dt.datetime], any],
        update: bool = True,
    ):
        if update:
            self.current_datetime += dt.timedelta(minutes=minutos)

        cpm = self.poblacion * 0.2 / self.minutos_de_funcionamiento()
        size = int(minutos * cpm)
        clientes = []
        for _ in range(size):
            val = self.rdm.randint(0, 2_000_000)
            cliente = constructor(val, self.current_datetime)
            clientes.append(cliente)
        return clientes
