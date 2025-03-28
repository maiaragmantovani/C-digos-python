while True:
    # Solicitar ao usuário para digitar um número
    numero = input("Digite um número (ou 'sair' para encerrar): ")

    # Verificar se o usuário deseja sair
    if numero.lower() == 'sair':
        print("Programa encerrado.")
        break  # Interrompe o loop

    # Verificar se a entrada é um número
    try:
        numero = int(numero)
        print(f"Você digitou o número: {numero}")
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")
