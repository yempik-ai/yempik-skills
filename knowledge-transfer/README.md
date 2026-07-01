# knowledge-transfer

Skill che intervista una persona, una domanda per volta, per estrarne il know-how tacito e scriverlo nei file del **company brain** dell'azienda: decisioni, processi, regole con fonte, glossario, domande aperte.

Non è un questionario fisso: è un flusso a fasi **objective-first**.
```
Obiettivo (perche') → Mappa processi (cosa fai, passo passo) → Laddering (eccezioni, criteri, errori) → Verifica (rispecchia e correggi)
```
Il valore vero e' nel laddering: eccezioni e criteri di decisione sono il tacito che nessun manuale scrive.

## Come si usa
1. Carica la skill nel tuo agente (Claude Code: copia la cartella in `.claude/skills/`; Cowork: importala come skill).
2. Segui le 4 fasi; una domanda per volta.
3. La skill scrive/aggiorna `company-brain/decisions/`, `processes/`, `rules.jsonl`, `glossary.md`, `open-questions.md`, `sources.md`.
4. Opzionale: genera 5-10 casi di test dalle regole estratte e verifica che un agente le applichi citando la fonte (soglia consigliata >=90%).

## Dominio pilota incluso
**Customer care / supporto** (banca domande completa in `SKILL.md`). Per un altro dominio (commerciale, amministrazione): duplicare il blocco "Banca domande" e riscrivere solo il laddering; lo scheletro a fasi resta identico.

Nessuno script/hook richiesto: e' una skill puramente conversazionale.
