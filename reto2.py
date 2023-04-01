#-Crea una función  que reciba una lista con valores numéricos y 
# devuelva el valor máximo y el mínimo ingresados


def max_min(lista):
    """
    Esta función recibe una lista con valores numéricos y devuelve el valor máximo y mínimo ingresados.
    """
    if len(lista) == 0:
        return None
    
    maximo = lista[0]
    minimo = lista[0]
    
    for valor in lista:
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
            
    return maximo, minimo

mi_lista = [1, 2, 3, 4, 5]
resultado = max_min(mi_lista)
print(resultado) 
