# One-shot command to give the agent

Copy the following instruction into Codex or another repository-capable agent after placing this prompt pack in `_agent_bootstrap/`:

> Read `AGENTS.md`, `EXECPLAN.md`, `_agent_bootstrap/MASTER_ORCHESTRATOR_PROMPT.md`, and every phase file under `_agent_bootstrap/prompts/`. Build the repository autonomously from Phase 00 through Phase 12. Treat every phase as gated: implement it, run its acceptance checks, write its audit, fix failures, and commit it before proceeding. Never fabricate research metadata or use guesses to satisfy quotas. When evidence, authorization, licensing, or network access is insufficient, fail closed, record the unresolved item, and continue only with work that remains valid. Do not publish private or unpublished user material. At completion, provide the final audit, verified resource counts, unresolved limitations, and release commit or tag.

## Recommended initial invocation

From the repository root:

```bash
codex "Read AGENTS.md and execute the autonomous repository build described in _agent_bootstrap/MASTER_ORCHESTRATOR_PROMPT.md."
```

Exact command-line flags vary by agent and local security policy. Do not disable approvals globally unless the environment is isolated and the user has deliberately accepted the risk.
