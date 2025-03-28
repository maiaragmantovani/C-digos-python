from prettytable import PrettyTable

# Criar uma tabela
tabela = PrettyTable()

# Definir os nomes das colunas
tabela.field_names = ["ID", "Nome", "Idade", "Cidade"]

# Adicionar linhas à tabela
tabela.add_row([1, "João", 25, "São Paulo"])
tabela.add_row([2, "Maria", 30, "Rio de Janeiro"])
tabela.add_row([3, "Carlos", 22, "Belo Horizonte"])
tabela.add_row([4, "Ana", 28, "Curitiba"])

# Exibir a tabela
print(tabela)
