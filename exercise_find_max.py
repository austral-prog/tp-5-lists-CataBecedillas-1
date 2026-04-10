# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
    
    indice = len(lista)
    
    if indice > 0:
        return max(lista)
    else:
        return None

numeros = [-1, -2, -3, -4]
print(find_max(numeros))
