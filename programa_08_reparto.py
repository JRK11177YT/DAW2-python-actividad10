# Alumno: Jorge Ruiz
# Programa 08 - Reparto de entradas
# Reparte un número de entradas entre varios grupos de forma equitativa,
# demostrando el uso de la división entera y el módulo.

total_entradas_texto = input("Introduce el número total de entradas disponibles: ")
total_entradas = int(total_entradas_texto)  # int porque las entradas son unidades enteras

numero_grupos_texto = input("Introduce el número de grupos: ")
numero_grupos = int(numero_grupos_texto)

entradas_por_grupo = total_entradas // numero_grupos  # División entera: entradas completas para cada grupo
entradas_sobrantes = total_entradas % numero_grupos  # Módulo: entradas que no se pueden repartir por igual

print("----- REPARTO DE ENTRADAS -----")
print(f"Entradas completas por grupo: {entradas_por_grupo}")
print(f"Entradas sin repartir: {entradas_sobrantes}")
