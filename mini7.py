lista = []

while (True):
    znaki = input('Podaj znaki: ')[0]
    lista.append(znaki)
    if 'x' in znaki:
        break
ile = len(lista)

print()
print(lista)
print()
print(f'Liczba podanych znakow wynosi: {ile}')
print()