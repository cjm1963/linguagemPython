num_i = input("Digite um numero inicial: ")
num_f = input("Digite um nomero final: ")

num_i = int(num_i)
num_f = int(num_f)
            
# variavel para contar os numeros pares
qtd = 0
while( num_i <= num_f):
    if num_i % 2 == 0:
        print(num_i)
        qtd = qtd + 1
    num_i = num_i + 1

print("---------------------------")
print("A quantidade de pares é "+str(qtd))