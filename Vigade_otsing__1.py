"""import math


print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => '))
S = a**2
print("Ruudu pindala", S)
P = 4 * a
print("Ruudu ümbermõõt", P)
di = a * math.sqrt(2)
print("Ruudu diagonaal", round(di, 2))
print()


print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b * c
print("Ristküliku pindala", S)
P = 2 * (b + c)
print("Ristküliku ümbermõõt", P)
di = math.sqrt(b**2 + c**2)
print("Ristküliku diagonaal", round(di, 2))
print()


print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiuse pikkus => "))
d = 2 * r
print("Ringi läbimõõt", d)
S = math.pi * r**2
print("Ringi pindala", round(S, 2))
C = 2 * math.pi * r
print("Ringjoone pikkus", round(C, 2))
"""

arv=int(input("Sisesta arv: "))
if arv==13: 
    arv=77
print(arv)

if arv>0:
    print("Positivne arv")
elif arv<0:
    print("Negativne arv")
else:
    print("0")


hinne=int(input("Mis hinne sa täna sai?")) #"A" "MA" "X" "5" "4" "3"
if hinne==5: or hinne==
    print("super!")
elif hinne==4:
    print("Hea hinne!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2:
    print("Halb!")
else:
    print("Ma ei tea, mis hinne see on!")


from random import *
a=randint(-1000,1000)
print(a)
if a*3==0:
