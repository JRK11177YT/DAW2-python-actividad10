# Alumno: Jorge Ruiz
# Programa 01 - Ficha personal
# Este programa solicita datos personales al usuario y muestra una ficha con la
# información, además de mostrar el tipo de dato (type) de la edad y de la altura.

# input() siempre devuelve texto (str), por eso los datos numéricos hay que convertirlos después
nombre_completo = input("Introduce tu nombre completo: ")  # Se queda como str, no necesita conversión

edad_texto = input("Introduce tu edad: ")  # input() devuelve un str aunque el usuario escriba un número
edad = int(edad_texto)  # Convertimos el texto a un número entero (int) para poder operar con él

altura_texto = input("Introduce tu altura en metros (ej. 1.75): ")  # Se recoge como texto
altura = float(altura_texto)  # Convertimos a float porque la altura tiene decimales

ciudad_residencia = input("Introduce tu ciudad de residencia: ")  # Se mantiene como str

respuesta_experiencia = input("¿Tienes experiencia programando? (si/no): ")  # Respuesta en texto
# La comparación == genera directamente un valor booleano (True o False)
tiene_experiencia = respuesta_experiencia.lower() == "si"  # .lower() evita problemas de mayúsculas

# Mostramos la ficha completa usando f-strings: la f delante de las comillas permite
# insertar variables dentro del texto escribiéndolas entre llaves {}
print("----- FICHA PERSONAL -----")
print(f"Nombre completo: {nombre_completo}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} m")
print(f"Ciudad de residencia: {ciudad_residencia}")
print(f"¿Tiene experiencia programando?: {tiene_experiencia}")

# type() nos permite comprobar de qué tipo de dato es cada variable en tiempo de ejecución
print(f"Tipo de dato de la edad: {type(edad)}")
print(f"Tipo de dato de la altura: {type(altura)}")
