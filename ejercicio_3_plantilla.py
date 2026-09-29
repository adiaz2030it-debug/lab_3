numero_dia = int(input("Escribe un número del 1 al 7: "))

match numero_dia:
    case 1:
        print("El día seleccionado es: Lunes")

    # Completa los casos del 2 al 7.

    case _:
        print("Error: el número debe estar entre 1 y 7.")

        print("")