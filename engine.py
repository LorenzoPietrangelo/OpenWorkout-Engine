
from itertools import combinations

MIN_REST = 2

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


days_selected=[1,2,5]
muscle_priority=["Chest","Lats","upper back","Quads","Hamstrings",
                "side delts","Triceps","Biceps","glutes","adduttori"]

for day, muscles in build_week(days_selected, muscle_priority).items():
    print(day, muscles)

