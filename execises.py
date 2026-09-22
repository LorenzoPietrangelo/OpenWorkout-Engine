from exercise_model import Esercizio, Categoria, Muscolo
esercizi = [
    Esercizio("Pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO),
    Esercizio("Cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, [Muscolo.UPPER_BACK, Muscolo.BICEPS]),
    Esercizio("Wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, [Muscolo.LATS, Muscolo.BICEPS]),
    Esercizio("Dumbbell bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, monolaterale=True),
    Esercizio("Cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO),
    Esercizio("Dumbbell lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO),
    Esercizio("Leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO),
    Esercizio("Leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO),
    Esercizio("Leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, [Muscolo.QUADS]),
    Esercizio("SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, [Muscolo.HAMSTRINGS]),
    Esercizio("Adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO),
    Esercizio("Hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE),
]