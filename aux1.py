def soma_lista(lista):
    # Variável auxiliar para armazenar a soma
    aux = 0
    
    # Percorrer a lista e somar os valores
    for num in lista:
        aux += num  # Atualiza a soma
    
    return aux

# Exemplo de uso
lista = [1, 2, 3, 4, 5]

# Chama a função para somar os elementos
resultado = soma_lista(lista)

# Exibe o resultado
print(f"A soma dos elementos da lista é: {resultado}")
