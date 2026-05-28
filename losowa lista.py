import random

n=5
for i in range(100):
    liczby.append(random.randint(0,1000))
    
#a)
suma=0
for i in liczby:
    suma+=i
print(suma)

#b)
minimalna=liczby[0]
for i in range(1,n):
    if liczby[i]<minimalna:
        minimalna=liczby[i]
print(minimalna)

#c)
posortowane=liczby.sorted()
print(posortowane)