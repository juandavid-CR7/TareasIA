def suma_lista(numeros):
    total = 0
    for num in numeros:
        total += num
    return total

lista = [1, 2, 3, 4, 5]
print("Suma de la lista de numeros:", suma_lista(lista))