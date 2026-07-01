---
name: knowledge-transfer
description: >-
  Conduce un'intervista strutturata a una persona per estrarne il know-how
  operativo (conoscenza tacita) e trasformarlo nei file del company brain:
  decisioni, processi, regole con fonte, glossario, domande aperte. Usala quando
  un'azienda deve trasferire la conoscenza di una persona (onboarding, rischio-uscita,
  standardizzazione di un processo) in un contesto operativo che il team e gli agenti
  AI possono leggere e applicare. Termine di categoria: "company brain".
---

# Knowledge Transfer · l'intervista che costruisce il company brain

> Skill del kit **cowork-os** (per Claude Cowork). v1: intervista in testo/chat, nessun front-end vocale richiesto.

## Cosa fa (e cosa NON fa)

**Fa:** intervista una persona una domanda per volta, scava la conoscenza tacita (eccezioni, criteri di decisione, errori tipici, regole non scritte) e la scrive come **file del company brain** che restano dell'azienda: decisioni, processi, regole con fonte, glossario, domande aperte.

**Non fa:** non e' una chiacchierata trascritta, non e' un questionario fisso, non inventa. Ogni regola estratta ha una **fonte** (intervista, data, chi l'ha detto) e un livello di **confidence**. Se non sa, lo dichiara.

## Principio guida: objective-first, una domanda per volta

Non partire dai task. Parti dal perche': cosa deve saper **fare** un nuovo assunto (o un agente) da solo alla fine? Quell'obiettivo fissa il perimetro. Poi guidi la persona sui suoi processi reali, generando follow-up dinamici dalle risposte, non da lista fissa. Chiudi sempre rispecchiando e facendo correggere.

## Il conduttore: 4 fasi

**Fase 0 · Setup (30 secondi).** Chiedi: chi sei, che ruolo, quale processo/area copriamo oggi, quanto tempo abbiamo. Crea la cartella `company-brain/` se non esiste.

**Fase 1 · Obiettivo.** Una domanda alla volta:
- Qual e' il risultato che questa conoscenza deve produrre?
- Cosa deve saper fare, da solo, un nuovo assunto entro 2 settimane?
- Quali sono i 3 casi che gestisci piu' spesso, e i 3 che fanno piu' danni se gestiti male?
Da qui esce il **perimetro di distillazione**.

**Fase 2 · Mappa dei processi.** Prendi il caso piu' frequente e guida:
- Come arriva la richiesta? (canale) Cosa fai per primo? Passo passo fino alla chiusura.
- Quali sistemi apri, in che ordine? Dove ti fermi ad aspettare qualcuno?
Ripeti per i 2-3 processi chiave. Una cosa per volta.

**Fase 3 · Approfondimento (laddering) — qui si estrae il valore.** Su ogni processo scava:
- Quando NON fai cosi'? (le eccezioni sono il tacito)
- Come scegli tra A e B? Qual e' il criterio esatto?
- Qual e' un errore che i nuovi fanno e che sembra piccolo ma costa caro?
- Qual e' una regola non scritta che nessun manuale dice?
- Cosa fai quando non sai la risposta? Cosa non devi mai promettere?

**Fase 4 · Verifica.** Rispecchia 5-8 regole chiave e fai correggere:
- "Quindi la regola e': fai X, tranne quando Y. Giusto?"
Correggi finche' la persona conferma. Riduce l'interpretazione.

## Regole di conduzione (come intervistare bene)

- **Una domanda per volta.** Mai raffiche.
- **Follow-up dinamici** dalla risposta, non dal copione.
- **Parla la lingua della persona**, niente gergo tecnico o AI.
- **Insisti sulle eccezioni e sui criteri di decisione**: li' vive il know-how che non e' scritto da nessuna parte.
- **Non riempire i silenzi con la tua interpretazione**: chiedi.
- **Chiudi ogni blocco rispecchiando** e facendo correggere.

## Output: cosa scrive nel company brain

```
company-brain/
  decisions/decisions.md        # decisioni e regole con stato e perche'
  processes/<processo>.md       # il flusso passo-passo per ogni processo
  rules.jsonl                   # regole strutturate (schema sotto), per gli agenti
  glossary.md                   # termini interni, nomi di sistemi, sigle
  open-questions.md             # buchi emersi, da chiarire con altre persone
  sources.md                    # ogni regola -> intervista, data, chi l'ha detta
```

Schema di ogni regola:

```json
{
  "id": "CC-014",
  "type": "decision_rule",
  "domain": "customer-care",
  "trigger": "Il cliente chiede un reso fuori dai termini standard",
  "action": "Verifica prima la data d'acquisto e la categoria prodotto; se entro 40 giorni e non personalizzato, autorizza; altrimenti proponi buono, non rimborso.",
  "exceptions": ["Cliente top / contratto annuale: autorizza comunque, poi segnala"],
  "anti_patterns": ["Promettere il rimborso prima di aver verificato la categoria"],
  "source": {"type": "interview", "person": "Nome ruolo", "date": "2026-07-01", "quote": "<frase testuale>"},
  "confidence": "high",
  "conflicts_with": []
}
```

`confidence`: `high` (detto esplicitamente) · `medium` (sintesi di piu' risposte) · `needs_review` (inferito, da validare). Solo `high`/`medium` vanno in produzione.

## Validazione (opzionale ma consigliata)

A fine intervista, genera 5-10 **casi di test** dal know-how estratto ("dato questo scenario, cosa fa la regola?") e verifica che un agente li applichi citando la regola giusta. E' l'unico modo per sapere se il company brain "ha appreso" o sta improvvisando. Soglia consigliata per uso in produzione: applica la regola giusta e rispetta le eccezioni nel >=90% dei casi.

---

## Banca domande · dominio pilota: CUSTOMER CARE / SUPPORTO

**Obiettivo:**
- Cosa deve saper gestire da solo un nuovo agente di supporto entro 2 settimane?
- Quali 3 tipi di richiesta valgono l'80% del volume?
- Quali 3 situazioni, se gestite male, ci fanno perdere il cliente?

**Mappa processi:**
- Prendiamo la richiesta piu' comune: da quale canale arriva? Qual e' la prima cosa che guardi? Poi? Fino a quando la consideri chiusa?
- Quali sistemi apri e in che ordine? Dove sei costretto a chiedere a qualcun altro?

**Laddering (specifico customer care):**
- Quando NON segui lo script standard?
- Come capisci se un cliente va prima calmato e poi risolto?
- Qual e' la soglia esatta per escalare a un senior o a un umano?
- Qual e' la differenza tra una risposta corretta e una che il cliente accetta davvero?
- Cosa fai quando non sai la risposta? Cosa non devi mai promettere?
- Un errore dei nuovi che sembra piccolo ma costa caro?
- Regole non scritte sul tono: cosa non dire mai a un cliente?
- Casi limite: reso fuori policy, cliente arrabbiato con ragione, richiesta ambigua, doppio ordine. Come li gestisci?

**Verifica:** rispecchia 5-8 regole ("escali quando X, tranne se Y, giusto?") e fai correggere.

> Per aggiungere un dominio (es. commerciale, amministrazione): duplica questo blocco e riscrivi solo le domande di laddering. Lo scheletro a fasi resta identico.
