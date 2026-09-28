# Alumno: Jorge Ruiz
# Programa 04 - Conversor de tiempo
# Convierte una cantidad de segundos en horas, minutos y segundos restantes,
# usando obligatoriamente los operadores // (división entera) y % (módulo).

total_segundos_texto = input("Introduce la cantidad total de segundos: ")
total_segundos = int(total_segundos_texto)  # int porque los segundos se introducen como número entero

# // es la división entera: divide y descarta la parte decimal del resultado
# % es el módulo: devuelve el resto que sobra de una división
horas = total_segundos // 3600  # Cuántas horas completas caben en el total de segundos
segundos_tras_horas = total_segundos % 3600  # Lo que sobra después de quitar las horas completas
minutos = segundos_tras_horas // 60  # Cuántos minutos completos caben en lo que sobra
segundos_restantes = segundos_tras_horas % 60  # Lo que sobra después de quitar también los minutos

# :02 dentro del f-string rellena con un cero a la izquierda si el número tiene un solo dígito
# (por ejemplo, 2 se muestra como 02), para lograr el formato HH:MM:SS del enunciado
print("----- CONVERSOR DE TIEMPO -----")
print(f"{horas:02}:{minutos:02}:{segundos_restantes:02}")
