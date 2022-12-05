import matplotlib.pyplot as plt
import numpy as np
global kansuu
global tenn0
global tenn0x
global tenn0y
global tenn1
global tenn1x
global tenn1y
global tenn2
global tenn2x
global tenn2y

np.set_printoptions(precision=2)

tenn0x=np.around(np.random.rand(), decimals=2)
tenn0y=np.around(np.random.rand(), decimals=2)
tenn1x=np.around(np.random.rand(), decimals=2)
tenn1y=np.around(np.random.rand(), decimals=2)
tenn2x=np.around(np.random.rand(), decimals=2)
tenn2y=np.around(np.random.rand(), decimals=2)

print("aaa")
plt.figure(figsize=(13,13))
tenn0=complex(tenn0x,tenn0y)
tenn1=complex(tenn1x,tenn1y)
tenn2=complex(tenn2x,tenn2y)
print("iii")
plt.plot(tenn0x,tenn0y,"o",picker=15)
plt.plot(tenn1x,tenn1y,"o",picker=15)
plt.plot(tenn2y,tenn2y,"o",picker=15)
print("uuu")

plt.xlim(0, 1)
plt.ylim(0, 1)
kannsuu2=-1*(tenn0+tenn1+tenn2)
kannsuu1=tenn0*tenn1+tenn1*tenn2+tenn2*tenn0
kannsuu0=-1*tenn0*tenn1*tenn2
def kannsuu(z):
  return z**3+kannsuu2*z**2+kannsuu1*z+kannsuu0
def bibunn(z):
  return 3*z**2+2*kannsuu2*z+kannsuu1
z=[]
motox=[]
motoy=[]
b=0
c=0
while b<1:
  while c<1:
    z.append(complex(b,c))
    motox.append(b)
    motoy.append(c)
    c=c+0.0002
  c=0
  b=b+0.0002
print(len(z))
for n in range(20):
  for i in range(25010001):
    z[i]=z[i]-kannsuu(z[i])/bibunn(z[i])
colorlist=[]
zitubu1=[]
kyobu1=[]
zitubu2=[]
kyobu2=[]
for n in range(25010001):
  d=tenn0-z[n]
  e=tenn1-z[n]
  f=tenn2-z[n]
  if abs(d.real)+abs(d.imag) < 0.01:
    colorlist.append("purple")
  elif abs(e.real)+abs(e.imag) < 0.01:
    colorlist.append("red")
  elif abs(f.real)+abs(f.imag) < 0.01:
    colorlist.append("yellow")
  else:
    colorlist.append("black")
  zitubu1.append(motox[n])
  kyobu1.append(motoy[n])
  zitubu2.append(z[n].real)
  kyobu2.append(z[n].imag)
print("eee")
plt.scatter(zitubu1,kyobu1,color=colorlist,s=0.00015)
print("オレンジ→赤、青→紫、緑→黄色")
plt.savefig("ニュートンフラクタル", format="png", dpi=700)
