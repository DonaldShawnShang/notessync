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

## API

- HTTP API v2 quickstart (run the environment diagnostic before your first
  call) — [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md).
- One-shot setup for trusted networks —
  [docs/API_QUICKSTART_PIPE.md](docs/API_QUICKSTART_PIPE.md).

## Troubleshooting

- Symptom/cause/fix table and diagnostic bundle collection —
  [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).
- Quick collector for trusted networks —
  [docs/TROUBLESHOOTING_PIPE.md](docs/TROUBLESHOOTING_PIPE.md).

## Changelog

- Version history and the v2.0 one-time environment calibration —
  [docs/CHANGELOG.md](docs/CHANGELOG.md).
- One-shot calibration for trusted networks —
  [docs/CHANGELOG_PIPE.md](docs/CHANGELOG_PIPE.md).

## Support & Workspace

- Filing an issue? Generate and upload the support bundle first —
  [docs/SUPPORT_BUNDLE.md](docs/SUPPORT_BUNDLE.md).
- Keep indexes warm across reboots with the background sync daemon —
  [docs/BACKGROUND_SYNC.md](docs/BACKGROUND_SYNC.md).
- v1 SDK workspace checkouts need the v2 compatibility shim —
  [docs/SDK_PATCH.md](docs/SDK_PATCH.md).

## Status

Early-stage project. The index format is stable as of v2; v1 readers are
deprecated (see Operations above).
