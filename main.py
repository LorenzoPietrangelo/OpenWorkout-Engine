from engine import build_week, assegna_esercizi
from execises import esercizi

from exercise_model import Muscolo

if __name__ == "__main__":

    days_selected=[1,2,5]
    muscle_priority = [
    Muscolo.CHEST,
    Muscolo.LATS,
    Muscolo.UPPER_BACK,
    Muscolo.QUADS,
    Muscolo.HAMSTRINGS,
    Muscolo.SIDE_DELTS,
    Muscolo.TRICEPS,
    Muscolo.BICEPS,
    Muscolo.GLUTES,
    Muscolo.ADDUCTORS]

    week = build_week(days_selected, muscle_priority)
    scheda = assegna_esercizi(week, muscle_priority, esercizi)

    for day, muscoli in week.items():
        print(f"Giorno {day}:", ", ".join(muscolo.value for muscolo in muscoli))

    print("--------------------------------------------------------------------------------")

    for day, workout in scheda.items():
        print(f"Giorno {day}:", ", ".join(esercizio.nome for esercizio in workout))

