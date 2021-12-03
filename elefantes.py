def incomodam(n):
    if n <= 0:
        return ''
    
    else:
        if n > 0:
            return 'incomodam ' + incomodam(n-1)
        
def elefantes(n, inicio = 1):
    if n < 1:
        return ''
    if inicio == n:
        return ''
    elif inicio == 1:
        return "Um elefante incomoda muita gente\n" + str(inicio+1) + " elefantes " + incomodam(inicio+1) + "muito mais\n" + elefantes(n, inicio + 1)
    else:
        return str(inicio) + " elefantes incomodam muita gente\n" + str(inicio+1) + " elefantes " + incomodam(inicio+1) + "muito mais\n" + elefantes(n, inicio + 1)
            

if __name__ == '__main__':
    n = 0
    print(elefantes(n))