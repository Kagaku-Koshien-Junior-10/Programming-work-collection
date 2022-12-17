from math import gcd
def lcm(p,q):
    return (p * q) // gcd(p,q)
def key(p, q ,e):
  n = p * q
  cita = lcm(p - 1, q - 1)

  for i in range(2, cita):
    if (e * i) % cita == 1:
      d = i
      break
  return d
p = 2357
q = 4159
e = 3299
n = p * q
d = key(p,q,e)
m = 9
print("↓ 素数p 素数q n=pq 素数e 平文m")
print(p,q,n,e,m)
c = (m**e)%n
print("↓暗号C")
print(c)
m_new = (c**d)%n
print("↓復号化された数M")
print(m_new)
