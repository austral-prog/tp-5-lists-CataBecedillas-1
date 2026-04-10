# Ejercicio 8: Invertir una lista

def reverse_list(lista):
    """
    Retorna una nueva lista con los elementos en orden inverso.

    Args:
        lista: Una lista de elementos

    Returns:
        Una nueva lista con los elementos en orden inverso
    """

    return lista[::-1]

autos = ["Porsche" , "Ferrari", "Lamborghini", "Bugatti", "Tesla", "Audi", "BMW", "Mercedes Benz", "Pagani"]
print(reverse_list(autos))
