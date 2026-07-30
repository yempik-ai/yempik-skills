# Failure modes

Five ways this pipeline produces output that looks right and is not. Each is diagnosable from
the artefact alone, which matters because every one of them ships something readable: nothing
here announces itself as an error.

## FM-1 · Polished median

- **Symptom:** the theses read varied and confident, but each `claim` reduces to an entry on
  the consensus map with a narrower scope or one extra qualifier. The `consensus` fields feel
  strained, as if written to make the claims look opposed to something.
- **Cause:** the denial pass in `references/divergence.md` was run against wording rather than
  meaning, so restatements passed the ban. Often compounded by a consensus map written as
  topics instead of claims, which bans nothing checkable.
- **Correction:** rerun the denial pass with a stricter ban list: every consensus entry plus
  every idea already generated, and the comparison made on the operative claim after stripping
  the phrasing. If the map itself was the weak link, rewrite it as declarative sentences first;
  a ban list that cannot be violated concretely cannot be enforced.

## FM-2 · Fake grounding

- **Symptom:** a `grounding` field carries ids that no tool call in this session returned, or
  relevance lines that describe what an item probably says.
- **Cause:** citations written from memory of the domain rather than from the check, usually
  because the relevance line was deferred and reconstructed afterwards, when the returned
  payload was no longer in context.
- **Correction:** red line, no partial repair. Discard the grounding for every affected thesis
  and rerun `references/grounding.md` from the sub-claim decomposition, recording ids and
  relevance lines at the moment each call returns. A single fabricated citation makes the whole
  output unverifiable, because the reader has no way to tell which of the others were real.

## FM-3 · Persona collapse

- **Symptom:** four or more personas in stage 3 produce the same idea in different vocabulary;
  the persona pass adds count but no tail.
- **Cause:** the personas differ in job title while sharing the incentives and daily friction
  that actually generate ideas, or a celebrity/genius persona slipped in and pulled the set
  toward its stereotype (the persona-collapse study, Xiao et al. 2026).
- **Correction:** swap the persona set for one where the personas are measured on genuinely
  different things (throughput, liability, waiting time, repeat visits) and re-check that no
  named public figure or "expert genius" framing is present. Convergence across personas is
  worth logging: it usually means the domain has one dominant operational constraint, which is
  itself a thesis candidate.

## FM-4 · Feasibility creep in divergence

- **Symptom:** stage 3 returns 8 to 10 ideas instead of 15 to 20, all plausible, none strange.
  The commentary contains judgments: "unrealistic", "would not pass review".
- **Cause:** evaluation ran inside generation. Filtering while generating re-collapses the
  distribution toward the median it was just pushed off, so the tail never reaches stage 4.
- **Correction:** regenerate the stage with the hard rule enforced: no evaluation, no
  filtering, no feasibility talk, nothing quietly omitted for being embarrassing. Feasibility
  is stage 4's verdict and it is cheap there: one lookup kills a bad idea with a citable
  reason, whereas suppression here costs the run its only source of non-obvious material.

## FM-5 · Readiness theater

- **Symptom:** the output uses the grounded contract while the coverage probe found 0 to 4
  relevant active items, or the probe was skipped and coverage asserted from the fact that the
  connector was attached.
- **Cause:** the readiness gate was treated as a formality rather than a binding classification,
  sometimes because the probe ran after ideation, when the answer it should produce was
  already known.
- **Correction:** rerun `references/readiness.md` before anything else, apply the thresholds
  as written, and apply the `UNGROUNDED: Brain coverage on this domain is <blind|thin>` label
  to every affected thesis. An honest thin-coverage run is useful; a thin-coverage run wearing
  the grounded contract is the pack's central claim, falsified.
