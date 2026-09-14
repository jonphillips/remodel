import json, math
from pathlib import Path

ROOT=Path('/Users/jon/Documents/Codex/2026-09-13/re')
SOURCE=Path('/Users/jon/Documents/Codex/2026-09-13/continue-this-kitchen-redesign-read-start/outputs')
g=json.loads((SOURCE/'combined-geometry.json').read_text())
a=g['island'][0]
u=[(g['island'][1][i]-a[i])/51 for i in range(2)]
v=[(g['island'][3][i]-a[i])/57 for i in range(2)]
def back(p):
    w=[p[i]-a[i] for i in range(2)]
    return [64+sum(w[i]*u[i] for i in range(2)),38+sum(w[i]*v[i] for i in range(2))]
points={k:back(p) for k,p in g['points'].items()}
walls={k:back(p) for k,p in g['wall'].items()}
tc,tf=points['TC'],points['TF']
length=math.dist(tc,tf)
axis=[(tc[i]-tf[i])/length for i in range(2)]
center=[(tc[i]+tf[i])/2 for i in range(2)]
normal=[axis[1],-axis[0]]
# Kitchen-side dining chair: one schematic side chair, not newly measured.
side_rim=[center[i]+24*normal[i] for i in range(2)]
side_back=[side_rim[i]+19*normal[i] for i in range(2)]
checks={
 'table_length':length,
 'guest_frontage_existing_context':79,
 'four_seats_at_24':96,
 'four_seats_test_pitch_30':120,
 'cleanup_face_170_relative_to_measured_lower_157':13,
 'cleanup_outer_195_relative_to_old_upper_190':5,
 'cleanup_mouth_by_working_face':{str(x):x-120 for x in (157,162,170)},
 'mouth_if_27_inch_dishwasher_opens_across_it':170-120-27,
 'B_depth_reduction':51-33,
 'B_family_aisle_to_old_lower':157-(64+33),
 'B_family_aisle_to_test_row':170-(64+33),
 'C_range_aisle':78.5-30.5,
 'C_family_aisle_to_test_row':170-(78.5+33),
 'C_range_aisle_with_27_inch_oven_projection':78.5-30.5-27,
 'island_dining_end_to_peninsula_front':137-95,
 'same_gap_with_20_inch_helper_work_envelope':137-95-20,
 'guest_back_to_schematic_side_chair_back_y_projection':side_back[1]-(179+26),
 'guest_pullout_to_schematic_side_chair_back_y_projection':side_back[1]-(179+36),
}
assert abs(length-66.5683)<.01
for name,target in [('C3', 'M2'),('C3','M4'),('M2','M4'),('C3','M5')]:
 assert abs(math.dist(points[name],points[target])-math.dist(g['points'][name],g['points'][target]))<1e-8
data={
 'status':'Conditional design footprints; no candidate approved. Not a survey, cabinet order, or construction model.',
 'units':'inches',
 'coordinate_note':'Inverse rigid display conversion of combined-geometry.json for axis-aligned concept drawing. Derived wall/table points are NOT replacement field coordinates.',
 'sources':[str(SOURCE/'combined-geometry.json'),str(SOURCE/'CURRENT_STATE.json'),'/Users/jon/Desktop/combined-geometry-review.md'],
 'points':points,'wall':walls,'lower':[back(p) for p in g['lower']], 'upper':[back(p) for p in g['upper']],
 'source_residuals':g['checks'],
 'common_test':{'cleanup':[170,41,25,110],'chef_support':[0,137,120,24],'raised_guest_surface':[0,161,120,18], 'range_connection':[0,135.5,27.5,1.5], 'guest_centers_x':[15,45,75,105], 'guest_width':24,'guest_occupied_projection':26,'guest_pullout_projection':36,'chef_helper_envelope':[24,20], 'route_width_test':42, 'dishwasher':[170,78,25,24], 'dishwasher_open_projection':27},
 'options':{
  'A':{'name':'Continuous peninsula prep','island':None,'chef_center':[60,127],'helper_center':[160,59],'water':[14,139,18,18],'board':[38,139,36,20],'mise':[78,139,36,20],'helper_board':[173,44,19,30]},
  'B':{'name':'Shallower island','island':[64,38,33,57],'chef_center':[107,77],'helper_center':[96,127],'water':[75,42,18,18],'board':[79,62,18,30],'mise':[69,65,10,30],'helper_board':[78,139,36,20]},
  'C':{'name':'Range-facing worktable','island':[78.5,38,33,57],'chef_center':[68.5,75],'helper_center':[96,127],'water':[5,42,18,18],'board':[80.5,48,20,36],'mise':[80.5,84,27,11],'helper_board':[78,139,36,20]}
 },
 'envelope_assumptions':{
  'guests':'30-inch pitch, 24-inch envelope width, 26-inch occupied or 36-inch pullout projection; design allowances, not measured guest chairs. 18-inch raised top requires actual knee-clearance/support design.',
  'dining':'TC chair uses confirmed 23.5-inch width and 19/36 projection with assumed axial pose. TF and two side chairs reuse those sizes only as stress proxies; their actual dimensions and poses are unknown.',
  'appliances':'Range oven 27-inch open projection over 48-inch width is deliberately conservative schematic; dishwasher 24-inch width/27-inch projection is a test module, not selected product.',
  'french_doors':'Optional hypothetical pair of 32-inch leaves, near hinge 3 inches beyond M7, flush continuation of wall, inward 90-degree sweeps. Opening width, hinge, setback, handing and plane are NOT measured. Does not reproduce 37/26.5 field observations; cannot validate actual door use.',
  'appliance_wall':'Refrigerator/ovens are topology-only and intentionally not assigned invented coordinates or swings. Their full access test remains unresolved.'
 },
 'checks':checks
}
(ROOT/'outputs/layout-study.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(checks,indent=2))
