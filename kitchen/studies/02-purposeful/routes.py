import json
from pathlib import Path
from geometry import gap,rect
R=Path(__file__).parent;d=json.loads((R/'explorations-model.json').read_text())
paths={'F2':[[30,240],[30,210],[32,182],[32,168],[34,160],[47,151.75],[55,144],[55,131],[54.5,112],[54.5,35]],'P2':[[ -15,211],[-15,252],[120,252],[144,218],[144,173],[137,151],[124,123],[55,123],[54.5,112],[54.5,35]]}
for c in d['cases']:
 obs={k:v for k,v in d['fixed'].items() if k not in ['DWdoor','DWloader','chef']};obs.update({'tread':d['stair']['tread'],'cap':d['stair']['cap']})
 obs.update({'part'+str(i):p for i,p in enumerate(c['parts'])});obs.update({'guest'+str(i):p for i,p in enumerate(c['seats'])});obs.update({'table':d['table']})
 for i,p in enumerate(d['table_chairs']):
  if not(c['id']=='P2' and i==2):obs['tablechair'+str(i)]=p
 # Partition is opened in P2, retained in F2. Other opening/rail context remains conditional.
 obs['porchpartition']=rect(0,277 if c['id']=='P2' else d['porch']['start_y_conditional'],d['porch']['partition_x'],100)
 path=paths[c['id']];g=[]
 for a,b in zip(path,path[1:]):
  for k,p in obs.items():g.append((gap([a,b],p)['inches'],k,a,b))
 g.sort();print(c['id'],g[:4]);c['route']={'centerline':path,'min_obstacle_radius':g[0][0],'limiting_obstacle':g[0][1],'conditions':'Four guests; table kitchen-side chair parked and proposed old-porch connection open.' if c['id']=='P2' else 'Four guests; table chairs retained.','meaning':'Minimum clearance of this tested centerline to modeled obstacles. Swept-disk check, not a surveyed whole-room route.'}
 for name,extras in [('helper',[c['helper_person']]),('DW',[d['fixed']['DWdoor'],d['fixed']['DWloader']]),('chef',[d['fixed']['chef']])]:
  limit=min([g[0][0]]+[gap([a,b],p)['inches'] for a,b in zip(path,path[1:]) for p in extras]);c['route'][name+'_diameter']=2*limit
(R/'explorations-model.json').write_text(json.dumps(d,indent=2)+'\n')
