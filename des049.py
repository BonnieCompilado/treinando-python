tab = int(input('Digite um número para ver sua tabuada: '))
print('TABUADA DO {}' .format(tab))

for c in range(1, 11):
    print('{} x {} = {}' .format(tab, c, tab * c))