# Estrutura de decisão IF, ELIF, ELSE
idade = int(input("Digite sua idade: "))

# Decisão baseada na idade
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Verificando se o número é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Verificando a nota do aluno
nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Em recuperação.")
else:
    print("Reprovado.")
