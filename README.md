# Calculadora Sencilla

Este es un proyecto básico de una calculadora en Python que permite realizar operaciones aritméticas simples como suma, resta, multiplicación y división. El programa utiliza una interfaz de consola con validación de entradas y la posibilidad de realizar múltiples operaciones en una misma ejecución.

## Funcionalidades

La calculadora admite las siguientes operaciones:

1. **Suma**: Añade dos números.
2. **Resta**: Resta el segundo número del primero.
3. **Multiplicación**: Multiplica dos números.
4. **División**: Divide el primer número por el segundo (con comprobación de división por cero).

## Mejoras Incluidas

- Validación de opciones ingresadas por el usuario.
- Manejo de errores si se ingresan datos no numéricos.
- Control de división por cero.
- Permite realizar múltiples operaciones sin reiniciar el programa.
- Código modular con funciones separadas y una estructura principal en `main()`.

## Uso

1. Ejecuta el programa.
2. Selecciona una opción de operación:
   - `1` para Suma
   - `2` para Resta
   - `3` para Multiplicación
   - `4` para División
3. Ingresa los dos números cuando se te solicite.
4. El resultado se mostrará en la consola.
5. El programa te preguntará si deseas hacer otra operación.

## Ejemplo de uso

```text
Selecciona una opción:
1. Suma
2. Resta
3. Multiplicación
4. División
Ingresa una opción: 1
Ingresa el primer valor: 5
Ingresa el segundo valor: 3
5.0 + 3.0 = 8.0

¿Deseas hacer otra operación? (s/n): s
```

## Requisitos

- Python 3.10 o superior (necesario para la instrucción `match`).

## Notas

- El programa valida que los valores ingresados sean numéricos.
- Si el usuario intenta dividir entre cero, se mostrará un mensaje de error.
- La calculadora sigue funcionando hasta que el usuario decida salir.

## Ejecución

Para ejecutar la calculadora, usa el siguiente comando en la terminal:

```bash
python calculadora.py
```

## Mejoras Futuras

1. Implementar una interfaz gráfica de usuario (GUI) con PyQt o Tkinter.
2. Agregar más funciones matemáticas: potencia, raíz cuadrada, módulo, etc.
3. Almacenar historial de operaciones.
4. Uso de expresiones matemáticas completas como entrada (ej: `2 + 3 * 4`).
