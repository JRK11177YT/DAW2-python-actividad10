# Actividad práctica: 10 programas básicos en Python

Diez programas independientes que repasan variables, tipos de datos, entrada de
datos con `input()`, conversión de tipos, operadores aritméticos/relacionales/lógicos
y salidas formateadas con f-strings. No se usan condicionales, bucles, listas ni
funciones propias.

## Requisitos

- Tener Python 3 instalado. Se puede comprobar con:
  ```
  python --version
  ```
  o, en algunos sistemas:
  ```
  python3 --version
  ```

## Cómo ejecutar los programas

1. Abrir una terminal dentro de la carpeta `actividad_10_programas`.
2. Ejecutar el programa que se quiera probar con `python` seguido del nombre del archivo:
   ```
   python programa_01_ficha.py
   ```
   Si `python` no funciona, probar con `python3`:
   ```
   python3 programa_01_ficha.py
   ```
3. Cada programa pedirá los datos necesarios por teclado y mostrará el resultado en la terminal.

### Nota para Windows: símbolos raros (€, tildes, ¿)

Si al ejecutar un programa aparecen símbolos extraños en lugar de € o de las tildes,
es un problema de la codificación de la consola de Windows, no del código. Se soluciona
ejecutando esto una vez en la terminal antes de lanzar los programas:

```
set PYTHONUTF8=1
```

(o `$env:PYTHONUTF8=1` si se usa PowerShell).

## Lista de programas

| Archivo | Descripción |
|---|---|
| programa_01_ficha.py | Ficha personal |
| programa_02_compra.py | Presupuesto de una compra |
| programa_03_temperatura.py | Conversor de temperatura (Celsius → Fahrenheit/Kelvin) |
| programa_04_tiempo.py | Conversor de tiempo (segundos → horas:minutos:segundos) |
| programa_05_nomina.py | Nómina básica de un trabajador |
| programa_06_operaciones.py | Operaciones con dos números |
| programa_07_rectangulo.py | Datos de un rectángulo (área, perímetro, diagonal) |
| programa_08_reparto.py | Reparto de entradas entre grupos |
| programa_09_acceso.py | Comparador lógico de acceso |
| programa_10_ticket.py | Ticket de una tienda informática |
