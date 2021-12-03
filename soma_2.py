def soma_lista(lista):
    local = 0
    soma = 0
    return calc(lista, local, soma)
    
def calc(lista, local, soma):
    if local == len(lista):
        return soma
    else:
        return calc(lista, local+1, soma + lista[local])
        
    
if __name__ == '__main__':
    print (soma_lista([5, 6, 9, 25]))