"""Rebuild the paired concept and local edge diagnostics. Python standard library only."""
import json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
old = json.loads((ROOT/'history/02-full-room/room-fit-study.json').read_text())
state = json.loads((ROOT/'history/03-porch-checkpoint/CURRENT_STATE.json').read_text())
def rect(x,y,w,h): return [[x,y],[x+w,y],[x+w,y+h],[x,y+h]]
def inside(p,poly):
    x,y=p; hit=False
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]: hit=not hit
    return hit
def project(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy))) if dx*dx+dy*dy else 0
    return [a[0]+t*dx,a[1]+t*dy]
def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def intersect(a,b,c,d):
    v=[cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)]
    return v[0]*v[1]<0 and v[2]*v[3]<0
def gap(a,b):
    if any(inside(p,b) for p in a) or any(inside(p,a) for p in b): return {'inches':0,'segment':None}
    out=(float('inf'),None)
    for c,d in zip(a,a[1:]+a[:1]):
        for e,f in zip(b,b[1:]+b[:1]):
            if intersect(c,d,e,f):return {'inches':0,'segment':None}
    for aa,bb in [(a,b),(b,a)]:
        for p in aa:
            for c,d in zip(bb,bb[1:]+bb[:1]):
                q=project(p,c,d);dist=math.dist(p,q)
                if dist<out[0]:out=dist,[p,q]
    return {'inches':round(out[0],3),'segment':out[1]}
def groupgap(aa,bb):return min((gap(a,b) for a in aa for b in bb),key=lambda d:d['inches'])
# Latest user correction: square extended table, fixed 30.5-inch rear wall gap.
# Rear window wall shares the confirmed partition far-end plane.
cx=(old['points']['TC'][0]+old['points']['TF'][0])/2
rear_wall_y=state['porch_registration']['conditional_registration']['partition_deck_side_end_y_if_120_uses_same_start_corner']
cy=rear_wall_y-30.5-24
old['table']=[]
for side,angles in [(1,range(-90,91,3)),(-1,range(90,271,3))]:
    for angle in angles:
        a=math.radians(angle);old['table'].append([cx+side*9.5+24*math.cos(a),cy+24*math.sin(a)])
def table_chairs(depth):return [rect(cx+33.5,cy-11.75,depth,23.5),rect(cx-33.5-depth,cy-11.75,depth,23.5),rect(cx-11.75,cy-24-depth,23.5,depth),rect(cx-11.75,cy+24,23.5,depth)]
old['table_chairs']=table_chairs(19)
old['table_pulled']=table_chairs(36)
c=old['cases'][3]
guest=c['guest']; helper=rect(78,148,42,18)
# One identical social shape; only this connecting surface changes between cases.
connector=[[36,114.5],[78,148],[78,166],[66,166],[36,135.5]]
model={
 'version':'2026-09-14 paired connection test v1','units':'inches',
 'status':'Conditional concept comparison; neither candidate is approved as a complete occupied fit.',
 'fixed':{k:v for k,v in old['fixed'].items() if k not in ['oven','ovenUser','landing36']},
 'stair':old['stair'],'points':old['points'],'table':old['table'],
 'table_center':[cx,cy],'rear_window_wall_y':rear_wall_y,'table_rear_wall_gap':30.5,
 'table_chairs':old['table_chairs'],'table_pulled':old['table_pulled'],
 'guest':guest,'helper_surface':helper,'helper_person':rect(84,128,24,20),
 'helper_board':rect(84,148,24,18),'helper_landing':rect(108,148,12,18),
 'seated':c['seated'],'pulled':c['pulled'],'knee':c['knee'],'connector':connector,
 'appliances':{
  'pantry_x':[29.5,61.5],'fridge_x':[61.5,109.5],
  'counter_x':[109.5,139],'ovens_x':[139,168.5],
  'fridge_front_y_approx':-2,
  'fridge_front_basis':'Island appliance end Y38 minus reported approximately 40-inch clearance to refrigerator front/handles. Conditional cross-source derivation, not a measured face coordinate.',
  'oven_front_y':None,'oven_front_sensitivity_default':-2,
  'door_projection_default':27,'operator_depth_default':20,
  'scope':'X sequence from A0 and recorded widths. Oven Y face unknown. All appliance door extents are sensitivity proxies, not actual product dimensions; side-by-side fridge door sweep and pullout travel need capture.'},
 'porch':{'partition_x':5.82468580682476,'start_y_conditional':228.91370358678918,'end_y_conditional':348.9137035867892,'kitchen_side_length':120,'inside_dimensions':[161,111],'wall_approx':[6,7],
  'placement':'Kitchen-facing partition collinear with tread right edge, confirmed in current user message and IMG_8610. Y endpoints retain sketch interpretation. Interior origin/setback not numerically closed; display interior room separately as a dimensioned context inset.',
  'purpose':'Breakfast/beverage service; no guest seating assumed.'},
 'assumptions':{
  'guest_frontage_each':30,'guest_surface_depth':24,'end_seat_angle_degrees':20,
  'guest_body_width':24,'guest_occupied_projection':26,'guest_pulled_projection':36,'knee_depth_proxy':15,
  'guest_height':'Unselected; knee/support fit remains unresolved.',
  'helper_frontage':42,'helper_depth':18,'body':[24,20],
  'table':'Latest user correction: square to room, 30.5 inches between rear table edge and window wall; that wall shares the far end of the 120-inch partition. 67 × 48 extended size retained; original approximate 66-inch tie history preserved separately. Lateral center X retained from prior conditional registration, not newly measured. Chair poses remain assumptions.',
  'walls':'M5 orthogonal directions only, no reconstructed trim or door sweeps. Higher stair/rail envelope unknown.',
  'connector':'Shaped link touching existing study landing and guest/helper surface; roughly 14–16 inches normal to its diagonal sides, with wider terminal junction. A shallow transfer/landing link, not a new full-depth cabinet run.'}
}
f=model['fixed']; parts=[guest,helper]
metrics={
 'range_aisle':48,'cleanup_aisle':42.5,'island_to_helper_front':44,
 'island_to_helper_body':24,
 'west_gate_bare':groupgap([f['landing']],parts),
 'west_gate_occupied':groupgap([f['landing']],parts+model['seated']),
 'east_tip_to_cleanup':groupgap(parts,[f['cleanup'],f['rear']]),
 'DW_door_to_social':groupgap(parts,[f['DWdoor']]),
 'DW_loader_to_social':groupgap(parts,[f['DWloader']]),
 'helper_to_DW_loader':gap(model['helper_person'],f['DWloader']),
 'guest_to_table_chair':groupgap(model['seated'],model['table_chairs']),
 'guest_to_table':groupgap(model['seated'],[model['table']]),
 'both_chair_sets_pulled':groupgap(model['pulled'],model['table_pulled']),
 'connector_to_island':gap(connector,f['island']),
 'connector_to_tread':gap(connector,model['stair']['tread']),
 'connector_to_cap':gap(connector,model['stair']['cap']),
 'note':'Edge-to-edge distances expose local constrictions. They are not continuous-route widths, code checks, or full collision-free route certifications.'}
model['metrics']=metrics
(ROOT/'current/comparison-model.json').write_text(json.dumps(model,indent=2)+'\n')
state['checkpoint']='2026-09-14 discussion update: table squared and anchored 30.5 inches from confirmed rear window-wall plane; 2+2 seating and enclosed stair-side counter authorized for exploration.'
state['table_correction']={'dimensions':[67,48],'center':[cx,cy],'rear_window_wall_y':rear_wall_y,'rear_edge_y':cy+24,'rear_wall_gap':30.5,'orientation_degrees':0,'status':'Relative placement fixed by user; lateral X retains previous conditional center under fixture. Global frame and S1 residual remain conditional.'}
state['program']['table']='Normally extended; square to principal walls; rear edge 30.5 inches from window wall; position under light fixture fixed.'
state['discussion_updates']={'stair':'Jon is comfortable enclosing exposed banister and reclaiming some adjacent space for more mise; extent not yet designed. Do not infer removal of required stair space.','seating':'Test two daily far-side seats and two perpendicular occasional end stools, wine/appetizer use, about 20 hosting occasions per year. Three remains an explicit alternative, not a selected reduction.','island':'Fridge-facing end stays at Y38, unchanged from original. 66-inch length extends 9 inches farther toward table than original 57. Jon permits considering a couple inches of final length adjustment later, not a change now.','appliances':'Existing access is a lived usable baseline. Generic operating bands are not new evidence of actual appliance interference.'}
state['porch_registration']['explicit_direction']='Kitchen-facing partition and tread right edge are collinear in plan, explicitly confirmed by Jon in current message with IMG_8610.'
state['porch_registration']['conditional_registration']['partition_x']=model['porch']['partition_x']
state['porch_registration']['conditional_registration']['limits']='X alignment now confirmed. 52/120 Y endpoint interpretation retained provisionally; 120 and 111 preserved separately. Small inset and 6–7-inch porch exterior walls explain differing reference chains qualitatively, not an exact numerical closure.'
state['porch_registration']['minimum_next_clarifications']=[]
state['porch_registration']['current_user_clarification']='The screen porch is set in ever so slightly; 6–7 inches for exterior wall. No exact inset supplied.'
state['current_comparison']='comparison-model.json'
state['porch_registration']['current_photo']='../sources/IMG_8610-stair-porch-alignment.jpeg'
state['current_result']='P1 shaped continuous connection closes the already restrictive west approach; its free-end gap to cleanup is inadequate in this specific placement. F1 retains west access but is also restricted. Neither is a selected design; four seats and daily core preserved.'
state['next_task']=['Start from the corrected orthogonal table. Explore a purposeful stair-side working elbow/peninsula and a rectangular 2+2 freestanding social/helper top, with occasional end stools shown separately.','Use the same comparison tool and baseline; avoid unrelated variant galleries.','Revise guest/helper footprint to widen a real route, then compare continuity again. No island shrink, guest reduction, or hall substitution without explicit tradeoff.','Capture actual refrigerator sweep and oven front/open projection for appliance access; approximate refrigerator closed gap is 40 inches.','52/120 endpoints can be confirmed only when exact beverage opening design needs them; no repeat S1 ties.']
state['source_handoff']='../history/01-original'
state['room_fit_study']='../history/02-full-room/room-fit-study.json'
prefixes={
 '/Users/jon/Documents/Codex/2026-09-14/files-pasted-by-the-user-kitchen/outputs/kitchen-next-session':'../history/01-original',
 '/Users/jon/Documents/Codex/2026-09-14/read-users-jon-documents-codex-2026/outputs/full-room-fit':'../history/02-full-room',
 '/Users/jon/Documents/Codex/2026-09-14/read-users-jon-documents-codex-2026/outputs/kitchen-next-turn':'../history/03-porch-checkpoint'}
def portable(v):
    if isinstance(v,dict):return {k:portable(x) for k,x in v.items()}
    if isinstance(v,list):return [portable(x) for x in v]
    if isinstance(v,str):
        for a,b in prefixes.items():v=v.replace(a,b)
        if v.startswith('sources/'):v='../history/03-porch-checkpoint/'+v
        elif v.startswith('new-photos/'):v='../history/01-original/'+v
    return v
(ROOT/'current/CURRENT_STATE.json').write_text(json.dumps(portable(state),indent=2)+'\n')
fragment=(ROOT/'tools/comparison-fragment.template.html').read_text().replace('__MODEL_JSON__',json.dumps(model,separators=(',',':')))
(ROOT/'current/comparison-fragment.html').write_text(fragment)
print(json.dumps(metrics,indent=2))
