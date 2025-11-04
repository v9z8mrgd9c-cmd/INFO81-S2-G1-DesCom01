import datetime as dt
import random
from collections.abc import Callable

from generador_uniforme import GeneradorUniforme

ESTADO = dict()
ESTADO["estaciones"] = ["Estacion A", "Estacion B", "Estacion C"]


class Cliente:
    def __init__(self, id: int, hora_creacion: dt.datetime):
        self.id = id
        self.nombre = f"Cliente_{id}"

        self.edad = 18 + (id % 50)
        op_estaciones = ESTADO["estaciones"]
        self.destino = op_estaciones[id % len(op_estaciones)]

        self.hora_creacion = hora_creacion
        self.origen = ...
        self.delay = ...  # Cuándo vuelve.


class Estacion:
    def __init__(
        self, nombre: str, poblacion: int, hora_inicio: dt.time, hora_final: dt.time
    ):
        self.nombre = nombre
        self.poblacion = poblacion
        self.generador = GeneradorUniforme(
            poblacion, 123, dt.datetime.now(), hora_inicio, hora_final
        )
        self.clientes = []

    def generar_demanda(
        self, minutos: int, cliente_factory: Callable[[int, dt.datetime], any]
    ):
        nuevos = self.generador.generar_clientes(minutos, cliente_factory)
        self.clientes.extend(nuevos)

    def reiniciar(self):
        self.clientes = []
        # TODO: Reiniciar el generador, y actualizar la hora


def cliente_factory(id: int, hora_creacion: dt.datetime):
    return Cliente(id, hora_creacion)
