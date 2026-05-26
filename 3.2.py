import random
max = 0
liczba = 100
while(True):
    liczba = int(input('Podaj liczbe: '))
    if liczba < 5:
        break
    if liczba > max:
        max = liczba
losowa = random.randint(-100, 100)
for i in range(max):
    print(random.randint(-100, 100),end=' ')