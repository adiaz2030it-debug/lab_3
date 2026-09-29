def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero


def dividir(primer_numero, segundo_numero):
    if segundo_numero == 0:
        return "Error: No se puede dividir entre cero."
    return primer_numero / segundo_numero


def es_par(numero):
    return numero % 2 == 0


while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar si un número es par")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # Completa aquí usando match/case.
    match opcion:
        case "1":
            n1 = float(input("ingrese el primer número: ")) 
            n2 = float(input("ingrese el segundo número: ")) 
            print(f"El resultado de la suma es: {sumar(n1, n2)}")
        case "2":
            n1 = float(input("ingrese el primer número: ")) 
            n2 = float(input("ingrese el segundo número: ")) 
            print(f"El resultado de la resta es: {restar(n1, n2)}")
        case "3":
            n1 = float(input("ingrese el primer número: ")) 
            n2 = float(input("ingrese el segundo número: ")) 
            print(f"El resultado de la multiplicación es: {multiplicar(n1, n2)}")
        case "4":
            n1 = float(input("ingrese el primer número: ")) 
            n2 = float(input("ingrese el segundo número: ")) 
            print(f"El resultado de la división es: {dividir(n1, n2)}")
        case "5":
            numero = float(input("ingrese un número: ")) 
            if es_par(numero):
                print(f"El número {numero} es par.")
            else:
                print(f"El número {numero} no es par.")
        case "6":
            print("Saliendo de la calculadora.")
            break
        case _:
            print("Opción no válida. Por favor, intente de nuevo.1")
