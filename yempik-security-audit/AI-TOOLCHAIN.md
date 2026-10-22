# AI Toolchain Hunting

#### When to use this file

Reach for this file when the repository uses AI in the way it is built or operated, not only in what it ships: AI provider keys, LLM gateways and proxies (LiteLLM, Portkey, in-house routers), AI SDKs, coding-agent and editor configuration committed to the repository (`.claude/`, `CLAUDE.md`, `AGENTS.md`, `.mcp.json`, `.cursor/`, `.vscode/tasks.json`, `.devcontainer/`), MCP servers that developers or automations launch, tracing and evaluation services that store prompts, and CI jobs that run AI tools with write authority. The important data flow is *lower-trust writer → AI toolchain input → execution or credential under a trusted identity*.

Use this alongside `SUPPLY-CHAIN-AND-RELEASE.md` and `AI-AND-LLM.md`, not instead of them. `AI-AND-LLM.md` covers a model inside the product; this file covers the AI tools around the people and pipelines that build and run it. Split large targets into credentials, agent and editor configuration, MCP launch, and AI dependencies.

## Core discipline (include in every agent prompt for this domain)

```
- An AI key, an agent configuration file, or an unpinned AI dependency is not a finding by itself. Name the lower-trust writer or reader, the trusted identity that executes or spends, and the concrete result.
- Treat committed agent, editor, and MCP configuration as code that runs with a developer's or a pipeline's authority. Establish who can change the file, which client reads it, and what that client runs without a separate trust decision.
- Client behavior (whether an editor or agent executes repository configuration, and when it asks first) lives outside the repository. If the decisive fact is the client's behavior for a specific version, record `needs_validation` with that exact client, version, and setting.
- Never call an AI provider, gateway, MCP server, or tracing service to test a credential or an endpoint. Establish exposure from source, build output, and local fixtures only; spend and live access are owner-observed checks.
- Credential findings name the scope that matters: whose budget the key spends, which organization data it reads, which other keys it unlocks. A revoked, dummy, or test-scoped value is not a confirmed exposure.
- Use `confirmed` for source-visible exposure or execution paths established with bounded local evidence. Use `needs_validation` for provider scopes, client defaults, registry state, and hosted CI settings that are not observable.
```

## AI credential attack classes (subagent_type: `research`)

**AI provider keys in reachable artifacts**
Provider keys or gateway keys reach a place a lower-trust principal can read: client bundles and public environment prefixes (`NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_`), committed example files with live-format values, container layers, build logs, error pages, or source maps. Trace the value from definition to the artifact and the artifact to its audience. Confirm the shipped artifact contains it by building locally inside the sandbox; the key's live scope and spend remain owner-observed.

**LLM gateway as a credential concentrator**
One gateway holds every provider key plus a master key, virtual keys, and a database of usage and prompts. Review how administrative routes authenticate, whether the master key has a committed or default value, whether virtual keys are scoped per team, model, and budget, whether stored provider keys are encrypted with a key the gateway process alone holds, and whether lower-trust services on the same network can reach administrative routes. Require a lower-trust caller who gains a key, a budget, or another team's data.

**Secrets and private data in model context and traces**
Prompts, system messages, tool results, or retrieved documents carry credentials or other principals' data, and the same content is persisted to tracing, evaluation, or logging services whose readers have lower trust than the data owner. Read prompt assembly and tracing configuration together. Disclosure to a service with the same readers as the data is not a finding.

## Agent and editor configuration attack classes (subagent_type: `general`)

**Repository-controlled agent and editor execution**
Committed configuration makes a developer's tool run commands or load servers: agent hooks and permission allowlists, project MCP servers enabled by default, editor tasks that run on folder open, devcontainer life-cycle commands, interpreter or formatter paths, `.envrc`. Establish the write path (fork pull requests, bots with merge rights, generated files, dependency updates, a stolen contributor token) and what runs, under which identity, with which environment, when a developer opens the repository or starts an agent. Compare against code owners and branch rules visible in source; hosted branch protection is a `needs_validation` fact.

**Repository text that steers a coding agent**
Instruction files (`CLAUDE.md`, `AGENTS.md`, rules directories), vendored documentation, fixtures, or generated files contain instructions that a coding agent with tool permissions reads as guidance. Prompt injection alone is not a finding. Require that content from a lower-trust source reaches the agent's instruction or context set, and that a deterministic setting in the repository (an auto-approved tool, a permissive allowlist, a hook) lets that content cause an action the developer did not request.

**MCP servers launched from mutable sources**
Configuration launches MCP servers through package runners with floating versions (`npx -y`, `@latest`, `uvx` without a pin), from personal forks, or as remote servers without authentication, and passes them broad environment variables or file-system roots. Trace the launch command, the version binding, the environment and paths handed over, and the trusted identity that starts it. A pinned server from a reviewed source with a narrow environment is not a finding.

## AI dependency and automation attack classes (subagent_type: `general`)

**Unbound AI SDKs and gateway images in privileged contexts**
AI SDKs, gateways, and agent frameworks resolve to versions that can change without review (open ranges, no lockfile or hashes, mutable image tags) inside a process or job that holds production secrets or publish rights. Prove the consumer: which build, job, or service installs it and which secrets exist in that context at install or start-up time.

**Start-up and install hooks**
Code executes before any application logic: Python path configuration files and site customization, package install scripts, native addons loaded on import, container entrypoints that install packages at start-up. Identify which hooks the repository vendors, generates, or permits, and whether installs run where credentials are present. Name the hook and the credential set it can reach.

**AI automation with write authority**
CI jobs or bots run an AI agent or apply model-generated changes with repository write tokens, package publish rights, or deployment credentials, while their input includes lower-trust content (issue bodies, pull request text from forks, external documents). Compare trigger, input source, token permissions, and whether a human approves the exact change before it lands.

## Universal moves (apply across the above)

- Draw the AI toolchain map first: every AI credential and where it lives, every configuration file a tool executes, every MCP launch, every AI dependency with the process that loads it. Then connect each lower-trust writer to a trusted identity.
- Start from the most valuable credential (gateway master key, organization-wide provider key, publish token) and walk backward to every place that can read it or every process that runs beside it.
- Compare developer laptops, CI, and production for the same tool. The weakest context that holds the strongest credential sets the priority.

## Validation rules (apply before reporting ANY finding here)

1. Name the lower-trust writer or reader, the AI toolchain input they control, the trusted identity that executes or spends, and the resulting credential exposure, unauthorized execution, or data disclosure.
2. For credential claims, show the value in a reachable artifact built locally or committed in source, and state what the scope would allow. Never test a key against a live service.
3. For configuration claims, cite the committed file, the write path into it, and the client behavior that executes it. Unknown client behavior for the pinned version is `needs_validation`.
4. For dependency and hook claims, prove the consuming process and the secrets present in it. A mutable version with no privileged consumer is a hardening note.
5. Return `confirmed` only with a complete source-visible path and a meaningful result. Return `needs_validation` with the exact provider scope, client default, registry state, or hosted setting an owner must observe.
