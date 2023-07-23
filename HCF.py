a,b=map(int,input().split())
c=[]
d=[]
for i in range(a,0,-1):
  if a%i==0:
    c.append(i)
for i in range(b,0,-1):
  if b%i==0:
    d.append(i)
for i in range(0,len(c)):
  for j in range(0,len(d)):
    if c[i]==d[j]:
      print(c[i])
  break
