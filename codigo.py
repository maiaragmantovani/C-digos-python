
notas = []
for i in range(1, 11):
    nota = int(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)

notas_crescentes = sorted(notas)
print("\nNotas em ordem crescente:")
for nota in notas_crescentes:
    print(nota)

notas_decrescentes = sorted(notas, reverse=True)
print("\nNotas em ordem decrescente:")
for nota in notas_decrescentes:
    print(nota)
