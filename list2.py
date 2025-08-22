# obter os numeros pares da lista e soma-los

num = [34,6,11,19,52,71,86,90]
resultado = 0

for x in num:
    if x % 2 == 0:
        resultado = resultado + x
        print(x)

print("------------------------")
print("o resultado da soma é: "+str(resultado))
