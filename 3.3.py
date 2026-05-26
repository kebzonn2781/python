import random

zakres1=[]
zakres2=[]
liczba=None
sumaparzystedod=0
iloparzysteujem=1

while liczba!=0:
    liczba=random.randint(-150,150)
    zakres1.append(liczba)

ile=len(zakres1)

while ile!=0:
    liczba=random.randint(-10, 10)
    zakres2.append(liczba)
    ile-=1

for i in zakres1:
    if i>0 and i%2==0:
        sumaparzystedod+=i
for i in zakres2:
    if i<0 and i%2==0:
        iloparzysteujem*=i

print()
print(f'Zakres 1 to: {zakres1}')
print()
print(f'Zakres 2 to: {zakres2}')
print()
print(f'Stosunek liczb parzystych dodatnich do liczb parzystych ujemnych wynosi: {sumaparzystedod/iloparzysteujem}')