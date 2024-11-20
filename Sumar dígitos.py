# Calcula la suma de los dígitos de un número
def suma_digitos():
    numero = input("Ingresa un número entero: ")
    suma = sum(int(digito) for digito in numero)
    print(f"La suma de los dígitos es: {suma}")

suma_digitos()
