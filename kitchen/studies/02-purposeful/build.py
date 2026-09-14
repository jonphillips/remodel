from pathlib import Path
import json,math
from geometry import rect,gap,groupgap
R=Path(__file__).parent
B=json.loads((R/'baseline.json').read_text());f=B['fixed']
def seats(x,y,w,kind):
    if kind=='2+2':
        front=[x+21,x+51];ends=[rect(x-26,y+3,26,24),rect(x+w,y+3,26,24)]
        knee=[rect(x,y+3,15,24),rect(x+w-15,y+3,15,24)]
        pulled=[rect(x-36,y+3,36,24),rect(x+w,y+3,36,24)]
        labels=['1','2','3','4'];daily=[0,1]
    else:
        front=[x+15,x+45,x+75];ends=[rect(x+w,y+3,26,24)]
        knee=[rect(x+w-15,y+3,15,24)]
        pulled=[rect(x+w,y+3,36,24)]
        labels=['3','1','2','4'];daily=[1,2]
    return {'seats':[rect(a-12,y+42,24,26) for a in front]+ends,'knee':[rect(a-12,y+27,24,15) for a in front]+knee,'pulled':[rect(a-12,y+42,24,36) for a in front]+pulled,'labels':labels,'daily_indices':daily}
F={'id':'F2','name':'Rectangular 2+2','top':rect(84,165,72,42),'top_rect':[84,165,72,42],'parts':[rect(84,165,72,42)],'helper':rect(99,165,42,18),'board':rect(105,165,24,18),'helper_person':rect(105,145,24,20),'mise_parts':[f['landing']],'attachment':[],'opening_assumed':False,**seats(84,165,72,'2+2')}
P={'id':'P2','name':'Stair-side working elbow','top':rect(6,166,90,42),'top_rect':[6,166,90,42],'parts':[rect(6,166,90,42),rect(6,135.5,30,30.5)],'helper':rect(39,166,42,18),'board':rect(45,166,24,18),'helper_person':rect(51,146,24,20),'mise_parts':[f['landing'],rect(6,135.5,30,30.5)],'attachment':[rect(6,135.5,30,30.5)],'opening_assumed':True,**seats(6,166,90,'3+1')}
for c in [P,F]:
    body=c['seats'];daily=[body[i] for i in c['daily_indices']]
    c['metrics']={
     'island_to_top':gap(f['island'],c['top']),
     'island_to_helper_person':gap(f['island'],c['helper_person']),
     'free_end_bare_to_cleanup':gap(c['top'],f['cleanup']),
     'east_end_occupied_to_cleanup':gap(body[-1],f['cleanup']),
     'east_end_occupied_to_DW_door':gap(body[-1],f['DWdoor']),
     'east_end_occupied_to_DW_loader':gap(body[-1],f['DWloader']),
     'DW_loader_to_top':gap(f['DWloader'],c['top']),
     'helper_to_DW_loader':gap(f['DWloader'],c['helper_person']),
     'hosting_to_table_chairs':groupgap(body,B['table_chairs']),
     'hosting_to_table_without_near_chair':groupgap(body,[B['table']]+B['table_chairs'][:2]+B['table_chairs'][3:]),
     'both_sets_pulled':groupgap(c['pulled'],B['table_pulled']),
     'guest_edge_to_near_table_chair':B['table_center'][1]-24-19-(c['top_rect'][1]+42),
     'stair_to_near_guest':groupgap(body,[B['stair']['cap'],B['stair']['tread']]),
     'west_end_to_landing':gap(body[-2],f['landing']) if c is F else None,
     'west_bare_to_landing':gap(c['top'],f['landing']) if c is F else None,
    }
    # Flat top occupancy and independent work surfaces: ensure every chair knee is within the top.
    def insidebox(p,r):x,y,w,h=r;return x-1e-6<=p[0]<=x+w+1e-6 and y-1e-6<=p[1]<=y+h+1e-6
    assert all(insidebox(p,c['top_rect']) for k in c['knee'] for p in k)
    assert len(body)==4 and len(daily)==2
    c['fit_status']='Conditional concept, not approved for construction or all operating states.'
B['cases']=[P,F];B['version']='2026-09-14 purposeful explorations v2'
B['scope']='Two distinct design explorations; shared fixed core and operating assumptions. 2+2 stool arrangement for F2; 3+1 for connected P2. Two everyday places in each. Opening and parked table chair are explicit P2 dependencies.'
B['stair_base_opening_test']={'wall_y':B['porch']['start_y_conditional'],'x_span':[-33,3],'clear_width':36,'status':'Conditional existing-or-widened stair-base door opening; actual jambs, retained piers and floor level unmeasured. Required for the P2 tested route.'}
B['opening_test']={'partition_x':B['porch']['partition_x'],'from_y':B['porch']['start_y_conditional'],'to_y':277,'width':277-B['porch']['start_y_conditional'],'status':'Proposed roughly 48-inch clear table-facing opening at stair-side end of old porch partition. Structural piers, stair-base door opening, floor levels and actual clear dimensions not established.'}
(R/'explorations-model.json').write_text(json.dumps(B,indent=2)+'\n')
print(json.dumps({c['id']:{k:(round(v['inches'],1) if isinstance(v,dict) else v) for k,v in c['metrics'].items()} for c in [P,F]},indent=2))
