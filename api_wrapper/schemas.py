from pydantic import BaseModel, Field, field_validator, model_validator

from exercise_model import Muscolo, Attrezzo, Categoria, Livello, Regione, REGIONI


#modelli di input

class RichiestaScheda(BaseModel):
    giorni: list[int] = Field(min_length=1, max_length=7,
                              description="Giorni di allenamento (1 = lunedì, 7 = domenica)",
                              examples=[[1, 2, 4, 5, 6]])
    priorita_muscoli: list[Muscolo | Regione] = Field(
        min_length=1,
        description="Muscoli in ordine di priorità; con il livello avanzato chest, lats, biceps, "
                    "triceps e glutes vanno indicati tramite le loro regioni",
        examples=[["chest", "lats", "upper back", "quads", "hamstrings", "side delts",
                   "triceps", "biceps", "glutes", "adductors"]])
    max_minuti: int = Field(gt=0, description="Durata massima di ogni allenamento in minuti",
                            examples=[60])
    attrezzi_disponibili: list[Attrezzo] | None = Field(
        default=None, description="Attrezzi disponibili; null = tutti")
    superserie: bool = Field(
        default=False,
        description="Se il tempo non basta, unisce gli esercizi di isolamento in superserie")
    monolaterali: bool = Field(
        default=False,
        description="Se il tempo avanza, sostituisce gli esercizi con la variante monolaterale")
    livello: Livello = Field(
        default=Livello.PRINCIPIANTE,
        description="Livello di esperienza: determina ripetizioni, recuperi e RIR")

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

    @model_validator(mode="after")
    def regioni_per_livello(self):
        if self.livello == Livello.AVANZATO:
            interi = [m.value for m in self.priorita_muscoli if m in REGIONI]
            if interi:
                raise ValueError("con il livello avanzato questi muscoli vanno indicati tramite "
                                 f"le loro regioni: {', '.join(interi)}")
        elif any(isinstance(m, Regione) for m in self.priorita_muscoli):
            raise ValueError("le regioni muscolari sono disponibili solo con il livello avanzato")
        return self


#modelli di output

class Intervallo(BaseModel):
    min: int | float
    max: int | float


class VoceEsercizio(BaseModel):
    nome: str
    serie: int
    ripetizioni: Intervallo | None
    recupero_minuti: Intervallo | None
    rir: Intervallo | None
    scoperto: bool


class Giorno(BaseModel):
    giorno: int
    muscoli: list[Muscolo | Regione]
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
    regioni: list[Regione]
    categoria: Categoria
    attrezzi: list[Attrezzo]
    monolaterale: bool
