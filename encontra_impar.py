def encontra_impares(lista):
    for n in lista:
        while n % 2 == 0:
            if lista[0]%2 != 0:
                lista.extend([lista[0]])
                return encontra_impares(lista[1:])
            else:
                return encontra_impares(lista[1:])
    fim = True
    if fim:
        return lista
            
if __name__ == '__main__':
    print (encontra_impares([7, 2, 3, 4, 5, 9, 6, 13]))