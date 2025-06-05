notas = []

for i in range(3):
    nota = float(input(f"Ingresá la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"El promedio es: {promedio}")
