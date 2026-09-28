# Alumno: Jorge Ruiz
# Programa 03 - Conversor de temperatura
# Convierte una temperatura en grados Celsius a Fahrenheit y a Kelvin.

temperatura_celsius_texto = input("Introduce la temperatura en grados Celsius: ")
temperatura_celsius = float(temperatura_celsius_texto)  # float porque la temperatura puede tener decimales

# Fórmulas de conversión de temperatura.
# Por precedencia de operadores, * y / se calculan antes que + y -,
# por eso no hacen falta paréntesis en temperatura_celsius * 9 / 5 + 32
temperatura_fahrenheit = temperatura_celsius * 9 / 5 + 32
temperatura_kelvin = temperatura_celsius + 273.15  # Se suma una constante fija a los grados Celsius

# Mostramos los resultados con dos decimales
print("----- CONVERSOR DE TEMPERATURA -----")
print(f"Temperatura en Celsius: {temperatura_celsius:.2f} °C")
print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {temperatura_kelvin:.2f} K")
