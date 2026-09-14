# Remodel

The permanent project home for Jon's remodel measurements, photographs, design studies, and decisions.

Start with [Kitchen / START_HERE](kitchen/START_HERE.md). The active design comparison is [purposeful explorations](kitchen/studies/02-purposeful/explorations.html); open it in a browser. It includes the continuous peninsula and the freestanding comparison under identical assumptions.

- `kitchen/current/`: controlling state, current evaluation, and shared drawing/model.
- `kitchen/sources/`: newly supplied original source images.
- `kitchen/history/`: complete earlier handoff packages, preserved without alteration.
- `kitchen/tools/`: editable drawing template, reproducible model builder, and the layout sandbox (below).

## Layout sandbox

A direct-manipulation floor plan for trying layout ideas **without changing the canonical design**. Open by double-clicking (any browser). Two scopes, built from the same tool:

- `kitchen/tools/sandbox.html` — **kitchen only**, to stay focused on the kitchen.
- `kitchen/tools/sandbox-porch.html` — **kitchen + the reclaimable old porch** (161 × 111 in ≈ 124 sq ft, per [EVALUATION.md](kitchen/current/EVALUATION.md)), placed against the confirmed kitchen-facing partition (X = 5.8247) and left editable, since the porch interior origin/setback is not yet fully reconciled. The new giant screened porch beyond M5 is not dimensioned in the repo and is not included.

Drag, resize, rotate, and round the corners of pieces (island, table, peninsula, appliances, porch); the room shell and perimeter counters are locked by default but can be unlocked. It reports live edge-to-edge clearances between pieces, carries a table's or peninsula's chairs when you move them, and lets you show/hide any piece. Save several named layouts to compare, or Export/Import them as JSON. All edits live only in your browser — nothing is written back to the repository.

Each sandbox inlines a snapshot of `kitchen/studies/02-purposeful/explorations-model.json` at build time. Regenerate the sandboxes, and refresh the snapshot after the canonical model changes, with:

```
python3 kitchen/tools/build_sandbox.py
```

Files in `kitchen/tools/` (all sandbox files):

- `sandbox.template.html` — the single source for both sandboxes (edit this one).
- `build_sandbox.py` — inlines the model snapshot and writes both scopes below.
- `sandbox.html` — generated, kitchen-only standalone page.
- `sandbox-porch.html` — generated, kitchen + porch standalone page.
- `sandbox.fragment.html`, `sandbox-porch.fragment.html` — generated, head/body-less versions used only for publishing as Artifacts.

The four generated files (`sandbox*.html`, `sandbox*.fragment.html`) are gitignored — edit the template, not them.

The repository is the canonical home. Daily Codex folders can contain working files and exported copies, but should not become competing sources of truth. Historical packages contain withdrawn assumptions and some old absolute paths; use the current entry point and [source map](kitchen/SOURCE_MAP.md).

This is a local archive and concept study, not a construction drawing set. Files were copied from the earlier task folders; originals were retained.
