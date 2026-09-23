const NOMI_GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"];

const NOMI_MUSCOLI = {
  "chest": "Petto",
  "lats": "Dorsali",
  "upper back": "Parte alta della schiena",
  "side delts": "Deltoidi laterali",
  "triceps": "Tricipiti",
  "biceps": "Bicipiti",
  "quads": "Quadricipiti",
  "hamstrings": "Femorali",
  "glutes": "Glutei",
  "adductors": "Adduttori",
};

// ordine iniziale proposto, uguale a main.py
const PRIORITA_INIZIALE = ["chest", "lats", "upper back", "quads", "hamstrings",
                           "side delts", "triceps", "biceps", "glutes", "adductors"];
const GIORNI_INIZIALI = [1, 2, 4, 5, 6];

const $ = (id) => document.getElementById(id);

const stato = {
  giorni: new Set(GIORNI_INIZIALI),
  muscoli: [],               // [{ valore, attivo }] nell'ordine di priorità
  attrezzi: new Set(),
  ultimaRichiesta: null,
};

const nomeMuscolo = (m) => NOMI_MUSCOLI[m] ?? m;
const maiuscola = (s) => s.charAt(0).toUpperCase() + s.slice(1);


//chiamate all'api

async function chiama(percorso, opzioni = {}) {
  const risposta = await fetch(percorso, opzioni);
  if (!risposta.ok) {
    let messaggio = `Errore ${risposta.status}`;
    try {
      const corpo = await risposta.json();
      if (Array.isArray(corpo.detail)) {
        messaggio = corpo.detail.map((d) => d.msg.replace(/^Value error, /, "")).join(" · ");
      } else if (corpo.detail) {
        messaggio = corpo.detail;
      }
    } catch { /* risposta non json */ }
    throw new Error(messaggio);
  }
  return risposta;
}

const inviaRichiesta = (percorso, richiesta) => chiama(percorso, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(richiesta),
});


//costruzione del form

function chip(testo, attivo, onClick) {
  const b = document.createElement("button");
  b.type = "button";
  b.className = "chip";
  b.textContent = testo;
  b.setAttribute("aria-pressed", String(attivo));
  b.addEventListener("click", () => {
    const nuovo = b.getAttribute("aria-pressed") !== "true";
    b.setAttribute("aria-pressed", String(nuovo));
    onClick(nuovo);
  });
  return b;
}

function disegnaGiorni() {
  $("giorni").replaceChildren(...NOMI_GIORNI.map((nome, i) => {
    const giorno = i + 1;
    return chip(nome.slice(0, 3), stato.giorni.has(giorno), (attivo) => {
      attivo ? stato.giorni.add(giorno) : stato.giorni.delete(giorno);
    });
  }));
}

function sposta(i, delta) {
  const j = i + delta;
  [stato.muscoli[i], stato.muscoli[j]] = [stato.muscoli[j], stato.muscoli[i]];
  disegnaMuscoli();
}

function pulsanteSposta(simbolo, etichetta, disabilitato, onClick) {
  const b = document.createElement("button");
  b.type = "button";
  b.className = "sposta";
  b.textContent = simbolo;
  b.title = etichetta;
  b.setAttribute("aria-label", etichetta);
  b.disabled = disabilitato;
  b.addEventListener("click", onClick);
  return b;
}

function disegnaMuscoli() {
  let rango = 0;
  $("muscoli").replaceChildren(...stato.muscoli.map((m, i) => {
    const li = document.createElement("li");
    li.classList.toggle("escluso", !m.attivo);

    const numero = document.createElement("span");
    numero.className = "rango";
    numero.textContent = m.attivo ? `${++rango}.` : "–";

    const spunta = document.createElement("input");
    spunta.type = "checkbox";
    spunta.checked = m.attivo;
    spunta.setAttribute("aria-label", `Allena ${nomeMuscolo(m.valore)}`);
    spunta.addEventListener("change", () => { m.attivo = spunta.checked; disegnaMuscoli(); });

    const nome = document.createElement("span");
    nome.className = "nome-muscolo";
    nome.textContent = nomeMuscolo(m.valore);

    li.append(numero, spunta, nome,
      pulsanteSposta("↑", "Sposta su", i === 0, () => sposta(i, -1)),
      pulsanteSposta("↓", "Sposta giù", i === stato.muscoli.length - 1, () => sposta(i, 1)));
    return li;
  }));
}

function disegnaAttrezzi(attrezzi) {
  $("attrezzi").replaceChildren(...attrezzi.map((a) => chip(maiuscola(a), false, (attivo) => {
    attivo ? stato.attrezzi.add(a) : stato.attrezzi.delete(a);
  })));
}

async function caricaCatalogo() {
  const [muscoli, attrezzi] = await Promise.all([
    chiama("/muscoli").then((r) => r.json()),
    chiama("/attrezzi").then((r) => r.json()),
  ]);
  const ordinati = [...PRIORITA_INIZIALE.filter((m) => muscoli.includes(m)),
                    ...muscoli.filter((m) => !PRIORITA_INIZIALE.includes(m))];
  stato.muscoli = ordinati.map((valore) => ({ valore, attivo: true }));
  disegnaMuscoli();
  disegnaAttrezzi(attrezzi);
}


//lettura del form

function leggiRichiesta() {
  return {
    giorni: [...stato.giorni].sort((a, b) => a - b),
    priorita_muscoli: stato.muscoli.filter((m) => m.attivo).map((m) => m.valore),
    max_minuti: Number($("max-minuti").value),
    attrezzi_disponibili: $("tutti-attrezzi").checked ? null : [...stato.attrezzi],
  };
}

function controllaRichiesta(r) {
  if (r.giorni.length === 0) return "Seleziona almeno un giorno di allenamento.";
  if (r.priorita_muscoli.length === 0) return "Seleziona almeno un muscolo da allenare.";
  if (!Number.isInteger(r.max_minuti) || r.max_minuti <= 0) return "Inserisci una durata valida in minuti.";
  return null;
}


//visualizzazione della scheda

function intervallo(i, suffisso = "") {
  return i ? `${i.min}–${i.max}${suffisso}` : "";
}

function cella(testo, classe) {
  const td = document.createElement("td");
  td.textContent = testo;
  if (classe) td.className = classe;
  return td;
}

function tabellaEsercizi(esercizi) {
  const table = document.createElement("table");
  table.innerHTML = "<thead><tr><th>Esercizio</th><th>Serie</th><th>Rip.</th><th>Recupero</th></tr></thead>";
  const tbody = document.createElement("tbody");
  for (const e of esercizi) {
    const tr = document.createElement("tr");
    if (e.scoperto) {
      tr.className = "scoperto";
      const td = cella(maiuscola(e.nome));
      td.colSpan = 4;
      tr.append(td);
    } else {
      tr.append(cella(e.nome),
                cella(String(e.serie), "num"),
                cella(intervallo(e.ripetizioni), "num"),
                cella(intervallo(e.recupero_minuti, " min"), "num"));
    }
    tbody.append(tr);
  }
  table.append(tbody);
  return table;
}

function cardGiorno(g, numero) {
  const card = document.createElement("article");
  card.className = "card giorno";

  const titolo = document.createElement("h3");
  titolo.textContent = `Workout ${numero} · ${NOMI_GIORNI[g.giorno - 1]}`;

  const meta = document.createElement("p");
  meta.className = g.supera_limite ? "meta oltre" : "meta";
  meta.textContent = `Durata stimata: ${Math.round(g.durata_minuti)} min`;

  card.append(titolo, meta, tabellaEsercizi(g.esercizi));
  return card;
}

function mostraScheda(scheda) {
  $("avvisi").replaceChildren(...scheda.avvisi.map((testo) => {
    const div = document.createElement("div");
    div.className = "avviso attenzione";
    div.textContent = testo;
    return div;
  }));
  $("settimana").replaceChildren(...scheda.giorni.map((g, i) => cardGiorno(g, i + 1)));
  $("risultato").hidden = false;
  $("risultato").scrollIntoView({ behavior: "smooth", block: "start" });
}

function mostraErrore(messaggio) {
  $("errore").textContent = messaggio;
  $("errore").hidden = !messaggio;
}


//azioni

async function genera(evento) {
  evento.preventDefault();
  const richiesta = leggiRichiesta();
  const problema = controllaRichiesta(richiesta);
  mostraErrore(problema);
  if (problema) return;

  const pulsante = $("genera");
  pulsante.disabled = true;
  pulsante.textContent = "Sto generando la scheda…";
  try {
    const scheda = await inviaRichiesta("/scheda", richiesta).then((r) => r.json());
    stato.ultimaRichiesta = richiesta;
    mostraScheda(scheda);
  } catch (e) {
    mostraErrore(e.message);
  } finally {
    pulsante.disabled = false;
    pulsante.textContent = "Genera scheda";
  }
}

async function scaricaCsv() {
  if (!stato.ultimaRichiesta) return;
  try {
    const blob = await inviaRichiesta("/scheda/csv", stato.ultimaRichiesta).then((r) => r.blob());
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "scheda.csv";
    link.click();
    URL.revokeObjectURL(url);
  } catch (e) {
    mostraErrore(e.message);
  }
}


//avvio

disegnaGiorni();
$("tutti-attrezzi").addEventListener("change", (e) => { $("attrezzi").hidden = e.target.checked; });
$("form").addEventListener("submit", genera);
$("scarica-csv").addEventListener("click", scaricaCsv);
caricaCatalogo().catch((e) => mostraErrore(`Impossibile caricare i dati: ${e.message}`));
