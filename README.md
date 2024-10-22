
# Calculadora Sencilla

Este es un proyecto básico de una calculadora en Python que permite realizar operaciones aritméticas simples como suma, resta, multiplicación y división. El programa utiliza una interfaz de consola para que el usuario seleccione la operación deseada y proporcione los valores de entrada.

## Funcionalidades

La calculadora admite las siguientes operaciones:

1. **Suma**: Añade dos números.
2. **Resta**: Resta el segundo número del primero.
3. **Multiplicación**: Multiplica dos números.
4. **División**: Divide el primer número por el segundo (con comprobación de división por cero).

## Uso

1. Ejecuta el programa.
2. Selecciona una opción de operación:
   - `1` para Suma
   - `2` para Resta
   - `3` para Multiplicación
   - `4` para División
3. Ingresa los dos números para la operación.
4. El resultado se mostrará en la consola.


## Ejemplo de uso

```python
Selecciona una opción:
1. Suma
2. Resta
3. Multiplicación
4. División
Ingresa una opción:1
Ingresa el primer valor:2
Ingresa el segundo valor:2
2.0 + 2.0 = 4.0
```

## Requisitos

- Python 3.10 o superior (necesario para la declaración `match`).

## Notas

- El programa incluye una validación para evitar la división por cero.
- Si se ingresa una opción no válida, se mostrará un mensaje de error.

## Ejecución

Para ejecutar la calculadora, puedes usar el siguiente comando en la terminal:

```bash
python calculadora.py
```


## Mejoras Futuras
1. Implementar una interfaz gráfica de usuario (GUI).
2. Agregar más funciones matemáticas (potencia, raíz cuadrada, etc.).
2. Manejo de errores mejorado.
