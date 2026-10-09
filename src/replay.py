"""Replay a past agent run through Mubit and diff the results."""
import mubit


def load_run(run_id: str) -> dict:
    return mubit.Client().runs.get(run_id)


def replay(run_id: str) -> list:
    run = load_run(run_id)
    return [mubit.Client().calls.rerun(call) for call in run["calls"]]
