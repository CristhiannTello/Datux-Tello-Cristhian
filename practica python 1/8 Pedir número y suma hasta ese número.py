# Solicitamos un número entero 
numero = int(input("ingresa un número entero que sea positivo: "))

# Verificamos que el número sea positivo
if numero > 0:
    # Calculamow la suma usando la fórmula
    suma = (numero * (numero + 1)) // 2
    print(f"La suma de los números de 1 hasta {numero} es: {suma}")
else:
    print("El número debe ser un entero positivo, ejecuta el código nuevamente.")