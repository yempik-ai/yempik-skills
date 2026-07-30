# yempik-founder-mode

**🇮🇹** Pack di ideazione contrarian per workspace collegati al **Yempik Company Brain**
([brain.yempik.ai](https://brain.yempik.ai)). L'agente mappa prima il consenso (le risposte
che darebbe chiunque), poi forza la divergenza con le tecniche misurate in letteratura, e
infine fonda ogni idea sopravvissuta sulla verità governata del tenant: decisioni attive,
regole, fatti, clienti. Arrivano 3-5 tesi con citazioni dal Brain; un'idea che contraddice
una decisione attiva non muore ma viene promossa a tesi contrarian interna, con l'argomento
del perché rivederla. Quello che il Brain non copre viene etichettato `UNGROUNDED`, mai
travestito da fondato. Propose-only: nulla entra nel Brain senza un sì umano per singola tesi.

**🇬🇧** Contrarian ideation pack for workspaces connected to the **Yempik Company Brain**
([brain.yempik.ai](https://brain.yempik.ai)). The agent first maps consensus (the answers
anyone would give), then forces divergence with the measured techniques from the literature,
and finally grounds every surviving idea in the tenant's governed truth: active decisions,
rules, facts, clients. You get 3-5 theses with Brain citations; an idea that contradicts an
active decision is not killed but promoted to an internal contrarian thesis, arguing the
revisit. Whatever the Brain does not cover ships labeled `UNGROUNDED`, never dressed up as
grounded. Propose-only: nothing enters the Brain without a human yes per single thesis.

## Install

```
/plugin marketplace add yempik-ai/yempik-skills
/plugin install yempik-founder-mode@yempik
```

The plugin declares `yempik-company-brain` as a dependency, so Claude Code installs it too
and the `mcp.yempik.ai` connector comes with it: one connection, one OAuth consent.

`npx skills add yempik-ai/yempik-skills` works as well, but copies the skill text only; you
attach the connector by hand
(`claude mcp add --transport http yempik https://mcp.yempik.ai/mcp`).

**Requires:** the Yempik MCP connector connected and authorized with at least the
`brain:read` scope (`brain:propose` only if you want to turn approved theses into Brain
candidates).
