import csv
import io

from engine import (build_week, assegna_esercizi, calcola_serie, durata_con_serie,
                    righe_scheda, scoperto, RECUPERO, RECUPERO_DEFAULT,
                    RIPETIZIONI, RIPETIZIONI_DEFAULT)
from execises import esercizi

from api_wrapper.schemas import Giorno, InfoEsercizio, Intervallo, Scheda, VoceEsercizio


#stessa pipeline di main.py

def genera(richiesta):
    week = build_week(richiesta.giorni, richiesta.priorita_muscoli)
    scheda = assegna_esercizi(week, richiesta.priorita_muscoli, esercizi,
                              richiesta.attrezzi_disponibili)
    return week, calcola_serie(scheda, richiesta.max_minuti)


#conversione dei risultati del motore nei modelli dell'api

def intervallo(tabella, default, e):
    minimo, massimo = tabella.get(e.categoria, default)
    return Intervallo(min=minimo, max=massimo)

def voce(e, serie):
    if scoperto(e):
        return VoceEsercizio(nome=e.nome, serie=0, ripetizioni=None,
                             recupero_minuti=None, scoperto=True)
    return VoceEsercizio(nome=e.nome, serie=serie,
                         ripetizioni=intervallo(RIPETIZIONI, RIPETIZIONI_DEFAULT, e),
                         recupero_minuti=intervallo(RECUPERO, RECUPERO_DEFAULT, e),
                         scoperto=False)

def info_esercizio(e):
    return InfoEsercizio(nome=e.nome, muscoli_primari=e.muscoli_primari,
                         muscoli_secondari=e.muscoli_secondari, categoria=e.categoria,
                         attrezzi=e.attrezzi, monolaterale=e.monolaterale)

def catalogo_esercizi():
    return [info_esercizio(e) for e in esercizi]

def scheda_json(richiesta):
    week, scheda_con_serie = genera(richiesta)
    giorni, avvisi = [], []
    for g, workout in scheda_con_serie.items():
        durata = durata_con_serie(workout)
        supera = durata > richiesta.max_minuti
        if supera:
            avvisi.append(f"Il giorno {g} dura almeno {durata:.0f} min, non è possibile "
                          f"rispettare il limite di {richiesta.max_minuti} min.")
        giorni.append(Giorno(giorno=g, muscoli=week[g], durata_minuti=round(durata, 1),
                             supera_limite=supera,
                             esercizi=[voce(e, s) for e, s in workout]))
    return Scheda(giorni=giorni, avvisi=avvisi)

def scheda_csv(richiesta):
    _, scheda_con_serie = genera(richiesta)
    buffer = io.StringIO()
    csv.writer(buffer).writerows(righe_scheda(scheda_con_serie))
    buffer.seek(0)
    return buffer
