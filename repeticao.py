# Estrutura de repetição com FOR
print("Contagem de 1 a 10 usando for:")
for i in range(1, 11):
    print(i, end=' ')
print("\n")

# Estrutura de repetição com WHILE
print("Contagem regressiva de 10 a 1 usando while:")
contador = 10
while contador > 0:
    print(contador, end=' ')
    contador -= 1
print("\n")

# Loop com break e continue
print("Exemplo de loop com break e continue:")
for numero in range(1, 11):
    if numero == 5:
        continue  # Pula o número 5
    if numero == 8:
        break  # Para o loop no número 8
    print(numero, end=' ')
print("\n")