# Validation record

September 13, 2026

- Reconstructed the display coordinates by an inverse rigid transformation of the prior qualified combined geometry. Checked C3–M2, C3–M4, M2–M4 and C3–M5 distance preservation numerically.
- Preserved the source residuals and did not edit the prior source files.
- Checked candidate footprint arithmetic, chair-projection arithmetic and the approximately 66.568-inch table span. These are design-model calculations, not field validation.
- Passed `node --check` on the visualization's extracted JavaScript.
- Inspected the actual browser rendering at 736 pixels, then 360 and 320 pixels. The narrow layouts had matching content and scroll widths: 328/328 and 288/288 pixels, respectively.
- Verified A/B/C selection, occupied/pulled-out chair state, door/appliance-envelope toggle, and earlier-counter-edge toggle. Verified updated drawing labels and explanatory state. Final browser console check returned no errors or warnings.
- Used a loopback-only preview after the sandbox required approval to bind the preview server. Approval was granted. No browser URL-policy bypass was used.

Not validated: actual doors/hinges, refrigerator and wall-oven coordinates and open states, exact chair/person poses, family-room boundaries, range-connection construction, cabinet engineering, actual appliance specifications, sink landings, utilities, or a continuous occupied route. The assumed French-door model does not reconcile the field chair observations and is explicitly excluded from actual clearance findings.

Files: `layout-tradeoff-review.md` is the human-readable decision record; `layout-study.json` contains source provenance, proposed footprints, assumptions and calculations. The interactive drawing is conversation content.
