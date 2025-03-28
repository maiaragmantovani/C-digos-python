
notas = []

# Coletando as notas dos alunos
total_alunos = 10
for i in range(total_alunos):
    nota = int(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

# Exibindo as notas em ordem crescente
notas.sort()
print("\nNotas em ordem crescente:", notas)

# Exibindo as notas em ordem decrescente
notas.sort(reverse=True)
print("Notas em ordem decrescente:", notas)

# Contando quantos alunos tiraram nota 100
quantidade_100 = notas.count(100)
print(f"\nQuantidade de alunos que tiraram 100: {quantidade_100}")

