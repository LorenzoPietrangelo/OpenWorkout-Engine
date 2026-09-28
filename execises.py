from exercise_model import Esercizio, Categoria, Muscolo, Attrezzo
esercizi = [
    Esercizio("Pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_PEC_FLY]),
    Esercizio("Dumbell fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_PEC_FLY]),
    
    Esercizio("Cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbell row", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    
    Esercizio("Wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Wide grip dumbell row", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell skull crusher", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    
    Esercizio("Leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_EXTENSION]),
    Esercizio("Sissy squat", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_EXTENSION]),
    
    Esercizio("Leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_CURL]),
    Esercizio("Nordic curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Single leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_CURL]),
    
    Esercizio("Leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_PRESS]),
    Esercizio("Dumbbell squat", [Muscolo.GLUTES,Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.QUADS], monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_PRESS]),
    
    Esercizio("Barbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE]),
    Esercizio("Dumbbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg barbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, muscoli_secondari=[Muscolo.HAMSTRINGS], monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE]),

    
    Esercizio("Adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ADDUTTORI]),
    Esercizio("Copenaghen plank", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Single leg adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ADDUTTORI]),

    Esercizio("Barbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE, Attrezzo.PANCA]),
    Esercizio("Dumbbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg barbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE, Attrezzo.PANCA]),
]
