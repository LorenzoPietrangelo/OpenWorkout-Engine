from pydantic import BaseModel, Field, field_validator

from exercise_model import Muscolo, Attrezzo, Categoria


#modelli di input

class RichiestaScheda(BaseModel):
    giorni: list[int] = Field(min_length=1, max_length=7,
                              description="Giorni di allenamento (1 = lunedì, 7 = domenica)",
                              examples=[[1, 2, 4, 5, 6]])
    priorita_muscoli: list[Muscolo] = Field(min_length=1,
                                            description="Muscoli in ordine di priorità",
                                            examples=[["chest", "lats", "upper back", "quads",
                                                       "hamstrings", "side delts", "triceps",
                                                       "biceps", "glutes", "adductors"]])
    max_minuti: int = Field(gt=0, description="Durata massima di ogni allenamento in minuti",
                            examples=[60])
    attrezzi_disponibili: list[Attrezzo] | None = Field(
        default=None, description="Attrezzi disponibili; null = tutti")

    @field_validator("giorni")
    @classmethod
    def giorni_validi(cls, giorni):
        if any(g < 1 or g > 7 for g in giorni):
            raise ValueError("i giorni devono essere compresi tra 1 e 7")
        if len(set(giorni)) != len(giorni):
            raise ValueError("i giorni non possono ripetersi")
        return sorted(giorni)

    @field_validator("priorita_muscoli")
    @classmethod
    def muscoli_unici(cls, muscoli):
        if len(set(muscoli)) != len(muscoli):
            raise ValueError("i muscoli non possono ripetersi")
        return muscoli


#modelli di output

class Intervallo(BaseModel):
    min: int
    max: int


class VoceEsercizio(BaseModel):
    nome: str
    serie: int
    ripetizioni: Intervallo | None
    recupero_minuti: Intervallo | None
    scoperto: bool


class Giorno(BaseModel):
    giorno: int
    muscoli: list[Muscolo]
    durata_minuti: float
    supera_limite: bool
    esercizi: list[VoceEsercizio]


class Scheda(BaseModel):
    giorni: list[Giorno]
    avvisi: list[str]


class InfoEsercizio(BaseModel):
    nome: str
    muscoli_primari: list[Muscolo]
    muscoli_secondari: list[Muscolo]
    categoria: Categoria
    attrezzi: list[Attrezzo]
    monolaterale: bool
