import datetime as dt
import random
from collections.abc import Callable

from dummy_classes import Estacion, cliente_factory

if __name__ == "__main__":
    poblacion = 100_000
    minutos = (dt.time(20, 0).hour - dt.time(7, 0).hour) * 60

    estacion1 = Estacion(
        "Ferroviario Valdivia", poblacion, dt.time(7, 0), dt.time(20, 0)
    )
    estacion1.generar_demanda(10, cliente_factory)
    print("Clientes:", len(estacion1.clientes))

    estacion1.reiniciar()
    estacion1.generar_demanda(minutos, cliente_factory)
    res = len(estacion1.clientes)
    print("Min:", poblacion * 0.19)
    print("Clientes:", res)
    print("Max:", poblacion * 0.21)
    assert poblacion * 0.19 <= res <= poblacion * 0.21
