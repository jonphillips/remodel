import json
import math
from pathlib import Path

root = Path('/Users/jon/Documents/Codex/2026-09-13/re')
base = json.loads((root / 'outputs/layout-study.json').read_text())
a, b = base['points']['M4'], base['points']['M2']
d = math.dist(a, b)
r4, r2 = 76., 170.
u = [(b[i]-a[i])/d for i in range(2)]
v = [-u[1], u[0]]
along = (r4*r4+d*d-r2*r2)/(2*d)
offset = math.sqrt(r4*r4-along*along)
branches=[]
for sign in [-1,1]:
    s=[a[i]+along*u[i]+sign*offset*v[i] for i in range(2)]
    assert abs(math.dist(s,a)-r4)<1e-8
    assert abs(math.dist(s,b)-r2)<1e-8
    branches.append({
        'sign':sign,
        'conditional_kitchen_axis_display_coordinate':s,
        'S1_M4_check':math.dist(s,a),
        'S1_M2_check':math.dist(s,b),
        'predicted_S1_M1_using_older_context_point':math.dist(s,[157,41]),
        'inside_historical_peninsula_rectangle_0_120_137_179':0<=s[0]<=120 and 137<=s[1]<=179,
    })
result={
    'status':'Two consistent direct ties captured. Branch and transverse position require an independent check before a footprint decision.',
    'units':'inches',
    'raw_measurements':{'S1_M4':76,'S1_M2':170},
    'source':'Jon explicitly supplied S1–M4=76 and S1–M2=170 in this task following the named horizontal tie request.',
    'S1_definition':'Vertical corner of bottom kitchen-stair newel shaft nearest M4, at lower-counter height. Decorative cap excluded.',
    'method_status':'Horizontal and same S1 endpoint interpreted from preceding request; not independently verified. No measurement tolerance supplied.',
    'baseline':{'M2_M4':95,'status':'Previously user-reported direct chord, preserved in qualified combined geometry.'},
    'geometry':{'triangle_inequality_slack':r4+d-r2,'projection_from_M4_along_M4_to_M2':along,'unsigned_offset_from_extended_baseline':offset,'branches':branches},
    'branch_assessment':'The positive-sign, dining-side branch is the current photo-consistent working hypothesis, not an independently confirmed field position. Both solutions retained. Do not reject the other solely because its approximate old-frame X is negative.',
    'sensitivity':{
        'note':'Illustrative change of S1–M2 alone by 0.5 inch, holding the other ties exact. This is NOT a supplied or estimated measurement tolerance.',
        'unsigned_offsets':{str(r):math.sqrt(r4*r4-((r4*r4+d*d-r*r)/(2*d))**2) for r in [169.5,170,170.5]},
    },
    'design_implication':'Photo-consistent branch puts the shaft reference inside the historical range-connected peninsula footprint. This flags a potential physical conflict beyond traffic inconvenience; it is conditional and must not be used to claim a new layout fits. That earlier footprint is already superseded for the fixed-wall baseline.',
    'limits':['Post cap, shaft dimensions, stair nosing, landing and arrival space are not captured by one point.','Display orientation and M1 context retain prior registration uncertainty. Original coordinates are not replaced.','No old non-orthogonal wall or hypothetical French-door geometry is used for the stair calculation.'],
    'next_measurement':{'name':'S1_M1','endpoint':'M1, the family-room-entrance end of the same lower straight cleanup working edge that leads to M2.','method':'From the same S1 shaft mark, straight horizontal at lower-counter height. Report obstruction rather than slope or endpoint substitution.','purpose':'Additional bearing and branch check. M1 placement remains older conditional counter context, so retain any residual rather than fitting it away.'},
}
(root/'outputs/stair-registration.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result['geometry'],indent=2))
