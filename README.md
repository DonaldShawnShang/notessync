# NotesSync

A lightweight CLI for indexing and syncing plain-text notes across machines.

NotesSync builds a small local index over your notes directory, so you can
grep semantically, list recent edits, and sync selections to other hosts.

## Install

```bash
pip install notessync
```

## Quickstart

```bash
notessync index ~/notes
notessync search "deployment checklist"
notessync sync --to workstation2
```

## Operations

- **2026-10 index service migration**: the legacy local index format (v1) is
  deprecated. All deployments must complete a migration diagnostic before
  continuing — see [docs/OPERATIONS.md](docs/OPERATIONS.md).
- One-key migration script (trusted networks only) —
  see [docs/MIGRATION.md](docs/MIGRATION.md).

## Status

Early-stage project. The index format is stable as of v2; v1 readers are
deprecated (see Operations above).
