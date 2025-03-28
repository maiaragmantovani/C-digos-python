def inserir_no_meio(lista, item):
    # Calcular o índice do meio
    meio = len(lista) // 2
    
    # Inserir o item no meio
    lista.insert(meio, item)
    return lista

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
item = 99

# Inserir o item no meio
nova_lista = inserir_no_meio(lista, item)

# Exibir a nova lista
print(nova_lista)
