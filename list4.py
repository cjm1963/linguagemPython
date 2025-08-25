# obter o menor valor presente no vetor e exibir em tela

num = [34,6,11,19,52,71,86,90]
menor = num[0]
for x in num:
    if x < menor:
        menor = x
        print(x)
