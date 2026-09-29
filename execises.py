from exercise_model import Esercizio, Categoria, Muscolo, Attrezzo, Regione
esercizi = [
    Esercizio("Pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, regioni=[Regione.STERNOCOSTALI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_PEC_FLY]),
    Esercizio("Dumbell fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, regioni=[Regione.STERNOCOSTALI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Low to high cable fly", [], Categoria.ISOLAMENTO, regioni=[Regione.CLAVICOLARI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Incline dumbbell fly", [], Categoria.ISOLAMENTO, regioni=[Regione.CLAVICOLARI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI, Attrezzo.PANCA]),
    Esercizio("Single arm low to high cable fly", [], Categoria.ISOLAMENTO, regioni=[Regione.CLAVICOLARI], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Single arm pec fly", [Muscolo.CHEST], Categoria.ISOLAMENTO, regioni=[Regione.STERNOCOSTALI], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_PEC_FLY]),
    
    Esercizio("Cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, regioni=[Regione.ILIACI], muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbell row", [Muscolo.LATS], Categoria.COMPOUND_UPPER, regioni=[Regione.ILIACI], muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Lat machine", [Muscolo.LATS], Categoria.COMPOUND_UPPER, regioni=[Regione.TORACICI], muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.LAT_MACHINE]),
    Esercizio("Single arm lat machine", [Muscolo.LATS], Categoria.COMPOUND_UPPER, regioni=[Regione.TORACICI], muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.LAT_MACHINE]),
    Esercizio("Single arm cable pulley", [Muscolo.LATS], Categoria.COMPOUND_UPPER, regioni=[Regione.ILIACI], muscoli_secondari=[Muscolo.UPPER_BACK, Muscolo.BICEPS], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    
    Esercizio("Wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Wide grip dumbell row", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm wide grip pulley", [Muscolo.UPPER_BACK], Categoria.COMPOUND_UPPER, muscoli_secondari=[Muscolo.LATS, Muscolo.BICEPS], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, regioni=[Regione.BICIPITE_BRACHIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, regioni=[Regione.BICIPITE_BRACHIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Cable hammer curl", [], Categoria.ISOLAMENTO, regioni=[Regione.BRACHIORADIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell hammer curl", [], Categoria.ISOLAMENTO, regioni=[Regione.BRACHIORADIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable hammer curl", [], Categoria.ISOLAMENTO, regioni=[Regione.BRACHIORADIALE], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Single arm cable bicep curl", [Muscolo.BICEPS], Categoria.ISOLAMENTO, regioni=[Regione.BICIPITE_BRACHIALE], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.TRICIPITE_BRACHIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell skull crusher", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.TRICIPITE_BRACHIALE], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Overhead cable extension", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.CAPI_MONOARTICOLARI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell overhead extension", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.CAPI_MONOARTICOLARI], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm overhead cable extension", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.CAPI_MONOARTICOLARI], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Single arm cable push down", [Muscolo.TRICEPS], Categoria.ISOLAMENTO, regioni=[Regione.TRICIPITE_BRACHIALE], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),

    Esercizio("Cable lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Dumbbell lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single arm cable lateral raise", [Muscolo.SIDE_DELTS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    
    Esercizio("Leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_EXTENSION]),
    Esercizio("Sissy squat", [Muscolo.QUADS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg extension", [Muscolo.QUADS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_EXTENSION]),
    
    Esercizio("Leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_CURL]),
    Esercizio("Nordic curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Single leg curl", [Muscolo.HAMSTRINGS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_CURL]),
    
    Esercizio("Leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_PRESS]),
    Esercizio("Dumbbell squat", [Muscolo.GLUTES,Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.QUADS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg press", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.QUADS], monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_LEG_PRESS]),
    
    Esercizio("Barbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE]),
    Esercizio("Dumbbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.HAMSTRINGS], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg barbell SLDL", [Muscolo.GLUTES, Muscolo.ADDUCTORS], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], muscoli_secondari=[Muscolo.HAMSTRINGS], monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE]),

    
    Esercizio("Adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ADDUTTORI]),
    Esercizio("Copenaghen plank", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, tempo_riscaldamento=3, tempo_serie=1),
    Esercizio("Single leg adductor machine", [Muscolo.ADDUCTORS], Categoria.ISOLAMENTO, monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ADDUTTORI]),

    Esercizio("Barbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE, Attrezzo.PANCA]),
    Esercizio("Dumbbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.MANUBRI]),
    Esercizio("Single leg barbell hip thrust", [Muscolo.GLUTES], Categoria.COMPOUND_GAMBE, regioni=[Regione.GRANDE_GLUTEO], monolaterale=True, tempo_riscaldamento=5, tempo_serie=1, attrezzi=[Attrezzo.BILANCIERE, Attrezzo.PANCA]),

    Esercizio("Abductor machine", [], Categoria.ISOLAMENTO, regioni=[Regione.MEDIO_GLUTEO], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ABDUTTORI]),
    Esercizio("Cable hip abduction", [], Categoria.ISOLAMENTO, regioni=[Regione.MEDIO_GLUTEO], tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
    Esercizio("Single leg abductor machine", [], Categoria.ISOLAMENTO, regioni=[Regione.MEDIO_GLUTEO], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.MACCHINA_ABDUTTORI]),
    Esercizio("Single leg cable hip abduction", [], Categoria.ISOLAMENTO, regioni=[Regione.MEDIO_GLUTEO], monolaterale=True, tempo_riscaldamento=3, tempo_serie=1, attrezzi=[Attrezzo.CAVI]),
]
