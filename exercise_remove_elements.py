# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
   
    indice = len(lista)
    
    if indice >= 6:
        del lista[0]
        del lista[3] #el 4 pasa a ser el nuevo 3 porque se eliminó el primer elemento.
        del lista[3] #una vez que se eliminaron el 0 y el 4 de la lista principal, el 5 pasa a ser el neuvo 3.
    
    elif indice > 1 and indice < 5:
        del lista[0]
   
    elif indice <= 1:
        lista = []
    
    return lista

autos = ["Porsche" , "Ferrari", "Lamborghini", "Bugatti", "Tesla", "Audi", "BMW", "Mercedes Benz", "Pagani"]

print(remove_elements(autos))
