
opcion = ""

while opcion != "4":
    
    opcion = input("Elija la conversion que desea hacer marcando un nro del 1 al 3:\n1- Decimal a Binario\n2- Decimal a Octal\n3- Decimal Hexadecimal\n4- Salir del programa\n")

    if opcion == "4": break

    if opcion not in ["1", "2", "3"]:
        print("\nError: Opción inválida.\n")
        continue

    numero = input("Ingrese el nro entero positivo que quiere convertir: ")

    while not numero.isdigit():
        numero = input("Error. Ingrese un nro entero positivo: ")

    numero = int(numero)

    if numero == 0:
        print(f"El resultado es: 0")
        continue

    resultado = ""

    if opcion == "1":
        while numero > 0:
            resultado =  str(numero % 2) + resultado
            numero = numero // 2
        print(f"La conversion a binario es: {resultado}\n")
    elif opcion == "2":
        while numero > 0:
            resultado =  str(numero % 8) + resultado
            numero = numero // 8
        print(f"La conversion a octal es: {resultado}\n")
    else:
        hexa = "0123456789ABCDEF"
        while numero > 0:
            resultado = hexa[numero % 16] + resultado
            numero = numero // 16
        print(f"La conversion a hexadecimal es: {resultado}\n")

print("Gracias por usar el programa")