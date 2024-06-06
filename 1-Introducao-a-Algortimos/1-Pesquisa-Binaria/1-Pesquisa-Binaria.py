"""
Implementação do algoritmo de Pesquisa Binária
de forma simples e imperativa.
"""


def pesquisa_binaria(lista_ordenada, item_desejado):
    """
    Retorna a posição do item desejado na lista,
    caso ele exista. Se o item não estive na lista,
    o retorno será 'None'.
    """

    indice_do_topo_da_lista = len(lista_ordenada) - 1
    indice_da_base_da_lista = 0

    while indice_da_base_da_lista <= indice_do_topo_da_lista:
        indice_do_meio_da_lista = (
            indice_da_base_da_lista + indice_do_topo_da_lista
        ) / 2
        indice_do_meio_da_lista = int(indice_do_meio_da_lista)

        item_do_meio_da_lista = lista_ordenada[indice_do_meio_da_lista]

        if item_desejado == item_do_meio_da_lista:
            return indice_do_meio_da_lista

        if item_desejado > item_do_meio_da_lista:
            indice_da_base_da_lista = indice_do_meio_da_lista + 1
        else:
            indice_do_topo_da_lista = indice_do_meio_da_lista - 1

    return None

def main():
    # Testando um tiquim:
    lista_ordenada = list(range(1, 11))

    print(pesquisa_binaria(lista_ordenada, 1))
    print(pesquisa_binaria(lista_ordenada, 2))
    print(pesquisa_binaria(lista_ordenada, 5))
    print(pesquisa_binaria(lista_ordenada, 10))
    print(pesquisa_binaria(lista_ordenada, 11))
    print(pesquisa_binaria(lista_ordenada, -1))

if __name__ == "__main__":
    main()
