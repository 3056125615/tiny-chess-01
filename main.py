import json,os,urllib.request as R
V=(0,100,320,330,500,900,0);M=10**6;NODES=50000
T="""########%%'+''+1++/5557;AAAA#####%''%)+-'-/3'-15'-15'-13%)--#%'''''''+++'+//'+/3'+/3'+//'+++''''%%%'%%%%%%%%%%%%%%%%''''////####%%%%%)))%)--%)-1%)-1%)--%)))%%%%7A-##')+##%%####################"""
T=[ord(c)-35 for c in T]
C={0:2,4:3,7:1,112:8,116:12,119:4};L=(33,31,18,14,-14,-18,-31,-33);J=(1,-1,16,-16,17,15,-17,-15)
N=0;H={};SEEN={}
def P(f):
 a=f.split();b=[0]*128;y=7;x=0
 for c in a[0]:
  if c=='/':y-=1;x=0
  elif c>'9':
   v=".PNBRQKpnbrqk".index(c);b[y*16+x]=v if v<7 else 6-v;x+=1
  else:x+=int(c)
 r=sum(1<<i for i,c in enumerate("KQkq") if c in a[2])
 e=-1 if a[3]=='-' else(int(a[3][1])-1)*16+ord(a[3][0])-97
 return b,1 if a[1]=='w' else -1,r,e
def A(b,q,c):
 for t in(q-c*15,q-c*17):
  if t&136<1 and b[t]==c:return 1
 for o in L:
  t=q+o
  if t&136<1 and b[t]*c==2:return 1
 for o in J:
  t=q+o
  if t&136<1 and b[t]*c==6:return 1
 for o,p in((J[4:],(3,5)),(J[:4],(4,5))):
  for d in o:
   t=q+d
   while t&136<1:
    if(v:=b[t]):
     if v*c>0 and abs(v) in p:return 1
     break
    t+=d
def K(s,m):
 b,c,r,e=s;b=b[:];f=m&127;t=m>>7&127;z=m>>14;p=b[f];b[f]=0;v=b[t];b[t]=z*c or p;a=abs(p);d=t-f
 if a==1:
  if t==e and not v:b[t-16*c]=0
  e=f+16*c if abs(d)==32 else -1
 else:e=-1
 if a==6:
  if abs(d)==2:q=f+3 if d>0 else f-4;u=f+d//2;b[u]=b[q];b[q]=0
 r&=~(C.get(f,0)|C.get(t,0))
 return b,-c,r,e
def _(m,f,t):
 if t>>4 in(0,7):
  for z in 5,4,3,2:m+=[f|t<<7|z<<14]
 else:m+=[f|t<<7]
def G(s):
 b,c,r,e=s;m=[]
 for f,p in enumerate(b):
  if p*c>0:
   a=abs(p)
   if a==1:
    t=f+16*c
    if t&136<1 and not b[t]:
     _(m,f,t)
     if f>>4==1+5*(c<0) and not b[t+16*c]:_(m,f,t+16*c)
    for d in -1,1:
     u=t+d
     if u&136<1:
      v=b[u]
      if v*c<0:_(m,f,u)
      elif u==e:m+=[f|u<<7]
   elif a in(2,6):
    for o in(L if a==2 else J):
     t=f+o
     if t&136<1 and b[t]*c<1:m+=[f|t<<7]
    if a==6 and not A(b,f,-c):
     for d in 1,-1:
      if r>>(c<0)*2&1+(d<0) and not any(b[f+d*i]for i in(1,2,3-(d>0))) and not A(b,f+d,-c):m+=[f|(f+2*d)<<7]
   else:
    o=(17,15,-17,-15)*(a!=4)
    for d in o+(1,-1,16,-16)*(a!=3):
     t=f+d
     while t&136<1:
      v=b[t]
      if v*c>0:break
      m+=[f|t<<7]
      if v:break
      t+=d
 return[x for x in m if not A((n:=K(s,x))[0],n[0].index(6*c),-c)]
def E(s):
 b,c=s[:2];z=0
 for q,p in enumerate(b):
  if p:
   a=abs(p);r=q>>4;f=q&7
   if p<0:r=7-r
   if f>3:f=7-f
   z+=(V[a]+T[(a-1)*32+r*4+f])*(1-2*(p<0))
 return z*c
def Q(s,a,b):
 global N
 if N>=NODES:return 0
 N+=1
 w,c,r,e=s;v=E(s)
 if v>=b:return v
 if v>a:a=v
 m=[x for x in G(s) if w[t:=x>>7&127] or abs(w[x&127])==1 and t==e]
 m.sort(key=lambda x:-abs(w[x>>7&127]))
 for x in m:
  v=-Q(K(s,x),-b,-a)
  if v>a:
   a=v
   if a>=b:break
 return a
def S(s,d,a,b):
 global N
 if N>=NODES:return 0
 N+=1
 if d<1:return Q(s,a,b)
 w,c,r,e=s;q=tuple(w),c,r,e
 t=H.get(q);u=t[2] if t else 0
 if t and t[0]>=d and t[1]>=b:return t[1]
 m=G(s)
 if not m:return -M if A(w,w.index(6*c),-c) else 0
 m.sort(key=lambda x:(x!=u,-abs(w[x>>7&127]),abs(w[x&127])))
 v=-M;y=0
 for x in m:
  v0=-S(K(s,x),d-1,-b,-a)
  if v0>v:v=v0;y=x
  if v0>a:
   a=v0
   if a>=b:break
 if v>=b:H[q]=(d,v,y)
 return v
def I(u):
 f=ord(u[0])-113+16*int(u[1]);t=ord(u[2])-113+16*int(u[3]);z="nbrq".index(u[4])+2 if u[4:] else 0
 return f|t<<7|z<<14
def choose(f,l):
 global N,H
 s=P(f);N=0;H={};m=list(map(I,l));O=dict(zip(m,l));w=m[0]
 k=str(s[0]),s[1];SEEN[k]=SEEN.get(k,0)+1
 for d in range(1,99):
  a=v=-M;z=m[0]
  for x in m:
   n=K(s,x);u=-S(n,d-1,-M,-a)
   if u>-101 and SEEN.get((str(n[0]),n[1])):u-=40
   if u>v:v=u;z=x
   if u>a:a=u
  if N>=NODES:break
  w=z
  if v>M-100:break
 return O.get(w,l[0])
def post(p,b):
 return json.load(R.urlopen(R.Request(os.environ["MAKEFUN_ENV_URL"]+p,json.dumps(b).encode(),{"content-type":"application/json"})))
if __name__=="__main__":
 i=None
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  if g["game"]!=i:SEEN={};i=g["game"]
  while g["status"]=="your_move":g=post("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
