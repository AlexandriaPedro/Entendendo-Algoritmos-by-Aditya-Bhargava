def buscaIndiceDoMenorValor(array):
    menor_valor = array[0]
    indice_menor_valor = 0
    for indice in range(1, len(array)):
        if menor_valor > array[indice]:
            menor_valor = array[indice]
            indice_menor_valor = indice
    
    return indice_menor_valor

def ordenacaoPorSelecao(array):
    array_ordenado = []
    for indice in range(len(array)):
        indice_do_menor_valor = buscaIndiceDoMenorValor(array)
        array_ordenado.append(array.pop(indice_do_menor_valor))

    return array_ordenado

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))
print(ordenacaoPorSelecao([1, 2, 3, 5, 4]))
print(ordenacaoPorSelecao([1000, 100, 10, 10, 1]))
print(ordenacaoPorSelecao([5, 3, 5, 5, 3]))
print(ordenacaoPorSelecao([1, 2, 3, 4, -5]))
