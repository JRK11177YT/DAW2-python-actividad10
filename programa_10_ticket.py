# Alumno: Jorge Ruiz
# Programa 10 - Ticket de una tienda informática
# Calcula el subtotal, el descuento, el IVA y el total de una compra,
# y muestra un ticket con los importes alineados.

nombre_cliente = input("Introduce el nombre del cliente: ")
nombre_producto = input("Introduce el nombre del producto: ")

precio_unitario_texto = input("Introduce el precio unitario (€): ")
precio_unitario = float(precio_unitario_texto)

cantidad_comprada_texto = input("Introduce la cantidad comprada: ")
cantidad_comprada = int(cantidad_comprada_texto)

porcentaje_descuento_texto = input("Introduce el porcentaje de descuento: ")
porcentaje_descuento = float(porcentaje_descuento_texto)

porcentaje_iva_texto = input("Introduce el porcentaje de IVA: ")
porcentaje_iva = float(porcentaje_iva_texto)

# Cálculos del ticket, respetando el orden indicado en el enunciado
subtotal = precio_unitario * cantidad_comprada
importe_descuento = subtotal * (porcentaje_descuento / 100)
precio_tras_descuento = subtotal - importe_descuento
importe_iva = precio_tras_descuento * (porcentaje_iva / 100)
total_a_pagar = precio_tras_descuento + importe_iva

# Dentro de cada f-string, <20 alinea el texto a la izquierda ocupando 20 caracteres
# y >9.2f alinea el número a la derecha ocupando 9 caracteres con dos decimales,
# de forma que todas las columnas del ticket queden alineadas verticalmente
print("----- TICKET -----")
print(f"{'Cliente:':<20}{nombre_cliente:>9}")
print(f"{'Producto:':<20}{nombre_producto:>9}")
print(f"{'Cantidad:':<20}{cantidad_comprada:>9}")
print(f"{'Subtotal:':<20}{subtotal:>9.2f} €")
print(f"{'Descuento:':<20}{importe_descuento:>9.2f} €")
print(f"{'IVA:':<20}{importe_iva:>9.2f} €")
print(f"{'TOTAL:':<20}{total_a_pagar:>9.2f} €")
