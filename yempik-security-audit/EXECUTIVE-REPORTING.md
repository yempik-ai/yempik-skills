# Executive Reporting

Instructions for `EXECUTIVE-SUMMARY.md`, the last Phase 6 artifact. `REPORT.md` serves the people who fix; this page serves the person who decides budget, priority, and who to call. That reader has three minutes, no security vocabulary, and the authority to act on Monday.

## Inputs and limits

- Derive every sentence from the final `findings.json`, the coverage ledger, and `REPORT.md`. Add no fact, verdict, severity, impact, or number that those files do not carry.
- Write after both validators pass and after `REPORT.md` exists. An incomplete run gets a summary too, and its first sentence says the run is incomplete.
- Never include reproduction steps, payloads, exploit detail, credential values, or internal hostnames. Point to `REPORT.md` for technical detail.
- `needs_validation` records never receive a severity word here either.

## Language

Write in the language of the user's request. When that language is Italian, write the Italian a senior manager uses in a board meeting: direct, concrete, no anglicisms where an Italian word exists (*problema confermato*, not *finding*; *chiave di accesso*, not *token* unless the word matters), each unavoidable technical term explained once in a clause. Do not translate English sentence structure. No fear words, no hedging stacked on hedging, no exclamation marks.

Map severity to plain words: critical → *critico* / critical, high → *grave* / serious, medium → *medio* / moderate, low → *basso* / low, informational → omitted.

## Structure

Use these five headings in the request language, in this order. Keep the whole page under about 450 words.

1. **Verdict** — one or two sentences. Count of confirmed problems, the most serious one in business terms, and whether the run was complete or partial. A clean run says that no problem was confirmed in what was examined and names the main limit. Never write that the software is secure.
2. **What is exposed** — one line per confirmed problem, most severe first, at most five (then a count of the rest): severity word, who could do what to whom, in terms of customers, employees, suppliers, money, or the company's name. Example shape: *Grave · Un cliente può leggere gli ordini di altri clienti modificando un numero nell'indirizzo della pagina.*
3. **Three questions for your team** — exactly three, answerable in a meeting, each tied to a confirmed record or to a blocker in a `needs_validation` record. Ask about ownership, timing, and evidence, not about technology. Example shape: *Chi può leggere la chiave principale del gateway AI, e quando è stata cambiata l'ultima volta?*
4. **What we could not verify** — the `needs_validation` blockers in plain words, each with who can resolve it (cloud provider, IT, software supplier, the developer's own tool settings).
5. **What this run did not cover, and when to run again** — profile, scope, deferred and out-of-scope areas from the ledger in one short paragraph. State that a single pass is not exhaustive and that a new run belongs after any material change to the code, its dependencies, or its AI tools.

## Example (Italian, structure only)

```markdown
# Sintesi per la direzione · <repo> · <data>

## Il verdetto
Due problemi confermati, uno grave. Il controllo è completo sul codice esaminato; non copre l'infrastruttura del fornitore cloud.

## Cosa è esposto
- Grave · Chi riceve un link di condivisione può leggere i documenti di altri clienti.
- Medio · La chiave del servizio AI finisce nel codice che il browser scarica: chiunque visiti il sito può usarla a spese dell'azienda.

## Tre domande per il team
1. Entro quando è corretto l'accesso ai documenti condivisi, e chi lo verifica dopo la correzione?
2. La chiave del servizio AI è già stata sostituita, e chi controlla la spesa degli ultimi trenta giorni?
3. Chi decide quali file di configurazione degli agenti di coding possono entrare nel repository?

## Cosa non abbiamo potuto verificare
- Se il bucket dei documenti è privato: lo conferma chi gestisce l'account cloud.

## Cosa resta fuori, e quando ripetere
Controllo standard su tutto il repository; esclusi l'app mobile e gli script di migrazione. Un solo passaggio non trova tutto: va ripetuto dopo ogni cambiamento importante del codice, delle dipendenze o degli strumenti AI.
```
