def exibir_tabuada():
    # Solicita ao usuário para digitar um número
    numero = int(input("Digite um número para ver sua tabuada: "))

    # Exibe a tabuada do número de 1 a 10
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Chama a função para exibir a tabuada
exibir_tabuada()
