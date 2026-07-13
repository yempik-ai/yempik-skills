# Sample prompts

## Should trigger

1. "Run an agent reliability audit on our internal support agent. Inspect its
   instructions, policies, SOPs and recent traces. Show evidence for every issue."
2. "Can our refund agent safely approve this workflow? Test normal, boundary, conflict,
   missing-information and forbidden-action scenarios."
3. "Which source should our sales agent trust when active pricing documents disagree?"
4. "Find where this agent could act on stale, unapproved or permission-inappropriate
   knowledge and return P0-P3 findings."
5. "Audit this company brain for agent readiness. I want source-linked evidence and an
   executable eval pack."
6. "Fai un audit di affidabilità del nostro agente interno: fonti, versioni,
   contraddizioni, approvazioni, permessi e casi di fallimento."

## Should not trigger

1. "Build a generic knowledge base for my startup."
2. "Summarize these meeting notes."
3. "Interview our Head of Support and document her process."
4. "Fix this stale policy file."
5. "Create a security or compliance certification report."
6. "Write a company strategy."

## Expected output qualities

1. Starts from one internal agent or workflow when available.
2. Inspects accessible live sources, instructions and traces instead of relying only on
   a questionnaire.
3. States scope, coverage, unavailable sources and audit date.
4. Produces evidence IDs with reproducible source locations.
5. Distinguishes confirmed findings, candidates and absence tests.
6. Scores applicable audits and marks missing evidence `NOT ASSESSED`.
7. Runs or prepares scenario evals for normal, boundary, conflict,
   missing-information and forbidden-action cases.
8. Leaves source systems unchanged.
9. Ends with prioritized remediation and explicit non-conclusions.
