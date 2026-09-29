
import csv
from collections import Counter
from itertools import combinations
from exercise_model import (Esercizio, Categoria, Muscolo, Attrezzo, MuscoloScoperto, SuperSerie, Livello,
                            Regione, REGIONI, PADRE)
from execises import esercizi

MIN_REST = 2
TOP_SLOT = 4

RISCALDAMENTO_GENERALE = 10
CAMBIO_ESERCIZIO = 0.5  # minuti per passare da un esercizio all'altro in superserie

# (min, max) in minuti; per ora l'avanzato usa gli stessi valori dell'intermedio
RECUPERO = {
    Livello.PRINCIPIANTE: {Categoria.ISOLAMENTO: (2, 3),
                           Categoria.COMPOUND_UPPER: (2, 3),
                           Categoria.COMPOUND_GAMBE: (3, 4)},
    Livello.INTERMEDIO: {Categoria.ISOLAMENTO: (2, 4),
                         Categoria.COMPOUND_UPPER: (2, 4),
                         Categoria.COMPOUND_GAMBE: (3, 5)},
}
RECUPERO[Livello.AVANZATO] = RECUPERO[Livello.INTERMEDIO]

# (min, max)
RIPETIZIONI = {
    Livello.PRINCIPIANTE: {Categoria.ISOLAMENTO: (8, 10),
                           Categoria.COMPOUND_UPPER: (8, 10),
                           Categoria.COMPOUND_GAMBE: (6, 8)},
    Livello.INTERMEDIO: {Categoria.ISOLAMENTO: (6, 8),
                         Categoria.COMPOUND_UPPER: (6, 8),
                         Categoria.COMPOUND_GAMBE: (4, 6)},
}
RIPETIZIONI[Livello.AVANZATO] = RIPETIZIONI[Livello.INTERMEDIO]

RIR = {Livello.PRINCIPIANTE: (0, 0), Livello.INTERMEDIO: (0, 1), Livello.AVANZATO: (1, 2)}  # (min, max)

INTESTAZIONE = ["esercizio", "serie", "ripetizioni", "recupero", "rir"]


#insieme di metodi che generano la seettimana con i muscoli ordianti
def rispetta_recupero(giorni):
    return (all(b - a >= MIN_REST for a, b in zip(giorni, giorni[1:]))
            and (len(giorni) == 1 or 7 - giorni[-1] + giorni[0] >= MIN_REST))

# occupati = giorni delle regioni sorelle: lo stesso giorno va bene, quelli consecutivi no
def valid_combos(days, n, occupati=()):
    return [c for c in combinations(sorted(days), n)
            if rispetta_recupero(sorted(set(c) | set(occupati)))]

def giorni_sorelle(m, week):
    sorelle = REGIONI.get(PADRE.get(m), [])
    return {g for g, muscoli in week.items() if any(s in muscoli for s in sorelle)}

def best_combo(days, n, week, occupati=()):
    return min(valid_combos(days, n, occupati),
               key=lambda c: (max(len(week[g]) for g in c), sum(len(week[g]) for g in c)),
               default=None)

def depths(combo, week):
    return sorted(len(week[g]) for g in combo)

def coppia_preferibile(c2, c3, week):
    confronti = list(zip(depths(c2, week), depths(c3, week)))
    return all(a <= b for a, b in confronti) and any(a < b for a, b in confronti)

def build_week(days, muscles):
    week = {g: [] for g in days}
    for m in muscles:
        occupati = giorni_sorelle(m, week)
        c3, c2 = best_combo(days, 3, week, occupati), best_combo(days, 2, week, occupati)
        combo = c3 or c2
        if c3 and c2 and coppia_preferibile(c2, c3, week):
            combo = c2
        for g in combo or []:
            week[g].append(m)
    return week


#insieme di metodi che costruisocno la scheda sostitunedo i muscoli con esercizi
def scoperto(e):
    return isinstance(e, MuscoloScoperto)

def eseguibile(e, attrezzi):
    return attrezzi is None or set(e.attrezzi) <= set(attrezzi)

# cosa allena un esercizio: i muscoli primari, oppure (per le regioni del livello avanzato)
# le sue regioni più i primari che non hanno regioni
def copertura(e, regionale):
    if not regionale:
        return set(e.muscoli_primari)
    return set(e.regioni) | {m for m in e.muscoli_primari if m not in REGIONI}

def esercizio_per(muscolo, esercizi, attrezzi=None):
    regionale = isinstance(muscolo, Regione)
    return next((e for e in esercizi
                 if muscolo in copertura(e, regionale) and eseguibile(e, attrezzi)), None)

def isolamento_per(muscolo, esercizi, attrezzi=None):
    regionale = isinstance(muscolo, Regione)
    return next((e for e in esercizi
                 if copertura(e, regionale) == {muscolo} and eseguibile(e, attrezzi)), None)

def compound_glutei_adduttori(gluteo, secondario, esercizi, attrezzi=None):
    regionale = isinstance(gluteo, Regione)
    return next((e for e in esercizi
                 if copertura(e, regionale) == {gluteo, Muscolo.ADDUCTORS}
                 and secondario in e.muscoli_secondari
                 and eseguibile(e, attrezzi)), None)

def vicini(giorno, week):
    return [m for d in range(1, MIN_REST)
              for g in ((giorno - d - 1) % 7 + 1, (giorno + d - 1) % 7 + 1)
              for m in week.get(g, [])]

def scegli_secondario(giorno, week, priorita):
    oggi = week[giorno]
    presenti = [m for m in (Muscolo.QUADS, Muscolo.HAMSTRINGS) if m in oggi]
    if presenti:
        return max(presenti, key=oggi.index)
    ordinati = sorted((Muscolo.QUADS, Muscolo.HAMSTRINGS),
                      key=lambda m: priorita.index(m) if m in priorita else len(priorita))
    adiacenti = vicini(giorno, week)
    liberi = [m for m in ordinati if m not in adiacenti]
    return liberi[0] if liberi else None

def oppure_scoperto(e, muscolo):
    return MuscoloScoperto(muscolo) if e is None else e

def assegna_esercizi(week, priorita, esercizi, attrezzi=None):
    esercizi = [e for e in esercizi if not e.monolaterale]
    # per il livello avanzato il compound copre solo il grande gluteo, il medio resta un muscolo normale
    gluteo = Regione.GRANDE_GLUTEO if Regione.GRANDE_GLUTEO in priorita else Muscolo.GLUTES
    gambe_speciali = (gluteo, Muscolo.ADDUCTORS)
    base = {m: esercizio_per(m, esercizi, attrezzi)
            for m in priorita if m not in gambe_speciali}
    risultato = {}
    for giorno, muscoli in week.items():
        compound, slot = None, None
        if all(m in muscoli for m in gambe_speciali):
            i_g, i_a = muscoli.index(gluteo), muscoli.index(Muscolo.ADDUCTORS)
            if min(i_g, i_a) >= TOP_SLOT:
                secondario = scegli_secondario(giorno, week, priorita)
                if secondario:
                    compound = compound_glutei_adduttori(gluteo, secondario, esercizi, attrezzi)
                    slot = max(i_g, i_a)
        workout = []
        for i, m in enumerate(muscoli):
            if m in gambe_speciali:
                if compound is None:
                    workout.append(oppure_scoperto(isolamento_per(m, esercizi, attrezzi), m))
                elif i == slot:
                    workout.append(compound)
            else:
                workout.append(oppure_scoperto(base[m], m))
        risultato[giorno] = workout
    return risultato

#insieme dei metodi che regolano il numero di serie per esercizio
def componenti(e):
    return e.esercizi if isinstance(e, SuperSerie) else (e,)

def intervallo_recupero(e, livello):
    if isinstance(e, SuperSerie):
        minimo, massimo = max((intervallo_recupero(x, livello) for x in e.esercizi), key=sum)
        return minimo + CAMBIO_ESERCIZIO, massimo + CAMBIO_ESERCIZIO
    return RECUPERO[livello][e.categoria]

def recupero(e, livello):
    return sum(intervallo_recupero(e, livello)) / 2

def lati(e):
    return 2 if isinstance(e, Esercizio) and e.monolaterale else 1

def tempo_serie(e, livello):
    return 0 if scoperto(e) else lati(e) * (e.tempo_serie + recupero(e, livello))

def durata(workout, serie, livello):
    return RISCALDAMENTO_GENERALE + sum(
        e.tempo_riscaldamento + s * tempo_serie(e, livello) for e, s in zip(workout, serie))

def durata_con_serie(workout, livello):
    return durata([e for e, _ in workout], [s for _, s in workout], livello) if workout else 0

def eccesso(workout, max_minuti, livello):
    return durata(workout, [1] * len(workout), livello) - max_minuti

def giorno_peggiore(scheda, max_minuti, livello, riducibile):
    candidati = [g for g, w in scheda.items()
                 if eccesso(w, max_minuti, livello) > 0 and riducibile(w)]
    return max(candidati, key=lambda g: eccesso(scheda[g], max_minuti, livello), default=None)

def isolamenti_liberi(workout):
    return [i for i, e in enumerate(workout)
            if isinstance(e, Esercizio) and e.categoria == Categoria.ISOLAMENTO]

def muscoli_allenati(e):
    return set(e.muscoli_primari) | {PADRE[r] for r in e.regioni}

# l'isolamento più in basso con il primo sopra di lui che non allena lo stesso muscolo
def coppia_superserie(workout):
    liberi = isolamenti_liberi(workout)
    for j in range(len(liberi) - 1, 0, -1):
        basso = liberi[j]
        for alto in reversed(liberi[:j]):
            if not muscoli_allenati(workout[alto]) & muscoli_allenati(workout[basso]):
                return alto, basso
    return None

def unisci_isolamenti(workout):
    alto, basso = coppia_superserie(workout)
    workout[alto] = SuperSerie(workout[alto], workout.pop(basso))

def forma_superserie(scheda, max_minuti, livello):
    scheda = {g: list(w) for g, w in scheda.items()}
    while (g := giorno_peggiore(scheda, max_minuti, livello,
                                lambda w: coppia_superserie(w) is not None)) is not None:
        unisci_isolamenti(scheda[g])
    return scheda

def slot(e, originale):
    return originale.index(componenti(e)[0])

def indice_tagliabile(workout, istanze):
    return next((i for i in range(len(workout) - 1, -1, -1)
                 if not scoperto(workout[i])
                 and any(istanze[x.nome] >= 3 for x in componenti(workout[i]))), None)

def taglia(workout, i, istanze, originale):
    e = workout.pop(i)
    tagliato = [x for x in componenti(e) if istanze[x.nome] >= 3][-1]
    istanze[tagliato.nome] -= 1
    workout.extend(x for x in componenti(e) if x is not tagliato)
    workout.sort(key=lambda x: slot(x, originale))

def taglia_workout(scheda, originale, max_minuti, livello):
    scheda = {g: list(w) for g, w in scheda.items()}
    istanze = Counter(x.nome for w in scheda.values() for e in w for x in componenti(e))
    tagliabile = lambda w: indice_tagliabile(w, istanze) is not None
    while (g := giorno_peggiore(scheda, max_minuti, livello, tagliabile)) is not None:
        taglia(scheda[g], indice_tagliabile(scheda[g], istanze), istanze, originale[g])
    return scheda

def variante_monolaterale(e, esercizi):
    return next((x for x in esercizi
                 if x.monolaterale
                 and set(x.muscoli_primari) == set(e.muscoli_primari)
                 and set(x.muscoli_secondari) == set(e.muscoli_secondari)
                 and set(x.regioni) == set(e.regioni)
                 and x.categoria == e.categoria
                 and set(x.attrezzi) == set(e.attrezzi)), None)

def scambia_monolaterali(workout, max_minuti, livello, esercizi):
    workout = list(workout)
    for i, e in enumerate(workout):
        if not isinstance(e, Esercizio) or e.monolaterale:
            continue
        variante = variante_monolaterale(e, esercizi)
        if variante is None:
            continue
        workout[i] = variante
        if eccesso(workout, max_minuti, livello) > 0:
            workout[i] = e
    return workout

def serie_base(workout):
    return [0 if scoperto(e) else 1 for e in workout]

def aggiungi_serie(workout, max_minuti, livello):
    serie = serie_base(workout)
    reali = [i for i, e in enumerate(workout) if not scoperto(e)]
    while reali:
        for i in reali:
            if durata(workout, serie, livello) + tempo_serie(workout[i], livello) > max_minuti:
                return list(zip(workout, serie))
            serie[i] += 1
    return list(zip(workout, serie))

# un giorno segue una sola strada: se sfora si riduce (superserie e tagli) e resta a 1 serie,
# altrimenti si riempie il tempo (varianti monolaterali, poi serie)
def calcola_serie(scheda, max_minuti, superserie=False, monolaterali=False, esercizi=esercizi,
                  livello=Livello.PRINCIPIANTE):
    originale = scheda
    sforati = {g for g, w in scheda.items() if eccesso(w, max_minuti, livello) > 0}
    if superserie:
        scheda = forma_superserie(scheda, max_minuti, livello)
    scheda = taglia_workout(scheda, originale, max_minuti, livello)
    risultato = {}
    for g, w in scheda.items():
        if g in sforati:
            minimo = durata(w, [1] * len(w), livello)
            if minimo > max_minuti:
                print(f"Attenzione: il giorno {g} dura almeno {minimo} min, "
                      f"non è possibile rispettare il limite di {max_minuti} min.")
            risultato[g] = list(zip(w, serie_base(w)))
            continue
        if monolaterali:
            w = scambia_monolaterali(w, max_minuti, livello, esercizi)
        risultato[g] = aggiungi_serie(w, max_minuti, livello)
    return risultato









#insieme dei metodi che completano la scheda e producono il file .csv

def ripetizioni(e, livello):
    minimo, massimo = RIPETIZIONI[livello][e.categoria]
    return f"{minimo}|{massimo}"

def recupero_testo(e, livello):
    minimo, massimo = intervallo_recupero(e, livello)
    return f"{minimo}|{massimo} min"

def rir_testo(livello):
    minimo, massimo = RIR[livello]
    return f"{minimo}" if minimo == massimo else f"{minimo}|{massimo}"

def riga_esercizio(e, serie, livello):
    if scoperto(e):
        return [e.nome, "", "", "", ""]
    return [e.nome, serie, ripetizioni(e, livello), recupero_testo(e, livello), rir_testo(livello)]

def tabella_workout(numero, workout, livello):
    return [[f"workout {numero}", "", "", "", ""],
            INTESTAZIONE,
            *(riga_esercizio(e, s, livello) for e, s in workout)]

def separatore(giorno_precedente, giorno):
    return [[], ["REST DAY"], []] if giorno - giorno_precedente > 1 else [[]]

def righe_scheda(scheda, livello):
    giorni = sorted(scheda)
    righe = []
    for numero, giorno in enumerate(giorni, start=1):
        if numero > 1:
            righe += separatore(giorni[numero - 2], giorno)
        righe += tabella_workout(numero, scheda[giorno], livello)
    return righe

def scrivi_csv(scheda, livello, percorso="scheda.csv"):
    with open(percorso, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(righe_scheda(scheda, livello))
    return percorso

