# Kitchen Scaled Base-Plan Survey — v1

**Purpose:** Collect and verify only the coordinates needed to convert the approved topology checkpoint into a proportional, survey-backed existing-condition plan. This is not a design exercise and does not authorize scaling/tracing topology diagram v5.

**Current status:** The first coordinate capture is complete and recorded in `kitchen_existing_conditions_geometry_v1_1.json`. This worksheet remains the verification protocol for resolving the explicitly noted discrepancies before construction geometry or 3D modeling.

## Reference frame

Use the same orientation as topology checkpoint v5:

- **+X:** range side → family-room side (the 51 in chef-axis direction).
- **+Y:** appliance side → dining/window-table side (the 57 in appliance-to-dining direction).
- **Origin O:** the theoretical intersection of the *inside faces* of the range-side and appliance-side walls. If this is not a physical, accessible corner, make the two perpendicular datum lines with painter’s tape/laser and measure from those lines.

Record coordinates as `(X, Y)` in inches, to the nearest 1/2 in when practical. Do not supply diagonals as substitutes for X/Y coordinates.

## Already locked — do not remeasure unless correcting an error

| Item | Known value |
|---|---|
| Island X dimension | 51 in, range edge → family-room/chef edge |
| Island Y dimension | 57 in, appliance edge → dining edge |
| Island range edge → range front | 34 in |
| Island appliance edge → refrigerator front/handles | about 40 in |
| Island dining edge → nearest cleanup counter | 38 in |
| Refrigerator width | 48 in |
| Appliance-side sequence | butler opening 32 in → refrigerator 48 in → counter 29.5 in → ovens 29.5 in → transition |
| Range width | 48 in |
| Range-side counter depth | 27.5 in |
| Prep sink | 4 in from island family-room edge; 6.5 in from island appliance edge |
| Straight lower cleanup run | 76 in |
| Angled peninsula projection/depth | about 60 in |
| Raised guest surface / lower surface depths | 18 in / 24 in |
| Dining table / table-to-window / guest edge-to-table | 48 × 67 in / 30 in / 84 in |

## Captured coordinate checkpoint — 2026-09-12

All values are inches in the datum frame below. The JSON geometry record is authoritative for confidence labels and audit notes.

| Point | Captured value | Status |
|---|---:|---|
| I0 | (64, 38) | Captured; island edges parallel to datum lines. |
| R0 | (30.5, 63.5) | Captured. |
| A0 | (29.5, 0) | Captured. |
| C1 | (190, 41) | Captured far dining-facing counter edge. |
| C2 | (190, 133) | Captured far-edge diagonal start. |
| C3 | (146, 177) | Captured far-edge diagonal end. |
| C4 | (68, 177) | Captured far-edge lower-run end. |
| W1 | (177, 215) nominal | Coordinate needs reconciliation; direct C3→W1 tape is about 54 in. |
| G1 / G2 | (143, 176) / (64, 176) | Captured raised-perch front edge. |
| T1 / T2 | (60, 258) / (126, 258) | Captured kitchen-near table corners. |

## Verification / recapture only

The points below have been captured. Re-measure only to correct a stated uncertainty, preserve the datum/endpoints, and replace the matching audit note rather than silently averaging values.

### 1. Island placement

Captured island **range–appliance corner** (nearest both the range and appliance sides):

`I₀ = (64, 38)`

The other three corners follow from the locked 51 × 57 in dimensions. Island edges were captured as parallel to the two datum lines.

### 2. Range placement

Captured **appliance-side/range-side corner of the range front**:

`R₀ = (30.5, 63.5)`

Re-check only if the 34 in island-range clearance audit fails.

### 3. Appliance-wall placement

Captured X-coordinate of the **range-side edge of the butler-pantry opening**:

`A₀ = (29.5, 0)`

The known 32 / 48 / 29.5 / 29.5 in sequence then locates the refrigerator, counter, and ovens along the appliance side.

### 4. Cleanup/sink geometry — the critical missing chain

The captured C1–C4/G1/G2 values appear in the checkpoint table above. For any corrective capture, provide an `(X, Y)` coordinate from the two datum lines; do not provide a diagonal substitute.

- `C₁` / `C₂` — far dining-facing edge of the straight cleanup/service counter.
- `C₃` / `C₄` — far dining-facing edge of the diagonal and lower cleanup run.
- `G₁` / `G₂` — endpoints of the raised guest-perch front edge.
- `W₁` — nominal far wall corner; reconcile against the direct C3→W1 ≈54 in tape before using it in a scaled plan.

### 5. Dining band

Captured kitchen-near corners: `T₁ = (60, 258)` and `T₂ = (126, 258)`. The known table dimensions locate the remaining corners once its orientation is known. Reconcile the recorded 66 in coordinate span against the separately reported 67 in table length before modeling.

## Capture method

For each point, use a tape or laser from the two datum lines—not a diagonal. A quick floor sketch with values is perfect. Photos with the tape visible are useful for endpoint verification, but measurements remain the authority.

## Output after final verification

The project record must contain:

1. A proportionally drawn existing-condition plan, with measured geometry solid and unresolved geometry visibly provisional.
2. A coordinate update to `kitchen_existing_conditions_geometry_v1_1.json` retaining the confidence label for every point.
3. A/B/C concept overlays on the identical base plan; every moved, expanded, deleted, or reprogrammed surface will be explicit.

## Reclaim-the-diagonal concept test — field checks before reuse

This is **not** an existing-condition capture. It records the measurements needed to validate or reject the current flipped-peninsula/cleanup concept without silently converting a sketch into an as-built plan.

The concept provisionally moves the straight cleanup row 5 in toward the family-room side, from its current captured far edge at X = 190 to a proposed far edge at X = 195. Keeping the confirmed 25 in counter depth would place its kitchen-facing working edge at X = 170. That calculation produces:

- `T2.X = 126` to proposed cleanup working edge `X = 170` = **44 in** at the table corner.
- Proposed peninsula end `X = 120` to proposed cleanup working edge `X = 170` = **50 in**.

These values are provisional test geometry. They are usable only to identify what must be measured next.

Before presenting this option as feasible, capture:

1. The actual maximum counter outer-face location available toward the family-room wall from C1/C2 through the intended lower cleanup termination. Record wall face, trim/baseboard, and any opening/structural constraint separately.
2. The complete lower cleanup termination geometry after it enters today’s diagonal passageway. The counter must not grow into the dining-table approach.
3. The actual table corner, table footprint, and dining-chair pull-back envelope at the proposed passage—not just T2’s nominal coordinate.
4. The clear, walkable route from the kitchen table to the inner kitchen at floor level, including the narrowest point and turning condition. The working target is 42 in minimum at the table corner and preferably more where people turn.
5. Sink, dishwasher, plumbing, electric, and cabinet-depth feasibility for a straight cleanup row in the proposed location.

Do not change C1–C4, W1, or the locked existing measurements until a corrective field capture supports that change. The concept simply releases the diagonal from its assumed role as required circulation/counter geometry.
