from random import randint

print('===== JOKENPÔ =====')

jogador = int(input('Escolha uma das opções:\n'
                    '1. Pedra\n'
                    '2. Papel\n'
                    '3. Tesoura\n'
                    ''))

computador = randint(1, 3)

if jogador == 1:
    if computador == 1:
        print('Empate! Ambos escolheram Pedra.')
    elif computador == 2:
        print('Você perdeu! Computador escolheu Papel.')
    else:
        print('Você ganhou! Computador escolheu Tesoura.')
elif jogador == 2:
    if computador == 1:
        print('Você ganhou! Computador escolheu Pedra.')
    elif computador == 2:
        print('Empate! Ambos escolheram Papel.')
    else:
        print('Você perdeu! Computador escolheu Tesoura.')
elif jogador == 3:
    if computador == 1:
        print('Você perdeu! Computador escolheu Pedra.')
    elif computador == 2:
        print('Você ganhou! Computador escolheu Papel.')
    else:
        print('Empate! Ambos escolheram Tesoura.')
print('Fim de jogo!')