lista = []

for liczba in range (3):
    liczba = int(input('Podaj nieujemna liczbe: '))
    if liczba <= -1:
        print('Miala byc liczba nieujemna.')
        continue
    lista.append(liczba)
    
print(lista)