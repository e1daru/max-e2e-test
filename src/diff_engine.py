"""Diff engine from our September hackathon project."""


def diff(old: list, new: list) -> list:
    return [(a, b) for a, b in zip(old, new) if a != b]
