from exercise_model import Esercizio, Categoria, Muscolo, Attrezzo
esercizi = [
    Esercizio("Pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_PEC_FLY]),
    Esercizio("Dumbell fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbell row", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Wide grip dumbell row", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),

    Esercizio("Cable bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell skull crusher", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),

    Esercizio("Cable lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO,monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_EXTENSION]),
    Esercizio("Sissy squat", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_CURL]),
    Esercizio("Nordic curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    
    Esercizio("Leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_PRESS]),
    Esercizio("Dumbbell squat", [Muscolo.GLUTES,Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Barbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE]),
    Esercizio("Dumbbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    
    Esercizio("Adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ADDUTTORI]),
    Esercizio("Copenaghen plank", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    
    Esercizio("Barbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE, Attrezzo.PANCA]),
    Esercizio("Dumbbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
]
