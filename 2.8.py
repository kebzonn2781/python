import time
sek = int(input('Podaj liczbe sekund: '))
if sek < 10:
    time.sleep (sek)
if sek >= 10:
    print('Nie bede tyle czekal.')