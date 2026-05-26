login = 'papaj'
haslo = '2137'
plogin = None
phaslo = None
lprob = 0
lprob2 = 0
sk = '1 000 000 dolarow kurcze przelew'

print('WITAJ W BANKOMACIE PKO BP!')
while plogin != login:
    plogin = input()
    lprob +=1
    if lprob == 3:
        print('Konto zostalo zablokowane cymbale, zwyzywaj caly swiat i wybombiaj stad.')
        quit()

if plogin == login:
    while phaslo != haslo:
        phaslo = input('Podaj haslo: ')      

        if phaslo == haslo:
            print()
            print('Poprawnie zalogowano!')
            print(f'Stan konta wynosi: {sk}')
            quit()
        else:
            lprob2 += 1
            print('Niepoprawne haslo.')

            if lprob2 == 3:
                print('Zapomniales hasla i zalatwiles sobie zablokowane konto, brawo!')
                quit()