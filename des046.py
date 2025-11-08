from time import sleep

print('Iniciando a contagem regressiva...')
sleep(2)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!')