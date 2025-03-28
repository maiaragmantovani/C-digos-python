from datetime import datetime

# Exibir a hora atual
hora_atual = datetime.now().strftime("%H:%M:%S")
print(f"A hora atual é: {hora_atual}")

# Exemplo de cálculo de diferença entre horas
hora_inicial = datetime.strptime("14:30:00", "%H:%M:%S")
hora_final = datetime.strptime("17:45:00", "%H:%M:%S")

# Calcular a diferença entre as horas
diferenca = hora_final - hora_inicial
print(f"A diferença entre as duas horas é: {diferenca}")
