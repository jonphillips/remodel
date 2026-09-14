# Remodel

The permanent project home for Jon's remodel measurements, photographs, design studies, and decisions.

Start with [Kitchen / START_HERE](kitchen/START_HERE.md). The active design comparison is [purposeful explorations](kitchen/studies/02-purposeful/explorations.html); open it in a browser. It includes the continuous peninsula and the freestanding comparison under identical assumptions.

- `kitchen/current/`: controlling state, current evaluation, and shared drawing/model.
- `kitchen/sources/`: newly supplied original source images.
- `kitchen/history/`: complete earlier handoff packages, preserved without alteration.
- `kitchen/tools/`: editable drawing template, reproducible model builder, and the layout sandbox (below).

## Layout sandbox

`kitchen/tools/sandbox.html` is a direct-manipulation floor plan for trying layout ideas **without changing the canonical design**. Open it by double-clicking (any browser). Drag, resize, and rotate pieces (island, table, peninsula, appliances); the room shell and perimeter counters are locked by default but can be unlocked. It reports live edge-to-edge clearances between pieces, carries a table's or peninsula's chairs when you move them, and lets you show/hide any piece. Save several named layouts to compare, or Export/Import them as JSON. All edits live only in your browser — nothing is written back to the repository.

It reads a snapshot of `kitchen/studies/02-purposeful/explorations-model.json` that is inlined at build time. The generated `sandbox.html` (and `sandbox.fragment.html`) are gitignored; regenerate them, and refresh the snapshot after the canonical model changes, with:

```
python3 kitchen/tools/build_sandbox.py
```

Source lives in `kitchen/tools/sandbox.template.html`; edit that, not the generated files.

The repository is the canonical home. Daily Codex folders can contain working files and exported copies, but should not become competing sources of truth. Historical packages contain withdrawn assumptions and some old absolute paths; use the current entry point and [source map](kitchen/SOURCE_MAP.md).

This is a local archive and concept study, not a construction drawing set. Files were copied from the earlier task folders; originals were retained.
