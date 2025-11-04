__version__ = "1.0.0"
__license__ = "MIT"
from .generador import Generador
from .generadores.generador_uniforme import GeneradorUniforme

# Define public API
__all__ = [
    # Core classes
    "Generador",
    "GeneradorUniforme",
    # Metadata
    "__version__",
]
