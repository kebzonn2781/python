a1 = float(input('Podaj zmienna a1: '))
a2 = float(input('Podaj zmienna a2: '))
a3 = float(input('Podaj zmienna a3: '))
a4 = float(input('Podaj zmienna a4: '))
a5 = float(input('Podaj zmienna a5: '))

if a5 == 0:
    print('Nie mozna wykonac dzielenia przez 0.')
    exit()

wynik = (((a1+a2)*a3)-a4)/a5

print(f'((({a1}+{a2})*{a3})-{a4})/{a5} = {wynik}')
print(f'Wynik wynosi: {wynik}')