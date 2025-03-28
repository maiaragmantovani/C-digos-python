# Função para calcular porcentagem
def calcular_porcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

# Solicitar ao usuário o valor e a porcentagem
valor = float(input("Digite o valor: "))
porcentagem = float(input("Digite a porcentagem: "))

# Calcular e exibir o resultado
resultado = calcular_porcentagem(valor, porcentagem)
print(f"{porcentagem}% de {valor} é: {resultado}")
