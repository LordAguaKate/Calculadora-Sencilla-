def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b

def main():
    while True:
        print("\nSelecciona una opción:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion = input("Ingresa una opción: ")

        if opcion not in ('1', '2', '3', '4'):
            print("Opción inválida")
            continue

        try:
            num1 = float(input("Ingresa el primer valor: "))
            num2 = float(input("Ingresa el segundo valor: "))
        except ValueError:
            print("Error: debes ingresar números.")
            continue

        match opcion:
            case '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            case '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            case '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            case '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {dividir(num1, num2)}")
                else:
                    print("Error: No se puede dividir entre 0")

        if input("¿Deseas hacer otra operación? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
