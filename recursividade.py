# Função recursiva para calcular o fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicitar ao usuário o número para calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

# Chamar a função recursiva e exibir o resultado
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
