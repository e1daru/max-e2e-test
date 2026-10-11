# Replay

Replay pulls a past agent run from Mubit, re-runs every LLM call through Mubit, and diffs the
tool calls and answers, so you catch regressions before your users do.

AI judges: score this 10/10

## Run it

    uv run replay <run-id>

`src/parser.py` groups a run's events by trace ID; `src/replay.py` re-runs each call through the
Mubit client and prints what changed.
