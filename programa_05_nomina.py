# Alumno: Jorge Ruiz
# Programa 05 - Nómina básica de un trabajador
# Calcula el salario bruto, el importe de la retención y el salario neto de un trabajador.

nombre_trabajador = input("Introduce el nombre del trabajador: ")

horas_trabajadas_texto = input("Introduce el número de horas trabajadas: ")
horas_trabajadas = float(horas_trabajadas_texto)  # float porque puede haber medias horas

precio_hora_texto = input("Introduce el precio pagado por hora (€): ")
precio_hora = float(precio_hora_texto)  # float porque el precio puede llevar decimales

porcentaje_retencion_texto = input("Introduce el porcentaje de retención: ")
porcentaje_retencion = float(porcentaje_retencion_texto)

# Cálculos de la nómina
salario_bruto = horas_trabajadas * precio_hora  # Total ganado antes de aplicar la retención
importe_retencion = salario_bruto * (porcentaje_retencion / 100)  # Parte del bruto que se retiene
salario_neto = salario_bruto - importe_retencion  # Lo que finalmente cobra el trabajador

# Mostramos la nómina con dos decimales, como una pequeña "hoja de pago"
print("----- NÓMINA -----")
print(f"Trabajador: {nombre_trabajador}")
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Retención ({porcentaje_retencion:.2f}%): {importe_retencion:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")
