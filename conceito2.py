nota1 = input("digite a primeira nota:")
nota2 = input("digite a segunda nota:")
nota3 = input("digite a terceirta nota:")
nota4 = input("digite a quarta nota:")

# vamos converter as variaveis de notas 
# para tipo float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

# se a nota media do aluno for maior ou igual a 7, ->Aprovado
# se a nota media do aluno for menor ou igual a 4, ->Reprovado
# senão, ->Recuperação
if media >= 7:
    print("Sua nota media é:"+ str(media) + "Aprovado")
elif media <= 4:
    print("Sua nota media é:"+ str(media) + "Reprovado")
else:
    print("Sua nota media é:"+ str(media) + "Recuperação")

