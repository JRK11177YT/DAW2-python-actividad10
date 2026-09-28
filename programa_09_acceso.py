# Alumno: Jorge Ruiz
# Programa 09 - Comparador lógico de acceso
# Calcula distintos resultados booleanos relacionados con el acceso de una persona.
# Todavía no se usan estructuras condicionales (if), solo operadores relacionales y lógicos.

edad_texto = input("Introduce la edad del usuario: ")
edad = int(edad_texto)  # int porque la edad es un número entero

respuesta_autorizacion = input("¿Tiene autorización? (si/no): ")
respuesta_identificacion = input("¿Dispone de identificación? (si/no): ")

# Convertimos las respuestas de texto a valores booleanos mediante una comparación (==)
# .lower() evita problemas si el usuario escribe "Si", "SI", etc.
tiene_autorizacion = respuesta_autorizacion.lower() == "si"
tiene_identificacion = respuesta_identificacion.lower() == "si"

# >= es un operador relacional que también genera un valor booleano (True o False)
es_mayor_de_edad = edad >= 18

# and, or y not son los operadores lógicos que combinan valores booleanos entre sí
acceso_completo = es_mayor_de_edad and tiene_autorizacion and tiene_identificacion  # Deben cumplirse las tres
acceso_supervisado = tiene_autorizacion or es_mayor_de_edad  # Basta con que se cumpla una de las dos
acceso_bloqueado = not tiene_identificacion  # Invierte el valor booleano de tiene_identificacion

# El programa solo muestra los resultados booleanos, sin usar todavía ninguna estructura if
print("----- RESULTADOS DE ACCESO -----")
print(f"¿Es mayor de edad?: {es_mayor_de_edad}")
print(f"¿Acceso completo?: {acceso_completo}")
print(f"¿Acceso supervisado?: {acceso_supervisado}")
print(f"¿Acceso bloqueado?: {acceso_bloqueado}")
