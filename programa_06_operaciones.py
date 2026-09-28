# Alumno: Jorge Ruiz
# Programa 06 - Operaciones con dos números
# Solicita dos números y muestra el resultado de varias operaciones aritméticas.

primer_numero_texto = input("Introduce el primer número: ")
primer_numero = float(primer_numero_texto)  # float para admitir también números con decimales

segundo_numero_texto = input("Introduce el segundo número: ")
segundo_numero = float(segundo_numero_texto)

# Operadores aritméticos aplicados a los dos números
suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division_real = primer_numero / segundo_numero  # / siempre devuelve un resultado con decimales
division_entera = primer_numero // segundo_numero  # // descarta la parte decimal del resultado
resto = primer_numero % segundo_numero  # % devuelve el resto de la división entera
potencia = primer_numero ** segundo_numero  # ** eleva el primer número al segundo número

print("----- OPERACIONES CON DOS NÚMEROS -----")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División real: {division_real}")
print(f"División entera: {division_entera}")
print(f"Resto: {resto}")
print(f"Potencia: {potencia}")
