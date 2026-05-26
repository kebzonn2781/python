def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def dzielenie():
    x=int(input('Podaj liczbe pierwsza: '))
    y=int(input('Podaj liczbe druga: '))
    if y == 0:
        print('Nie mozna podzielic przez 0.')
    else:
        print(f'Dzielenie {x} przez {y} wynosi: {x/y}')

def mnozenie(a,b):
    return a*b

while True:
    wybor=int(input('Wybierz opcje: 1-dodawanie, 2-odejmowanie, 3-dzielenie, 4-mnozenie, 0-koniec dzialania: '))
    if wybor == 0:
        print('nara')
        break
    if wybor < 1 or wybor > 4:
        print('Nie ma takiego numeru!')
        continue
    a=int(input('Podaj liczbe pierwsza: '))
    b=int(input('Podaj liczbe druga: '))
    if wybor == 1:
        print(f'Wynik dodawania {a} + {b} to: {dodawanie(a,b)}.')
    elif wybor == 2:
        print(f'Wynik odejmowania {a} - {b} wynosi: {odejmowanie(a,b)}.')
    elif wybor == 3:
        dzielenie()
    elif wybor == 4:
        print(f'{a} razy {b} wynosi {mnozenie(a,b)}')
    else:
        print('Zly znak!')