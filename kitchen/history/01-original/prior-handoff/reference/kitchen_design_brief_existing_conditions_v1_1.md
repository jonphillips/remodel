# Kitchen Design Brief & Existing Conditions

**Canonical checkpoint:** v1.1 — topology-approved / survey pending  
**Purpose:** Living design brief and authoritative existing-conditions record for the kitchen project. This file is the human-readable source of truth; `kitchen_existing_conditions_geometry_v1_1.json` is its machine-readable companion.

## Status at this checkpoint

The **topology skeleton v4 is approved for placement and relationships only**. It is **not** a scaled plan, a survey, or a coordinate underlay. It establishes which elements connect to which, which side of the island the chef uses, and which areas are open versus cabineted. It does not establish exact perimeter coordinates, angles, lengths, or appliance alignment.

Future 2D drawings and the eventual 3D model must use measured survey geometry. They may use v4 only as a relationship/topology reference. No one may trace, scale, or reverse-engineer dimensions from the v4 image.

### Confidence hierarchy

| Level | Meaning | Current examples |
|---|---|---|
| **LOCKED TOPOLOGY** | Spatial relationship/placement confirmed; may be drawn diagrammatically. | Range side, appliance side, family-room counter turning through the diagonal main sink, straight cleanup/dishwasher run, open range/dining transition, central island, separate guest perch. |
| **LOCKED MEASUREMENTS** | Explicit physical measurement with stated endpoints. | 51 × 57 in island, 34 in island-to-range-front clearance, refrigerator 48 in wide. |
| **UNSURVEYED / SCHEMATIC COORDINATE GEOMETRY** | Location, angle, segment length, or alignment has not been field-surveyed; not usable as construction/model coordinates. | Refrigerator’s apparent position relative to island projections, perimeter angles, counter lengths beyond named measured segments, wall offsets, and all v4 drawing coordinates. |

### Active concept checkpoint — reclaim-the-diagonal cleanup study

The latest design work is a **concept test**, not a revision to existing conditions or a new locked plan. It tests a range-anchored, flipped peninsula with a straight cleanup row moved outward into the footprint of today’s diagonal family-room passageway. The intent is to reclaim trapped diagonal area for useful cleanup/service counter while keeping the dining-table-to-inner-kitchen route as a first-class requirement.

For this test only, the range location is held because moving it may be difficult given the existing exhaust path. The current island is a reference object only; its final size, orientation, and program remain open.

The test uses a provisional 5 in shift of the cleanup row toward the family-room wall. With the row’s kitchen-facing working edge at provisional X = 170, it produces a 44 in route at the captured table corner T2 (X = 126), above the project’s 42 in minimum. It leaves 50 in from the proposed peninsula end at X = 120 to that cleanup working edge. These are **test calculations from a partially captured frame**, not construction dimensions. In particular, the available family-room-side wall clearance, the true table/chair envelope, and the exact lower cleanup termination are unverified.

The corresponding drawing is `cleanup-row-into-diagonal-study.html`. The companion record is `kitchen_flipped_peninsula_cleanup_diagonal_study_v1.md`.
Earlier alternatives and their decision logic are retained in `kitchen_design_history_options_v1.md`; they are not quietly superseded or misrepresented as failures.

## Design brief and governing principles

### The project

Create a serious, highly personal working kitchen that supports one primary cook exceptionally well, gives a helper useful surge capacity without placing that person in the cook’s path, and preserves the kitchen’s social connection to dining and family-room life.

The downstream deliverable includes a reliable **3D model**. Measurements, photographs, and decisions must therefore be captured with named datums, explicit endpoints, units, and confidence labels. A later model is to be built from a field survey—not inferred from photos or a concept-plan image.

### Governing chef principle: protected back, short front

The normal chef position is at the island’s **family-room/chef edge**, looking forward toward the range. The island places the chef on the lee side of the current traffic rotary: the body is less likely to be stampeded by refrigerator, cleanup, and other circulation. This protection and the standing position are the same spatial fact, not separate amenities.

The design problem is to preserve that protected standing condition while compressing the relationship from **chef → board/prep water/trash/mise → heat**. More floor behind the chef is not automatically beneficial if it becomes an inviting traffic route.

### Social and household program

- The kitchen is a working-kitchen / chef’s-table environment, not a conventional entertainment island.
- The guest perch is a **separate social layer**, for conversation, wine, small plates, laptop/appetizer use, and watching the cook. It is not island seating and must not turn guests into through-traffic.
- There are **no chairs around the island**.
- The dining table/window relationship is protected (“sacred”); do not solve kitchen constraints by pushing the table toward the windows.
- The family-room boundary does real architectural work. Annexing family-room territory has a high burden of proof; recover trapped inches inside the working kitchen first.
- A separate offshoot for everyday food/hospitality functions remains a leading but provisional hypothesis. It may absorb non-cooking traffic such as water, ice, coffee, breakfast, snacks, glasses, flatware, and microwave use.
- Do not assume a recycling pullout is required. Compost is handled as a bowl/behavior, not necessarily dedicated cabinetry.
- Do not assume the current range, refrigerator, wall ovens, or their locations are protected in the future design. A 36 in induction range is credible to test alongside a 48 in envelope, not a decision. **Exception for the current reclaim-the-diagonal test:** hold the range where it is because the exhaust limitation makes a range move a high-friction assumption.

### Operational diagnosis

The existing island creates a traffic rotary: refrigerator/appliance access, cleanup/dishwasher activity, range work, and circulation orbit the central object. The current chef cockpit is locally effective but is separated from heat by substantial island depth and a range-side clearance. The current island’s concentrated prep sink/cutting area does not make its full footprint equally useful; adjacent linear mise/staging capacity is repeatedly scarce.

The desired hierarchy is:

> primary chef cockpit → chef mise/slack → optional helper/surge

It is not a default two-person island and not a line that forces a helper through the chef’s heat path.

## Authoritative coordinate language

Do not use compass directions, photo-left/photo-right, or casual “toward the fridge” language as substitutes for axes.

### Named kitchen sides

- **Range side:** wall/side containing the range.
- **Appliance side:** wall/side containing the butler-pantry opening, refrigerator, intermediate counter, and ovens.
- **Family-room side:** family-room opening/boundary side.
- **Dining side:** peninsula/window-table side.

### Named island edges and axes

- **Family-room/chef edge:** edge where the chef stands.
- **Range edge:** island edge nearest the range.
- **Appliance edge:** island edge toward the appliance side.
- **Dining edge:** island edge toward the dining/peninsula side.
- **Chef axis:** family-room/chef edge → range edge. The chef stands at the family-room/chef edge looking toward the range.
- **Appliance-to-dining length axis:** appliance edge ↔ dining edge.

## LOCKED TOPOLOGY — existing-condition skeleton

1. The range occupies the **range side**.
2. The **appliance side** sequence is: **butler-pantry opening → refrigerator → intermediate counter → wall ovens → opening/transition**.
3. A real family-room-side counter/cabinet run exists; it is not an open boundary all the way through. It turns through the **diagonal main cleanup sink**.
4. From that diagonal sink, cabinetry continues as a **straight cleanup/dishwasher run toward the dining side**. These are parts of a continuous bent perimeter counter system, not an invented floating peninsula.
5. The **range/dining transition is open floor/pass-through**, not a counter or cabinetry wrapping that corner.
6. The central island is a freestanding chef work object. Its family-room/chef edge is the normal standing edge; no chairs belong around it.
7. The guest perch is distinct from the chef island and sits as a social boundary/layer beyond the working kitchen. It is not evidence that the kitchen needs island seating.

## LOCKED MEASUREMENTS — existing conditions

All dimensions below are inches unless stated otherwise. “About” retains the uncertainty stated in the original measurement; do not silently promote it to exact survey geometry.

### Island, chef, and immediate clearances

| Item | Value | Endpoint / note |
|---|---:|---|
| Island chef-axis depth | **51 in** | Family-room/chef edge to range edge. Definitive orientation. |
| Island appliance-to-dining length | **57 in** | Appliance edge to dining edge. Definitive orientation. |
| Island to range front | **34 in** | Clearance from island range edge to actual range front. |
| Island to range/counter face | 37 in | Range projects 3 in proud of the counter face. |
| Appliance edge to refrigerator front/handles | about 40 in | Island appliance edge to refrigerator front/handles; not a wall-to-island coordinate. |
| Dining edge to nearest peninsula/cleanup counter | 38 in | Island dining edge to nearest kitchen-side peninsula/counter edge. |
| Chef body to range front | about 97 in | Normal chef body position to range front. |
| Chef body centerline to family-room island edge | 9–10 in | Normal cutting position. |
| Chef body centerline to cutting sweet spot | 18–20 in | Normal cutting position. |
| Family-room island edge to comfortable reach limit | about 28 in | Comfortable useful reach, not stretch reach. |
| Prep-sink position | 4 in from family-room edge; 6.5 in from refrigerator/appliance end | Existing island sink offsets. |

### Chef-core cross section and heat side

| Item | Value | Endpoint / note |
|---|---:|---|
| Chef-core overall cross section | 183.5 in (15 ft 3.5 in) | Family-room-side boundary to opposite fixed range/perimeter condition through island zone. |
| Family-room-side aisle | 42 in | Existing clear aisle. |
| Range width | 48 in | Existing range. |
| Range-side counter depth | 27.5 in | Existing perimeter counter depth. |
| Counter immediately to each side of range | 24 in each | Partly curved/shaped; usable area is not assumed rectangular. |
| Final stair edge to left range edge | 60 in | Along range side. |
| Right range edge to door-jamb opening | 28 in | Along range side. |

### Appliance side

| Item | Value | Endpoint / note |
|---|---:|---|
| Butler-pantry opening | 32 in | Width. |
| Refrigerator | 48 in | Width. |
| Intermediate counter | 29.5 in | Between refrigerator and ovens. |
| Wall ovens | 29.5 in | Width. |

### Cleanup / social / dining band

| Item | Value | Endpoint / note |
|---|---:|---|
| Straight lower cleanup-counter run | 76 in | From family-room entrance end to first reference point before geometry changes. |
| Angled peninsula projection/depth | about 60 in | Projection from straight run toward guest/table side; not diagonal-edge length. |
| Raised guest surface depth | 18 in | Existing surface. |
| Lower kitchen-side surface depth | 24 in | Existing surface. |
| Dining table | 48 × 67 in | Existing table width × length as reported. |
| Table to window/wall | 30 in | Shortest clear distance. |
| Current guest edge to table | 84 in | Shortest clear distance. |

### Survey coordinate checkpoint — 2026-09-12

The following coordinates were supplied against the v1 datum frame: origin at the theoretical intersection of range-side and appliance-side inside faces; **+X = range → family-room** and **+Y = appliance → dining**. Values are in inches. These are the first coordinates eligible for the scaled existing-condition base plan.

| Point | (X, Y) | Definition |
|---|---:|---|
| I0 | (64, 38) | Island range–appliance corner. Island edges confirmed parallel to datum lines. |
| R0 | (30.5, 63.5) | Appliance-side/range-side corner of range front. |
| A0 | (29.5, 0) | Range-side edge of butler-pantry opening. |
| C1 | (190, 41) | Family-room-side end of the **far, dining-table-facing** edge of the straight cleanup/service counter. |
| C2 | (190, 133) | Start of the diagonal in that same far counter edge. |
| C3 | (146, 177) | End of the diagonal in that same far counter edge. |
| C4 | (68, 177) | Dining-side end of the straight lower cleanup-counter far edge. |
| W1 | (177, 215) nominal | Far wall corner of the family-room-to-dining walkway; coordinate is approximate pending reconciliation with direct tape. |
| G1 / G2 | (143, 176) / (64, 176) | Endpoints of raised guest-perch front edge. |
| T1 / T2 | (60, 258) / (126, 258) | Dining-table corners nearest the kitchen. |

**Audit notes:**

- C1–C4 locate the **far dining-table-facing counter edge**, not the island-facing working edge. The straight C1→C2 segment is 25 in deep; its provisional kitchen-facing edge is X = 165, calculated from the captured far edge and not separately field-located.
- C1/C2 share X = 190, so that far edge is parallel to the island’s appliance-to-dining axis. C3/C4 share Y = 177. These are captured relationships, not inferred tracing geometry.
- The current W1 coordinate computes C3→W1 at about 49 in, but the direct field tape is about **54 in**. The direct field measurement controls; W1 remains nominal until its coordinate is reconciled.
- G1/G2 at Y = 176 and T1/T2 at Y = 258 imply an 82 in coordinate gap, while the earlier direct field measurement is 84 in. T2.X − T1.X is 66 in, while the earlier reported table length is 67 in. Retain all values; resolve the 2 in gap and 1 in table-span difference during the next perimeter/table verification rather than averaging or overwriting them.

## UNSURVEYED / SCHEMATIC COORDINATE GEOMETRY

The following must remain explicitly uncertain until a field survey creates a shared datum network:

- Exact refrigerator position and its intersections with island-edge projections.
- Exact position, width portrayal, and apparent overlap of refrigerator in v4.
- Perimeter counter angles, wall offsets, opening locations, and segment coordinates other than the individual measurements above.
- Exact diagonal cleanup-sink angle and the full geometry of the cleanup/peninsula run.
- Exact relation of island ends to appliance-wall segments and the range-wall endpoints.
- Exact alignment of table, guest perch, and chairs/circulation.
- All coordinates, apparent widths, and intersections shown in topology skeleton v4.

### Approximate visual alignment datum — not a measurement

If the **family-room/chef edge** of the island is projected toward the appliance wall, it appears to land **about 6 in inboard from the refrigerator’s right edge** (right edge as viewed facing the refrigerator). This is a visual/alignment observation only. It is not to be used to derive a precise range-edge projection, refrigerator overlap, or model coordinate.

## Measurement and modeling protocol

1. Preserve the confidence level of every datum: measured, approximate visual alignment, topology-only, or unresolved.
2. Record endpoints, face/handle/projection conditions, date, observer, and a shared reference datum for every new field measurement.
3. Establish a surveyed 2D datum network before making a scaled existing-condition plan or 3D model.
4. Build the eventual 3D model from the surveyed coordinate record, including walls, openings, ceiling/soffit transitions, counter depths/heights, appliance envelopes, and verified island/perimeter locations.
5. Use photographs to verify topology and visual conditions, never to substitute for dimensions.

## Current design-study queue

The immediate active study is the **reclaim-the-diagonal cleanup test**: retain the range in its current location; use a range-anchored flipped peninsula for chef support plus the separate guest layer; relocate/straighten cleanup into the present diagonal family-room passageway; and protect a genuine dining-table-to-inner-kitchen route. The test’s 5 in outward cleanup shift, 44 in table-corner route, 50 in peninsula-end opening, 120 in peninsula study length, and 24 in / 18 in two-level surfaces are provisional design parameters only. They require an on-site wall, passage, and service survey before they can constrain any 2D or 3D model.

Then return to A/B/C chef-core geometry using the coordinate language and confidence hierarchy above.

- **A — compressed/re-engineered island:** preserve the protected family-room chef position while testing a shallower, heat-translated chef object.
- **B — long, lean chef worktable:** test more useful linear mise/slack while protecting the refrigerator-side relationship and avoiding a new rotary.
- **C — separate cockpit and surge surface:** test whether a distinct helper/slack surface creates better separation without fragmented acreage.

Every study must be evaluated against: protected back; shorter chef-to-heat relationship; about 28 in useful reach; independent surge/slack; refrigerator/cleanup access; no new rotary; dining-table protection; and the rule that unsurveyed geometry is not a scaled plan.
