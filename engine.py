
import csv
from collections import Counter
from itertools import combinations
from exercise_model import Esercizio, Categoria, Muscolo, Attrezzo, MuscoloScoperto
from execises import esercizi

MIN_REST = 2
TOP_SLOT = 4

RISCALDAMENTO_GENERALE = 10
RECUPERO = {Categoria.COMPOUND_GAMBE: (3, 5)}  # (min, max) in minuti
RECUPERO_DEFAULT = (2, 4)

RIPETIZIONI = {Categoria.COMPOUND_GAMBE: (8, 10)}  # (min, max)
RIPETIZIONI_DEFAULT = (6, 8)

INTESTAZIONE = ["esercizio", "serie", "ripetizioni", "recupero"]


#insieme di metodi che generano la seettimana con i muscoli ordianti
def valid_combos(days, n):
    return [c for c in combinations(sorted(days), n)
            if all(b - a >= MIN_REST for a, b in zip(c, c[1:]))
            and (n == 1 or 7 - c[-1] + c[0] >= MIN_REST)]

def best_combo(days, n, week):
    return min(valid_combos(days, n),
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
        c3, c2 = best_combo(days, 3, week), best_combo(days, 2, week)
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

def esercizio_per(muscolo, esercizi, attrezzi=None):
    return next((e for e in esercizi
                 if muscolo in e.muscoli_primari and eseguibile(e, attrezzi)), None)

def isolamento_per(muscolo, esercizi, attrezzi=None):
    return next((e for e in esercizi
                 if e.muscoli_primari == [muscolo] and eseguibile(e, attrezzi)), None)

def compound_glutei_adduttori(secondario, esercizi, attrezzi=None):
    return next((e for e in esercizi
                 if set(e.muscoli_primari) == {Muscolo.GLUTES, Muscolo.ADDUCTORS}
                 and secondario in e.muscoli_secondari
                 and eseguibile(e, attrezzi)), None)

def scegli_secondario(giorno, week, priorita):
    oggi = week[giorno]
    domani = week.get(giorno % 7 + 1, [])
    presenti = [m for m in (Muscolo.QUADS, Muscolo.HAMSTRINGS) if m in oggi]
    if presenti:
        return max(presenti, key=oggi.index)
    ordinati = sorted((Muscolo.QUADS, Muscolo.HAMSTRINGS),
                      key=lambda m: priorita.index(m) if m in priorita else len(priorita))
    liberi = [m for m in ordinati if m not in domani]
    return liberi[0] if liberi else None

def oppure_scoperto(e, muscolo):
    return MuscoloScoperto(muscolo) if e is None else e

def assegna_esercizi(week, priorita, esercizi, attrezzi=None):
    gambe_speciali = (Muscolo.GLUTES, Muscolo.ADDUCTORS)
    base = {m: esercizio_per(m, esercizi, attrezzi)
            for m in priorita if m not in gambe_speciali}
    risultato = {}
    for giorno, muscoli in week.items():
        compound, slot = None, None
        if all(m in muscoli for m in gambe_speciali):
            i_g, i_a = muscoli.index(Muscolo.GLUTES), muscoli.index(Muscolo.ADDUCTORS)
            if min(i_g, i_a) >= TOP_SLOT:
                secondario = scegli_secondario(giorno, week, priorita)
                if secondario:
                    compound = compound_glutei_adduttori(secondario, esercizi, attrezzi)
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

def recupero(e):
    minimo, massimo = RECUPERO.get(e.categoria, RECUPERO_DEFAULT)
    return (minimo + massimo) / 2

def tempo_serie(e):
    return 0 if scoperto(e) else e.tempo_serie + recupero(e)

def durata(workout, serie):
    return RISCALDAMENTO_GENERALE + sum(
        e.tempo_riscaldamento + s * tempo_serie(e) for e, s in zip(workout, serie))

def durata_con_serie(workout):
    return durata([e for e, _ in workout], [s for _, s in workout]) if workout else 0

def eccesso(workout, max_minuti):
    return durata(workout, [1] * len(workout)) - max_minuti

def indice_tagliabile(workout, istanze):
    return next((i for i in range(len(workout) - 1, -1, -1)
                 if not scoperto(workout[i]) and istanze[workout[i].nome] >= 3), None)

def giorno_peggiore(scheda, istanze, max_minuti):
    candidati = [g for g, w in scheda.items()
                 if eccesso(w, max_minuti) > 0 and indice_tagliabile(w, istanze) is not None]
    return max(candidati, key=lambda g: eccesso(scheda[g], max_minuti), default=None)

def taglia_workout(scheda, max_minuti):
    scheda = {g: list(w) for g, w in scheda.items()}
    istanze = Counter(e.nome for w in scheda.values() for e in w)
    while (g := giorno_peggiore(scheda, istanze, max_minuti)) is not None:
        i = indice_tagliabile(scheda[g], istanze)
        istanze[scheda[g][i].nome] -= 1
        scheda[g].pop(i)
    return scheda

def aggiungi_serie(workout, max_minuti):
    serie = [0 if scoperto(e) else 1 for e in workout]
    reali = [i for i, e in enumerate(workout) if not scoperto(e)]
    while reali:
        for i in reali:
            if durata(workout, serie) + tempo_serie(workout[i]) > max_minuti:
                return list(zip(workout, serie))
            serie[i] += 1
    return list(zip(workout, serie))

def calcola_serie(scheda, max_minuti):
    scheda = taglia_workout(scheda, max_minuti)
    for g, w in scheda.items():
        minimo = durata(w, [1] * len(w))
        if minimo > max_minuti:
            print(f"Attenzione: il giorno {g} dura almeno {minimo} min, "
                  f"non è possibile rispettare il limite di {max_minuti} min.")
    return {g: aggiungi_serie(w, max_minuti) for g, w in scheda.items()}

#insieme dei metodi che completano la scheda e producono il file .csv

def ripetizioni(e):
    minimo, massimo = RIPETIZIONI.get(e.categoria, RIPETIZIONI_DEFAULT)
    return f"{minimo}|{massimo}"

def recupero_testo(e):
    minimo, massimo = RECUPERO.get(e.categoria, RECUPERO_DEFAULT)
    return f"{minimo}|{massimo} min"

def riga_esercizio(e, serie):
    if scoperto(e):
        return [e.nome, "", "", ""]
    return [e.nome, serie, ripetizioni(e), recupero_testo(e)]

def tabella_workout(numero, workout):
    return [[f"workout {numero}", "", "", ""],
            INTESTAZIONE,
            *(riga_esercizio(e, s) for e, s in workout)]

def separatore(giorno_precedente, giorno):
    return [[], ["REST DAY"], []] if giorno - giorno_precedente > 1 else [[]]

def righe_scheda(scheda):
    giorni = sorted(scheda)
    righe = []
    for numero, giorno in enumerate(giorni, start=1):
        if numero > 1:
            righe += separatore(giorni[numero - 2], giorno)
        righe += tabella_workout(numero, scheda[giorno])
    return righe

def scrivi_csv(scheda, percorso="scheda.csv"):
    with open(percorso, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(righe_scheda(scheda))
    return percorso

