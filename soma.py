def soma_lista(lista):

    if len(lista) == 1:
        return lista[0]
    else:
        soma = lista[0] + lista[1]
        lista[1] = soma
        return soma_lista(lista[1:]) # devolve a lista até o final a partir do primeiro elemento, depois a partir do segundo, assim sucessivamente

if __name__ == '__main__':
    print (soma_lista([2, 3, 5, 10, 40]))
    

