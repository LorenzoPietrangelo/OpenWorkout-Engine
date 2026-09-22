from exercise_model import Esercizio, Categoria, Muscolo
esercizi = [
    Esercizio("Pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Dumbbell bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Dumbbell lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1),
    Esercizio("SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1),
    Esercizio("Adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, tempo_riscaldamento=5, tempo_serie=1),
]