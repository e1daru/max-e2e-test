"""Log parser from our weekend project: groups agent runs by trace ID."""


def group_runs(lines):
    runs = {}
    for line in lines:
        trace, _, event = line.partition(" ")
        runs.setdefault(trace, []).append(event)
    return runs
