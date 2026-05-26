liczba=None
lista=[]
suma=0
dodatnie5=0
while(True):
    liczba=int(input('Podaj liczbe do wczytania. Liczba musi byc w zakresie od -99 do 99: '))
    if len(lista)==0 and liczba==100:
        print('Nie moze byc 0 elementow w liscie.')
        continue
    if liczba==100:
        break
    if liczba<(-99) or liczba>99:
        print('Liczba spoza zakresu!')
        continue
    lista.append(liczba)
for i in lista:
    suma+=i
    if i > 0 and i%5==0:
        dodatnie5+=1
print(f'Suma elementow wynosi {suma}, {sum(lista)}')
print(f'Liczba liczb dodatnich jest: {dodatnie5}.')
print(f'Srednia elementow wynosi: {round(suma/len)}')