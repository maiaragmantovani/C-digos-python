def verificar_numero(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

# Exemplo de uso
numero = int(input("Digite um número: "))
verificar_numero(numero)
