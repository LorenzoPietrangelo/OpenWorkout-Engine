from engine import build_week, assegna_esercizi, calcola_serie, durata_con_serie
from execises import esercizi

from exercise_model import Muscolo

if __name__ == "__main__":

    days_selected=[1,3,5]
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
    max_minuti = 20  # tempo massimo per allenamento in minuti
    week = build_week(days_selected, muscle_priority)
    scheda = assegna_esercizi(week, muscle_priority, esercizi)
    scheda_con_serie = calcola_serie(scheda, max_minuti)                 # 3. numero di serie

    print("--------------------------------------------------------------------------------")

    for day, muscoli in week.items():
        print(f"Giorno {day}:", ", ".join(muscolo.value for muscolo in muscoli))

    print("--------------------------------------------------------------------------------")

    for day, workout in scheda.items():
        print(f"Giorno {day}:", ", ".join(esercizio.nome for esercizio in workout))

    print("--------------------------------------------------------------------------------")

    for day, workout in scheda_con_serie.items():
        print(f"Giorno {day} ({durata_con_serie(workout):.0f} min):",
              ", ".join(f"{e.nome} x{s}" for e, s in workout))