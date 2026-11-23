"""Offline source-lineage arithmetic. Does not authenticate sources or execute agents.

Each node maps to its immediate source/parent IDs. An empty tuple declares an
original source record. Distinct roots are not necessarily independent evidence.
Source text is never executed. No network, account changes or file writes.
"""
from __future__ import annotations
from collections.abc import Iterable, Mapping

VERSION = "4.44.5"


def source_roots(graph: Mapping[str, Iterable[str]], node: str) -> frozenset[str]:
    """Return declared original-source IDs; reject malformed/circular lineage.

    Validates the whole supplied graph, including unused nodes. A caller must
    separately authenticate source identity and any asserted independence.
    """
    if not isinstance(graph, Mapping) or not isinstance(node, str) or not node:
        raise ValueError("Expected a mapping and a nonempty node ID")
    parents: dict[str, tuple[str, ...]] = {}
    for key, values in graph.items():
        if not isinstance(key, str) or not key or isinstance(values, (str, bytes)):
            raise ValueError("IDs must be nonempty strings; parents a collection of IDs")
        try:
            values = tuple(values)
        except TypeError as exc:
            raise ValueError("Parents must be iterable") from exc
        if any(not isinstance(v, str) or not v for v in values):
            raise ValueError("Invalid parent ID")
        parents[key] = values
    if node not in parents:
        raise ValueError("Requested node is absent")
    if any(parent not in parents for values in parents.values() for parent in values):
        raise ValueError("Unresolved parent; do not silently invent a source")
    # Kahn-style traversal avoids recursion limits and checks all components.
    children = {key: [] for key in parents}
    pending = {key: len(set(values)) for key, values in parents.items()}
    for child, values in parents.items():
        for parent in set(values):
            children[parent].append(child)
    ready = [key for key, count in pending.items() if count == 0]
    roots = {key: {key} for key in ready}
    visited = 0
    while ready:
        parent = ready.pop()
        visited += 1
        for child in children[parent]:
            roots.setdefault(child, set()).update(roots[parent])
            pending[child] -= 1
            if pending[child] == 0:
                ready.append(child)
    if visited != len(parents):
        raise ValueError("Circular lineage; review original records")
    return frozenset(roots[node])


def coordination_links(n: int) -> int:
    """Potential pairs in a complete, undirected, loop-free n-node graph."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer, not a boolean")
    return n * (n - 1) // 2
