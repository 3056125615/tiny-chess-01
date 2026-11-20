import json,os,urllib.request as U
V=(100,320,330,500,900,0);M=1<<20;NODES=50000
T=b"########%%'+''+1++/5557;AAAA#####%''%)+-'-/3'-15'-15'-13%)--#%'''''''+++'+//'+/3'+/3'+//'+++''''%%%'%%%%%%%%%%%%%%%%''''////####%%%%%)))%)--%)-1%)-1%)--%)))%%%%7A-##')+##%%#####################-2--7A<2APK2FUP2FUP2APK-7A<#-2-"
C={0:2,4:3,7:1,112:8,116:12,119:4};L=(33,31,18,14,-14,-18,-31,-33);J=(1,-1,16,-16,17,15,-17,-15);R=J[4:]+J[:4];B=((L,2),(J,6));D=((R[:4],(3,5)),(R[4:],(4,5)))
N=0;H={};SEEN={};CQ=0
def P(f):
 a=f.split();b=[0]*128;q=112
 for c in a[0]:
  if c=='/':q-=24
  elif c>'9':v=".PNBRQKpnbrqk".index(c);b[q]=(v,6-v)[v>6];q+=1
  else:q+=int(c)
 return b,2*(a[1]>'b')-1,sum(1<<i for i,c in enumerate("KQkq")if c in a[2]),16*int(a[3][1])+ord(a[3][0])-113 if a[3]>'-'else-1
def A(b,q,c,L=L,J=J,B=B,D=D):
 for t in q-c*15,q-c*17:
  if t&136<1 and b[t]==c:return 1
 for o,p in B:
  for d in o:
   t=q+d
   if t&136<1 and b[t]*c==p:return 1
 for o,p in D:
  for d in o:
   t=q+d
   while t&136<1:
    if(v:=b[t]):
     if v*c>0 and abs(v)in p:return 1
     break
    t+=d
def K(s,m):
 b,c,r,e=s;b=b*1;f=m&127;t=m>>7&127;z=m>>14;p=b[f];b[f]=0;v=b[t];b[t]=z*c or p;a=abs(p);d=t-f
 if a<2:
  if t==e and not v:b[t-16*c]=0
  e=f+16*c if d%32<1 else-1
 else:e=-1
 if a>5 and abs(d)==2:q=f+3-(d<0)*7;u=f+d//2;b[u]=b[q];b[q]=0
 r&=~C.get(f,0)&~C.get(t,0)
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
   if a<2:
    t=f+16*c
    if t&136<1 and not b[t]:
     _(m,f,t)
     if f>>4==1+5*(c<0)and not b[t+16*c]:_(m,f,t+16*c)
    for u in t-1,t+1:
     if u&136<1 and b[u]*c<0:_(m,f,u)
     elif u==e:m+=[f|u<<7]
   elif a%4==2:
    for o in(L,J)[a>2]:
     t=f+o
     if t&136<1 and b[t]*c<1:m+=[f|t<<7]
    if a>5 and not A(b,f,-c):
     for d in 1,-1:
      if r>>(c<0)*2&1+(d<0)and not any(b[f+d*i]for i in(1,2,3-(d>0)))and not A(b,f+d,-c):m+=[f|(f+2*d)<<7]
   else:
    for d in(R[:4],R[4:],R)[a-3]:
     t=f+d
     while t&136<1:
      v=b[t]
      if v*c>0:break
      m+=[f|t<<7]
      if v:break
      t+=d
 if CQ:m=[x for x in m if b[x>>7&127]or abs(b[x&127])==1 and x>>7&127==e]
 k=b.index(6*c)
 return[x for x in m if not A((n:=K(s,x))[0],x>>7&127 if b[x&127]==6*c else k,-c)]
def E(s):
 b,c,*_=s;z=0;e=5 not in b and-5 not in b or b.count(0)>112
 for q,p in enumerate(b):
  if p:
   a=abs(p);j=q&7;r=(q>>4)^7*(p<0);f=j
   if f>3:f=7-f
   z+=(V[a-1]+T[(a-1)*32+r*4+f+32*e*(a>5)]-35)*(1-2*(p<0))
   if a<2 and r>2 and not any(-p in b[u::16]for u in(j-1,j,j+1)if 0<=u<8):z+=8*r*(1-2*(p<0))
 return z*c
def S(s,d,a,b):
 global N
 if N>=NODES:return 0
 N+=1
 w,c,r,e=s
 if d<1:
  if d==0:
   if N>=NODES:return 0
   N+=1
  v=E(s)
  if v>=b:return v
  a=max(a,v)
  global CQ
  CQ=1;m=G(s);CQ=0
  m.sort(key=lambda x:-abs(w[x>>7&127]))
  for x in m:
   v=-S(K(s,x),-1,-b,-a)
   if v>a:
    a=v
    if a>=b:break
  return a
 q=tuple(w),c,r,e
 t=H.get(q)or(0,0,0);u=t[2]
 if t[0]>=d and t[1]>=b:return t[1]
 m=G(s)
 if not m:return-M if A(w,w.index(6*c),-c) else 0
 m.sort(key=lambda x:(x!=u,-abs(w[x>>7&127]),abs(w[x&127])))
 v=y=-M
 for x in m:
  v0=-S(K(s,x),d-1,-b,-a)
  if v0>v:v=v0;y=x
  if v0>a:
   a=v0
   if a>=b:break
 if v>=b:H[q]=d,v,y
 return v
I=lambda u:ord(u[0])-113+16*int(u[1])|(ord(u[2])-113+16*int(u[3]))<<7|"  nbrq".find(u[4:])<<14
def choose(f,l):
 global N,H
 s=P(f);N=0;H={};w=l[0]
 k=str(s[0]),s[1];SEEN[k]=SEEN.get(k,0)+1
 for d in range(1,99):
  v=-M;z=l[0]
  for x in l:
   n=K(s,I(x));u=-S(n,d-1,-M,-v)
   if u>-101 and SEEN.get((str(n[0]),n[1])):u-=40
   if u>v:v=u;z=x
  if N>=NODES:break
  w=z
  if v>M-100:break
 return w
post=lambda p,b:json.load(U.urlopen(U.Request(os.environ["MAKEFUN_ENV_URL"]+p,json.dumps(b).encode(),{"content-type":"application/json"})))
if __name__=="__main__":
 i=None
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  if g["game"]!=i:SEEN={};i=g["game"]
  while g["status"]=="your_move":g=post("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
