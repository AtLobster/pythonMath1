import numpy as np

a = 2.493
b = 0.911
print(np.degrees(a))
print(np.degrees(b))

c = 137.7
d = 62.3
print(f'\n{np.radians(c)} rad')
print(f'{np.radians(d)} rad\n')

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
    print(f"{np.array(i):<3} deg  I {np.radians(i): .3f} rad")

lävistäjä = 6.4
suhde_leveys = 3
suhde_korkeus = 2

kerroin = lävistäjä / np.sqrt(suhde_leveys ** 2 + suhde_korkeus ** 2)

leveys = suhde_leveys * kerroin
korkeus = suhde_korkeus * kerroin

print(f'\nSuorakulmion sivut ovat {leveys: .1f}m, {korkeus: .1f}m')













