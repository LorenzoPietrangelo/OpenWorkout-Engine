
from itertools import combinations
from exercise_model import Esercizio, Categoria, Muscolo
from execises import esercizi

MIN_REST = 2
TOP_SLOT = 4


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

def build_week(days, muscles):
    week = {g: [] for g in days}
    for m in muscles:
        c3, c2 = best_combo(days, 3, week), best_combo(days, 2, week)
        combo = c3 or c2
        if c3 and c2 and all(a < b for a, b in zip(depths(c2, week), depths(c3, week))):
            combo = c2
        for g in combo or []:
            week[g].append(m)
    return week


#insieme di metodi che costruisocno la scheda sostitunedo i muscoli con esercizi
def esercizio_per(muscolo, esercizi):
    return next((e for e in esercizi if muscolo in e.muscoli_primari), None)

def isolamento_per(muscolo, esercizi):
    return next((e for e in esercizi if e.muscoli_primari == [muscolo]), None)

def compound_glutei_adduttori(secondario, esercizi):
    return next((e for e in esercizi
                 if set(e.muscoli_primari) == {Muscolo.GLUTES, Muscolo.ADDUCTORS}
                 and secondario in e.muscoli_secondari), None)

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

def assegna_esercizi(week, priorita, esercizi):
    gambe_speciali = (Muscolo.GLUTES, Muscolo.ADDUCTORS)
    base = {m: esercizio_per(m, esercizi) for m in priorita if m not in gambe_speciali}
    risultato = {}
    for giorno, muscoli in week.items():
        compound, slot = None, None
        if all(m in muscoli for m in gambe_speciali):
            i_g, i_a = muscoli.index(Muscolo.GLUTES), muscoli.index(Muscolo.ADDUCTORS)
            if min(i_g, i_a) >= TOP_SLOT:
                secondario = scegli_secondario(giorno, week, priorita)
                if secondario:
                    compound = compound_glutei_adduttori(secondario, esercizi)
                    slot = max(i_g, i_a)
        workout = []
        for i, m in enumerate(muscoli):
            if m in gambe_speciali:
                if compound is None:
                    workout.append(isolamento_per(m, esercizi))
                elif i == slot:
                    workout.append(compound)
            else:
                workout.append(base[m])
        risultato[giorno] = workout
    return risultato


