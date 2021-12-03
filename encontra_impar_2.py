def encontra_impares(lista):
    lista_impar = []
    local = 0
    return auxiliar(lista, local, lista_impar)
    
def auxiliar(lista, local, lista_impar):
    
    if local == len(lista):
        return lista_impar
    else:
        if lista[local]%2 != 0:
            lista_impar.extend([lista[local]])
            return auxiliar(lista, local+1, lista_impar)
        else:
            return auxiliar(lista, local+1, lista_impar)
        
    
    
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print (encontra_impares(lista))