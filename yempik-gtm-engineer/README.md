# Yempik GTM Engineer

Agent Skill for founder-led outbound: build an account universe, score it, get the list
approved, write evidence-grounded first touches and the single follow-up, classify replies,
and run the weekly GTM review. It works alongside the Yempik Company Brain, which holds the
company truth the messages are allowed to assert.

[Agent Skills](https://agentskills.io/specification) format (`SKILL.md` with `name` and
`description` frontmatter). Works in Claude Code, Claude.ai, Codex and any client that
supports the standard.

## The guarantee

**The agent drafts. It never sends.** No email, no calendar acceptance, nothing published. If
a connected tool exposes a send mode, the skill does not call it, however the request is
phrased. Send and delete stay with a human, always. Alongside it: no pipeline stage advances
without a dated, verifiable event, so the pipeline describes facts rather than hopes.

## Requirements

| Connector | Status | Without it |
|---|---|---|
| Email | **Required.** Thread search, message bodies, draft list. | Not installable: without reply verification the system is blind. |
| Enrichment | Optional | Sourcing runs on public sources only, which is already the observed default. |
| CRM | Optional | The pipeline file becomes the only record, and that must be declared. |
| Calendar | Optional | Slots are proposed and a human verifies the conflicts. |

Full requirements and the acceptable degradations are in `references/connectors.md`; who may
do what per connector is in `references/permissions.md`.

Before the first run, three things must be ratified in the Company Brain: the ICP with its
exclusions, the approved claims, and the send authorisation rule. Without them the skill
refuses to enter outreach. See `references/setup-and-intake.md`.

## Install

```bash
npx skills add yempik-ai/yempik-skills
```

The two governed routines (`gtm_followup_engine`, `gtm_weekly_review`) are activated from the
Yempik platform, not from the client: install the GTM Engineer pack from its card at
[brain.yempik.ai](https://brain.yempik.ai) and approve the routine proposals in your Inbox.
Scopes required: `brain:read`, `brain:propose`, `routines:read`, `routines:execute`.

## Motion profile

Valid for founder-led outbound: low volume, high touch, email primary, human send authority.
Not for high-volume or multi-domain outbound, not autonomous sending, not a CRM replacement,
not an enrichment-platform replacement.

---

# Yempik GTM Engineer (italiano)

Agent Skill per l'outbound gestito dal founder: costruire un universo di account, assegnargli
un punteggio, far approvare la lista, scrivere primi tocchi fondati su evidenze e l'unico
follow-up previsto, classificare le risposte e condurre la review GTM settimanale. Lavora
insieme al Company Brain di Yempik, che custodisce la verità aziendale che i messaggi possono
affermare.

Formato [Agent Skills](https://agentskills.io/specification) (`SKILL.md` con frontmatter
`name` e `description`). Compatibile con Claude Code, Claude.ai, Codex e ogni client che
supporta lo standard.

## La garanzia

**L'agente prepara bozze. Non invia mai.** Nessuna email, nessun invito accettato, niente di
pubblicato. Se uno strumento collegato espone una modalità di invio, la skill non la chiama,
comunque sia formulata la richiesta. Invio ed eliminazione restano sempre a una persona.
Insieme a questo: nessuno stato della pipeline avanza senza un evento datato e verificabile,
così la pipeline descrive fatti e non speranze.

## Requisiti

| Connettore | Stato | Se manca |
|---|---|---|
| Email | **Obbligatorio.** Ricerca thread, corpo dei messaggi, elenco bozze. | Non installabile: senza verifica delle risposte il sistema è cieco. |
| Enrichment | Opzionale | Il sourcing lavora solo su fonti pubbliche, che è già il comportamento osservato. |
| CRM | Opzionale | Il file di pipeline diventa l'unico registro, e va dichiarato. |
| Calendario | Opzionale | Gli slot si propongono e i conflitti li verifica una persona. |

Requisiti completi e degradazioni accettabili in `references/connectors.md`; chi può fare
cosa su ogni connettore in `references/permissions.md`.

Prima del primo run servono tre ratifiche nel Company Brain: l'ICP con le sue esclusioni, i
claim approvati e la regola di autorizzazione all'invio. Senza, la skill si rifiuta di entrare
in outreach. Vedi `references/setup-and-intake.md`.

## Installazione

```bash
npx skills add yempik-ai/yempik-skills
```

Le due routine governate (`gtm_followup_engine`, `gtm_weekly_review`) si attivano dalla
piattaforma Yempik, non dal client: installa il pacchetto GTM Engineer dalla sua card su
[brain.yempik.ai](https://brain.yempik.ai) e approva le proposte di routine nell'Inbox. Scope
richiesti: `brain:read`, `brain:propose`, `routines:read`, `routines:execute`.

## Profilo del motion

Valida per outbound gestito dal founder: volumi bassi, alto tocco, email come canale
primario, autorità di invio umana. Non per outbound ad alto volume o multi-dominio, non per
l'invio automatico, non è un sostituto del CRM né di una piattaforma di enrichment.
