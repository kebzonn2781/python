liczba = int(input('Podaj liczbe: '))
if liczba % 15==0:
    print(f'Liczba {liczba} jest podzielna przez 3 i 5')
elif liczba % 3==0:
    print(f'Liczba {liczba} jest podzielna przez 3')
elif liczba % 5==0:
    print(f'Liczba {liczba} jest podzielna przez 5')
else:
    print(f'Liczba {liczba} nie jest podzielna przez 3 i 5')