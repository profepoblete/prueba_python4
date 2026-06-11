
try:
    
    while True:
        try:
            numerador = int(input("Ingrese numerador: "))
            if numerador > 0:
                break
            else:
                print("El numerador debe ser un entero positivo")
        except ValueError as v1:
            print("Error de valor. Debe ser un entero positivo")



    while True:
        try:
            divisor = int(input("Ingrese divisor: "))
            if divisor > 0:
                break
            else:
                print("El divisor debe ser un entero positivo")
        except ValueError as v1:
            print("Error de valor. Debe ser un entero positivo")

    resultado = numerador/divisor

    print(f"El resultado es: {resultado}")
except ValueError as ve:
    print("Error de tipo de valor. Debe ingresar enteros positivos")
except ZeroDivisionError as ze:
    print("Error al tratar de deividir por 0. El divisor debe ser un entero positivo")
except Exception as ex:
    print(f"Ups!!! ocurrió un error inesperado. Llame a mesa de ayuda \n Detalle: {ex}")