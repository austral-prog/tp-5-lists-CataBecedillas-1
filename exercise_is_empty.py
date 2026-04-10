# Ejercicio 9: Verificar si una lista está vacía

def is_empty(lista):
    """
    Determina si una lista está vacía.

    Args:
        lista: Una lista de elementos

    Returns:
        True si la lista está vacía, False en caso contrario
    """
    
    indice = len(lista)
    
    if indice > 0:
        return False
    else:
        return True
    
autos = []
print(is_empty(autos))

