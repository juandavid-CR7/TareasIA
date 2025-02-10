# Ejercicio 2 serie de sucecion fibonacci

def fibonacci(numeros):
    secuencia = [0, 1]
    while len(secuencia) < numeros:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Imprimir los primeros 15 números de la serie Fibonacci
print(fibonacci(15))