samogloska = ['a','e','o','u','y']
spolgloska = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
cyfra = ['1','2','3','4','5','6','7','8','9','0']
znak = input('Podaj znak: ')
if znak in spolgloska:
    print('Jest to spolgloska.')
elif znak in samogloska:
    print('Jest to samogloska.')
elif znak in cyfra:
    print('Jest to cyfra.')
else:
    print('Niepoprawne dane.')