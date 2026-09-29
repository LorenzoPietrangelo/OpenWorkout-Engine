from dataclasses import dataclass, field
from enum import Enum

class Livello(Enum):
    PRINCIPIANTE = "principiante"
    INTERMEDIO = "intermedio"
    AVANZATO = "avanzato"


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


# regioni muscolari, usate solo dal livello avanzato al posto del muscolo intero
class Regione(Enum):
    STERNOCOSTALI = "sternocostali"
    CLAVICOLARI = "clavicolari"
    ILIACI = "iliaci"
    TORACICI = "toracici"
    BICIPITE_BRACHIALE = "bicipite brachiale"
    BRACHIORADIALE = "brachioradiale"
    TRICIPITE_BRACHIALE = "tricipite brachiale"
    CAPI_MONOARTICOLARI = "capi monoarticolari del tricipite brachiale"
    GRANDE_GLUTEO = "grande gluteo"
    MEDIO_GLUTEO = "medio gluteo"


REGIONI = {
    Muscolo.CHEST: [Regione.STERNOCOSTALI, Regione.CLAVICOLARI],
    Muscolo.LATS: [Regione.ILIACI, Regione.TORACICI],
    Muscolo.BICEPS: [Regione.BICIPITE_BRACHIALE, Regione.BRACHIORADIALE],
    Muscolo.TRICEPS: [Regione.TRICIPITE_BRACHIALE, Regione.CAPI_MONOARTICOLARI],
    Muscolo.GLUTES: [Regione.GRANDE_GLUTEO, Regione.MEDIO_GLUTEO],
}
PADRE = {r: m for m, regioni in REGIONI.items() for r in regioni}


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
    MACCHINA_ABDUTTORI = "macchina abduttori"
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
    regioni: list[Regione] = field(default_factory=list)  # cosa allena per il livello avanzato
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
    muscolo: Muscolo | Regione
    tempo_riscaldamento: int = 0
    tempo_serie: int = 0

    @property
    def nome(self):
        return f"nessun attrezzo disponibile per {self.muscolo.value}"
