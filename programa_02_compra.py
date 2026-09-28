# Alumno: Jorge Ruiz
# Programa 02 - Presupuesto de una compra
# Calcula el importe sin IVA, el importe del IVA y el precio final de una compra.

nombre_producto = input("Introduce el nombre del producto: ")  # Texto, no requiere conversión

precio_unitario_texto = input("Introduce el precio unitario (€): ")
precio_unitario = float(precio_unitario_texto)  # float porque el precio puede llevar decimales

cantidad_unidades_texto = input("Introduce la cantidad de unidades: ")
cantidad_unidades = int(cantidad_unidades_texto)  # int porque las unidades son un número entero

porcentaje_iva_texto = input("Introduce el porcentaje de IVA (ej. 21): ")
porcentaje_iva = float(porcentaje_iva_texto)  # Puede llevar decimales, por eso usamos float

# Cálculos del presupuesto (la precedencia de operadores hace * antes que las asignaciones)
importe_sin_iva = precio_unitario * cantidad_unidades  # Precio unitario multiplicado por las unidades
importe_iva = importe_sin_iva * (porcentaje_iva / 100)  # El IVA es un porcentaje del importe sin IVA
precio_final = importe_sin_iva + importe_iva  # El precio final suma el importe sin IVA más el IVA

# :.2f dentro de un f-string redondea y muestra el número con exactamente dos decimales
print("----- PRESUPUESTO DE COMPRA -----")
print(f"Producto: {nombre_producto}")
print(f"Cantidad: {cantidad_unidades}")
print(f"Importe sin IVA: {importe_sin_iva:.2f} €")
print(f"Importe del IVA: {importe_iva:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
