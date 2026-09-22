from dataclasses import dataclass, field
from enum import Enum

class Categoria(Enum):
    ISOLAMENTO = "isolamento"
    COMPOUND_UPPER = "compound upper"
    COMPOUND_GAMBE = "compound gambe"


class Muscolo(Enum):
    CHEST = "chest"
    LATS = "lats"
    UPPER_BACK = "upper back"
    SIDE_DELTS = "side delts"
    TRICEPS = "triceps"
    BICEPS = "biceps"
    QUADS = "quads"
    HAMSTRINGS = "hamstrings"
    GLUTES = "glutes"
    ADDUCTORS = "adductors"
    
@dataclass
class Esercizio:
    nome: str
    muscoli_primari: list[Muscolo]
    categoria: Categoria
    tempo_riscaldamento: int
    tempo_serie: int
    muscoli_secondari: list[Muscolo] = field(default_factory=list)
    monolaterale: bool = False

