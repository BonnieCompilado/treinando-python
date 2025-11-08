print('SOMA DE TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE TRÊS ENTRE 1 E 500')
soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('A soma de todos os números ímpares múltiplos de três entre 1 e 500 é de {}' .format(soma))