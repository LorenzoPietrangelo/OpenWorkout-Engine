# OpenWorkout Engine

> This project is founded on a simple belief: **everyone has the right to train properly.**

OpenWorkout Engine generates a personalized weekly workout program from a few inputs: the days you can train, how long each session can last, the equipment you have and the muscles you care about most. It is deterministic and rule-based: no AI, no black box. Every choice the engine makes follows the rules described below.

It can be used as a Python script, as a REST API or through a small web interface.

**[Try it online](https://open-workout-engine.vercel.app)** · **[API documentation](https://open-workout-engine.vercel.app/docs)**

---

## Table of contents

- [Quick start](#quick-start)
- [Inputs](#inputs)
- [Output](#output)
- [Rules](#rules)
- [How the algorithm works](#how-the-algorithm-works)
- [API](#api)
- [Project structure](#project-structure)
- [Adding exercises](#adding-exercises)
- [Known limitations](#known-limitations)
- [Roadmap](#roadmap)
- [License](#license)

---

## Quick start

Requires **Python 3.14+**.

```bash
git clone https://github.com/LorenzoPietrangelo/OpenWorkout-Engine.git
cd OpenWorkout-Engine
pip install -r requirements.txt
```

**Command line.** Edit the inputs at the top of `main.py`, then run:

```bash
python main.py
```

The weekly split, the chosen exercises and the final sets are printed to the terminal, and the program is saved to `scheda.csv`.

**API and web interface.**

```bash
uvicorn api_wrapper.app:app --reload
```

- Web interface: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs

---

## Inputs

| Input | Description |
|---|---|
| **Training days** | Days of the week you train, as numbers from `1` (Monday) to `7` (Sunday) |
| **Muscle priority** | The muscles you want to train, ordered from most to least important |
| **Max duration** | Maximum length of each session, in minutes |
| **Available equipment** | The equipment you have. Leave it empty (`None` / `null`) to assume a fully equipped gym |
| **Supersets** | Whether you are willing to do [supersets](#supersets) when time is short. Off by default |

Supported muscles: `chest`, `lats`, `upper back`, `side delts`, `triceps`, `biceps`, `quads`, `hamstrings`, `glutes`, `adductors`.

Supported equipment: dumbbells, barbell, bench, cables, pec fly machine, leg extension, leg curl, leg press, adductor machine, smith machine, lat machine, T-bar. The exact identifiers are listed by `GET /attrezzi`.

---

## Output

For each training day, the program lists the exercises in order. Each exercise has:

- **Sets**, calculated to fill the available time
- **Rep range**: 8–10 for leg compound movements, 6–8 for everything else
- **Rest**: 3–5 min for leg compound movements, 2–4 min for everything else. A superset has a single rest (see [Supersets](#supersets))

A rest day between two sessions is marked in the CSV export.

If no exercise can be performed with the available equipment, the muscle still appears in the program as a placeholder ("no equipment available for …"), so you know what is missing.

---

## Rules

The engine follows these rules:

- **48-hour recovery.** A muscle is never trained on two consecutive days. This also applies across the week boundary (Sunday → Monday).
- **Frequency.** Every muscle is trained **2 or 3 times per week**. The engine tries for 3 whenever possible.
- **One exercise per muscle.** Each muscle gets one exercise, which is repeated on every day that muscle is trained. Glutes and adductors are the only exception (see below).
- **One set as a baseline.** Every exercise starts with one set. More sets are added only if the time allows it.

### Glutes and adductors

Glutes and adductors can be trained with isolation exercises (hip thrust, adductor machine…) or together with a single compound leg movement (squat, leg press, stiff-leg deadlift…). The engine decides day by day:

1. If glutes and adductors are **not trained on the same day**, each gets its own isolation exercise.
2. If they are on the same day and **at least one of them is in the top 4 slots** of that workout, they are still high-priority, so each gets its own isolation exercise.
3. If they are on the same day and **both are below the top 4 slots**, a single compound movement replaces both. It takes the lower of their two slots. The compound is chosen based on its secondary muscle:
   - if **quads or hamstrings** are also trained that day, the compound uses that muscle as a secondary. If both are trained that day, it uses the one in the lower slot. For example, if hamstrings are already in the workout, a stiff-leg deadlift is chosen.
   - if **neither** is trained that day, the engine picks the one with higher overall priority, as long as it is not trained the next day (to respect recovery).
   - if both quads and hamstrings are trained the next day, the compound is skipped and glutes and adductors fall back to isolation exercises.

### Supersets

A superset is two isolation exercises performed back to back, with a single rest at the end. Supersets are optional: they are used only if you enable them and only when a session does not fit the time limit even with one set per exercise.

- **Which exercises.** Only isolation exercises can be paired, and each exercise can be in at most one superset. The engine pairs the **two lowest isolation exercises** in the workout, even if other exercises sit between them.
- **Position.** The superset takes the **higher slot** of the two. The first exercise of the superset is the one that was higher in the workout.
- **Timing.** Warm-up and set duration do not change: they are the sum of the two exercises. Rest changes: there is **one rest per round**, equal to the longer rest of the two exercises **plus 30 seconds** to move from one exercise to the other. With the default values, a round costs 5.5 min instead of 8 min for the two exercises done separately.
- **Sets.** Both exercises in a superset always get the same number of sets.

---

## How the algorithm works

The program is built in three phases.

### 1. Building the weekly split

Muscles are processed one at a time, in priority order. For each muscle, the engine looks at every valid way to place it on **3 days** and on **2 days** (valid = no two sessions less than 48 hours apart). Among these, it picks the combination whose workouts are currently the emptiest, so the muscle gets the **highest available slot**.

3 days are preferred. A 2-day placement wins only if it puts the muscle in a higher slot on every day it compares to the 3-day option (better in at least one, never worse).

Muscles already placed are never moved, so higher-priority muscles always keep the best positions.

### 2. Assigning exercises

Each muscle is replaced with an exercise from the catalogue that targets it as a primary muscle and can be performed with the available equipment. Glutes and adductors follow the [dedicated rules](#glutes-and-adductors).

### 3. Fitting the time limit

The duration of a session is estimated as:

```
10 min general warm-up
+ for each exercise:  exercise warm-up  +  sets × (set duration + average rest)
```

**If a session is too long** (it exceeds the limit even with one set per exercise), the engine reduces it in two steps. Both steps work the same way: they always act on the day that exceeds the limit the most, make one change, recalculate and repeat.

1. **Supersets** (only if enabled). On the worst day that still has two free isolation exercises, the two lowest are merged into a [superset](#supersets). This repeats until every day fits, or until no day has two free isolation exercises left. It does not remove any exercise, so weekly volume is kept.
2. **Removing exercises.** On the worst day, the engine removes the lowest exercise that is trained 3 times a week (bringing it down to 2). This repeats until every day fits, or until no exercise trained 3 times a week is left.
   - If the lowest removable item is a superset, only one of its two exercises is removed: the one trained 3 times a week, or the lower one if both are. The other exercise becomes a normal exercise again and goes back to its **original slot**.

If a day still does not fit, a warning is returned.

**If a session is too short,** sets are added one at a time from the top exercise to the bottom, cycling through the list, until the next set would exceed the time limit. Higher-priority muscles therefore get extra volume first.

---

## API

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/scheda` | Generate a program (JSON) |
| `POST` | `/scheda/csv` | Generate a program (CSV download) |
| `GET` | `/muscoli` | List supported muscles |
| `GET` | `/attrezzi` | List supported equipment |
| `GET` | `/esercizi` | List the exercise catalogue |

Full interactive documentation, where you can try every endpoint from the browser, is available at **[`/docs`](https://open-workout-engine.vercel.app/docs)** (Swagger UI) and **[`/redoc`](https://open-workout-engine.vercel.app/redoc)** on the hosted version, or at http://localhost:8000/docs when running locally.

Example request:

```json
POST /scheda
{
  "giorni": [1, 2, 4, 5, 6],
  "priorita_muscoli": ["chest", "lats", "upper back", "quads", "hamstrings",
                       "side delts", "triceps", "biceps", "glutes", "adductors"],
  "max_minuti": 60,
  "attrezzi_disponibili": null,
  "superserie": false
}
```

| Field | Meaning |
|---|---|
| `giorni` | Training days (1 = Monday … 7 = Sunday) |
| `priorita_muscoli` | Muscles in priority order |
| `max_minuti` | Max session length in minutes |
| `attrezzi_disponibili` | Available equipment, `null` = everything |
| `superserie` | `true` to allow [supersets](#supersets) when time is short. Optional, default `false` |

The response contains, for each day, the muscles trained, the exercises with sets, reps and rest, the estimated duration and whether it exceeds the limit. It also includes a list of warnings. A superset appears as a single exercise named after both exercises (e.g. `"Leg curl + Cable push down"`), with its single rest, which can be a decimal number (e.g. `2.5`–`4.5` min).

---

## Project structure

```
open-workout-engine/
├── engine.py                 # Core algorithm: weekly split, exercise assignment, sets, CSV export
├── exercise_model.py         # Data model: muscles, equipment, categories, Esercizio and SuperSerie
├── execises.py               # Exercise catalogue: add new exercises here
├── main.py                   # CLI example: edit the inputs and run to generate scheda.csv
│
├── api_wrapper/              # REST API (FastAPI)
│   ├── app.py                # App entry point, mounts routers and frontend
│   ├── schemas.py            # Request/response models and input validation
│   ├── service.py            # Bridge between the API and the engine
│   └── routers/
│       ├── scheda.py         # POST /scheda, POST /scheda/csv: generate a program
│       └── catalogo.py       # GET /muscoli, /attrezzi, /esercizi: browse the catalogue
│
├── frontend/                 # Static web UI served by the API
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Project metadata and Vercel config
└── LICENSE                   # MIT
```

> Note: identifiers, API fields and the web interface are currently in Italian.

---

## Adding exercises

Exercises live in `execises.py`. To add one, append an `Esercizio` to the list:

```python
Esercizio(
    "Barbell squat",                              # name
    [Muscolo.GLUTES, Muscolo.ADDUCTORS],          # primary muscles
    Categoria.COMPOUND_GAMBE,                     # category: ISOLAMENTO, COMPOUND_UPPER, COMPOUND_GAMBE
    muscoli_secondari=[Muscolo.QUADS],            # secondary muscles
    tempo_riscaldamento=5,                        # warm-up time (min)
    tempo_serie=1,                                # duration of one set (min)
    attrezzi=[Attrezzo.BILANCIERE],               # required equipment (empty = bodyweight)
),
```

When several exercises fit the same muscle and equipment, the engine picks the **first one in the list**, so order matters.

---

## Known limitations

- **At least two non-consecutive training days are required.** Since every muscle must be trained 2–3 times a week with 48 hours of rest, a single training day, or only consecutive days (e.g. Monday + Tuesday), produces an empty program. In a 3-day consecutive block (e.g. Mon–Tue–Wed), the middle day stays empty.
- Exercise selection is not randomized. The same inputs always produce the same program.

---

## Roadmap

- **Experience level (beginner / advanced).** Advanced lifters will be able to target different regions of the same muscle (e.g. upper and lower chest). Regions will be treated as one muscle for placement, so they are always trained in the same session.
- **Full Body A/B split.** Two alternating workouts in a rolling cycle, e.g. with 3 sessions per week: week 1 `A → B → A`, week 2 `B → A → B`.
- Separate *priority* and *non-priority* muscle lists.
- Clear feedback when the selected days cannot produce a valid program.
- A larger exercise catalogue.

---

## License

Released under the [MIT License](LICENSE).
