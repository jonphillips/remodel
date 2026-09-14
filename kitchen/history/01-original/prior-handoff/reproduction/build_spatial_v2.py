import json, math
from pathlib import Path
root=Path('/Users/jon/Documents/Codex/2026-09-13/re')
old=json.loads((root/'outputs/layout-study.json').read_text())
stair=json.loads((root/'outputs/stair-registration.json').read_text())
def box(x,y,w,h): return [[x,y],[x+w,y],[x+w,y+h],[x,y+h]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [a[i]-b[i] for i in range(2)]
def add(a,b):return [a[i]+b[i] for i in range(2)]
def mul(a,s):return [x*s for x in a]
def point_seg(p,a,b):
 v=sub(b,a)
 if dot(v,v)==0:return math.dist(p,a)
 t=max(0,min(1,dot(sub(p,a),v)/dot(v,v)))
 return math.dist(p,add(a,mul(v,t)))
def inside(p,poly):
 c=False
 for a,b in zip(poly,poly[1:]+poly[:1]):
  if (a[1]>p[1])!=(b[1]>p[1]) and p[0]<(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1])+a[0]:c=not c
 return c
def point_poly(p,poly):return 0 if inside(p,poly) else min(point_seg(p,a,b) for a,b in zip(poly,poly[1:]+poly[:1]))
def pd(a,b):return min([point_poly(p,b) for p in a]+[point_poly(p,a) for p in b])
def band(a,b,near,far):
 v=sub(b,a);L=math.hypot(*v);t=mul(v,1/L);n=[-t[1],t[0]]
 return [add(a,mul(n,-near)),add(b,mul(n,-near)),add(b,mul(n,-far)),add(a,mul(n,-far))]
def social(n,angle):
 start=72.5; length=n*30; y=190;c=math.cos(math.radians(angle));s=math.sin(math.radians(angle))
 l=[start+30,y];r=[start+length-30,y]
 segments=[[sub(l,[30*c,30*s]),l],[l,r],[r,add(r,[30*c,-30*s])]]
 if n==3:counts=[1,1,1]
 else:counts=[1,2,1]
 edge=[segments[0][0],l,r,segments[-1][1]]
 normals=[]
 for a,b in segments:
  t=mul(sub(b,a),1/math.dist(a,b));normals.append([-t[1],t[0]])
 def inset(depth):
  result=[sub(edge[0],mul(normals[0],depth))]
  for i in [1,2]:
   bisector=mul(add(normals[i-1],normals[i]),depth/(1+dot(normals[i-1],normals[i])))
   result.append(sub(edge[i],bisector))
  result.append(sub(edge[-1],mul(normals[-1],depth)))
  return result
 g=inset(24);back=inset(42)
 full=[edge+back[::-1]];guest=[edge+g[::-1]];helper=[g+back[::-1]]
 chairs=[];labels=[]
 for (a,b),count in zip(segments,counts):
  t=mul(sub(b,a),1/math.dist(a,b));normal=[-t[1],t[0]]
  for j in range(count):
   rim=add(a,mul(t,30*(j+.5)));l=add(rim,mul(t,-12));r=add(rim,mul(t,12))
   chairs.append([l,r,add(r,mul(normal,26)),add(l,mul(normal,26))])
   labels.append(add(rim,mul(normal,13)))
 return {'full':full,'guest':guest,'helper':helper,'chairs':chairs,'chair_labels':labels,'nominal_frontage':length,'projected_guest_edge_span':length-60*(1-c),'angle':angle}
mise=box(0,111.5,36,24)
islands={'compact':{'rect':[78.5,38,36,60],'water_module':[96.5,38,18,18],'water_bowl':[98.5,40,14,14],'rear_strip':[98.5,56,14,24]},'long':{'rect':[78.5,38,30,78],'water_module':[78.5,98,30,18],'water_bowl':[86.5,100,14,14],'rear_strip':[98.5,56,8,24]}}
cases={}
for n in [3,4]:
 for ang in [0,20]:
  x=social(n,ang)
  x['checks']={'mise_to_social_min_edge_distance':min(pd(mise,p) for p in x['full']), 'M5_to_guest_chair_min':min(point_poly(old['points']['M5'],p) for p in x['chairs'])}
  for key,v in islands.items():x['checks'][key+'_island_to_social_min']=min(pd(box(*v['rect']),p) for p in x['full'])
  cases[f'{n}-{ang}']=x
assert cases['3-20']['checks']['mise_to_social_min_edge_distance']>cases['3-0']['checks']['mise_to_social_min_edge_distance']
assert all(len(v['chairs'])==int(k[0]) for k,v in cases.items())
data={'status':'Qualified concept geometry; no route, cabinetry or construction approval. Dimensions of proposed objects are design tests.', 'units':'inches', 'points':old['points'], 'stair':stair['geometry']['branches'][1]['conditional_kitchen_axis_display_coordinate'], 'stair_ties':stair['raw_measurements'], 'stair_third_tie_residual':-1.6551535181330053,'lower_context':old['lower'],'islands':islands,'social_cases':cases,
 'fixed_cleanup_test':{'rect':[157,41,25,65],'sink_module':[157,43,25,30],'dishwasher_module':[157,77,25,24],'note':'Working face stays at reported X=157. Nominal 25-inch depth and 65-inch straight length; wall thickness/termination and full landing program unresolved. Modules are allowances, not selected products.'},
 'mise_test':{'rect':[0,111.5,36,24],'old_nominal_rect':[0,111.5,27.5,24],'note':'Test a deeper rectangular left-range landing without extending it toward the stair. Actual old curved footprint and usable gain not established.'},
 'board':[80.5,56,18,24],'intake':[80.5,38,14,18],'offload':[80.5,80,18,18], 'chef':[58.5,58,20,24], 'helper':[105.5,128,24,20],
 'notes':['Old orthogonal kitchen-axis registration remains conditional. M5 is drawn only as a point with corrected axis directions; old estimated trim positions and invented door sweeps are omitted.','Angles are 20-degree inward end-seat tests with 30-inch frontage per guest, 24-inch guest and 18-inch helper depth measured perpendicular to each edge. Joins/support/knee space unresolved.','Dining TC chair uses confirmed 23.5-inch width and 19-inch occupied projection, with assumed alignment. Other three chairs reuse those sizes only as stress proxies.','Guest occupied projection 26 inches and width 24 inches, person rectangles and appliance-open projections are design assumptions.','The compact sink has a very small 18-inch-square module allowance; no faucet, rim, cabinet or plumbing fit is certified.','Min edge distances and point-to-chair distances are local model diagnostics, not continuous route widths or verified physical clearances.']}
(root/'outputs/spatial-comparison-v2.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v['checks'] for k,v in cases.items()},indent=2))
