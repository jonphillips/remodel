import math
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
