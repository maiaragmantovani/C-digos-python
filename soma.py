# Função para somar dois números
def somar(a, b):
    return a + b

# Solicitar ao usuário os números para somar
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamar a função e exibir o resultado
resultado = somar(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é: {resultado}")
