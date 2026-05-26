lista = []
parzyste = 0
nieparzyste = 0

for i in range (5):
    liczba = int(input('Podaj liczbe: '))
    lista.append(liczba)

print()
print(lista)
print()

for liczba in lista:
    if liczba % 2==0:
        print(f'Liczba {liczba} jest parzysta')
        parzyste+=1
    else:
        print(f'Liczba {liczba} jest nieparzysta')
        nieparzyste+=1

print()
print(f'Parzystych liczb jest {parzyste}')
print(f'Nieparzystych liczb jest {nieparzyste}')
print()