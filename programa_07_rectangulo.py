# Alumno: Jorge Ruiz
# Programa 07 - Datos de un rectángulo
# Calcula el área, el perímetro y la diagonal de un rectángulo.

base_texto = input("Introduce la base del rectángulo: ")
base = float(base_texto)  # float porque las medidas pueden llevar decimales

altura_texto = input("Introduce la altura del rectángulo: ")
altura = float(altura_texto)

# Cálculos geométricos del rectángulo
area = base * altura
perimetro = 2 * (base + altura)  # Los paréntesis fuerzan a sumar primero y multiplicar por 2 después
diagonal = (base ** 2 + altura ** 2) ** 0.5  # Elevar a 0.5 equivale a calcular la raíz cuadrada

print("----- DATOS DEL RECTÁNGULO -----")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
print(f"Diagonal: {diagonal:.2f}")
