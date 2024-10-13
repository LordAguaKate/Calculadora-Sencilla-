# Calculadora sencilla Proyecto basico 
# Funciones para la calculadora

def sum (num1, num2):
    return num1 + num2

def rest (num1, num2):
    return num1 - num2

def mult (num1, num2):
    return num1 * num2

def div (num1, num2):
    return num1 / num2

# Avisos al usuario desde la consola
print("Selecciona una opción:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Ingresa una opción
opcion = input("Ingresa una opción:")

# Valores de num1 y num2
num1 = float(input("Ingresa el primer valor:"))
num2 = float(input("Ingresa el segundo valor:"))

# Uso de case
match opcion:
    case '1':
        print(f"{num1} + {num2} = {sum(num1, num2)}")
        
    case '2':
        print(f"{num1} - {num2} = {rest(num1, num2)}")
        
    case '3':
        print(f"{num1} * {num2} = {mult(num1, num2)}")
        
    case '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {div(num1, num2)}")
        else:
            print("Error: No se puede dividir entre 0")
    case _:
        print("Opción inválida")






