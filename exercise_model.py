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


class Attrezzo(Enum):
    MANUBRI = "manubri"
    BILANCIERE = "bilanciere"
    PANCA = "panca"
    CAVI = "cavi"
    MACCHINA_PEC_FLY = "macchina pec fly"
    MACCHINA_LEG_EXTENSION = "macchina leg extension"
    MACCHINA_LEG_CURL = "macchina leg curl"
    MACCHINA_LEG_PRESS = "macchina leg press"
    MACCHINA_ADDUTTORI = "macchina adduttori"
    MULTIPOWER = "multipower"
    LAT_MACHINE = "lat machine"
    TBAR = "t-bar"
    

@dataclass
class Esercizio:
    nome: str
    muscoli_primari: list[Muscolo]
    categoria: Categoria
    tempo_riscaldamento: int
    tempo_serie: int
    muscoli_secondari: list[Muscolo] = field(default_factory=list)
    monolaterale: bool = False
    attrezzi: list[Attrezzo] = field(default_factory=list)  # lista vuota = corpo libero


@dataclass
class SuperSerie:
    """Due esercizi di isolamento eseguiti in successione con un unico recupero."""
    primo: Esercizio
    secondo: Esercizio

    @property
    def esercizi(self):
        return (self.primo, self.secondo)

    @property
    def nome(self):
        return f"{self.primo.nome} + {self.secondo.nome}"

    @property
    def categoria(self):
        return self.primo.categoria

    @property
    def tempo_riscaldamento(self):
        return self.primo.tempo_riscaldamento + self.secondo.tempo_riscaldamento

    @property
    def tempo_serie(self):
        return self.primo.tempo_serie + self.secondo.tempo_serie


@dataclass(frozen=True)
class MuscoloScoperto:
    """Segnaposto: nessun esercizio eseguibile con gli attrezzi disponibili."""
    muscolo: Muscolo
    tempo_riscaldamento: int = 0
    tempo_serie: int = 0

    @property
    def nome(self):
        return f"nessun attrezzo disponibile per {self.muscolo.value}"
