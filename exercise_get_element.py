# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    
    lista_autos = len(lista) -1
    
    # pones el -1 porque cuenta del 0 hasta un número menos de 
    # la cantidad que son. Si son 6 elementos, te va a contar 5, porque el 0 es un número.
      
    if indice > lista_autos:
        return None
   
    elif indice < - lista_autos:
        return None
    
    else:
        return lista[indice] #se pone así porque es el indice que corresponde a la lista.
 
# indice_a = int(input())

# autos = ["Porsche", "Ferrari", "Lamborghini", "Bugatti", "Tesla"]

# print(get_element(autos, indice_a))