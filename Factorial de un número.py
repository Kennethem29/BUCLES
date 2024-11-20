# Calcula el factorial de un número
def factorial():
    numero = int(input("Ingresa un número: "))
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(f"El factorial de {numero} es: {resultado}")

factorial()
