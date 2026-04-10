# Ejercicio 7: Contar ocurrencias de un elemento

def count_occurrences(lista, elemento):
    """
    Cuenta cuántas veces aparece un elemento en la lista.

    Args:
        lista: Una lista de elementos
        elemento: El elemento a buscar

    Returns:
        Un entero con la cantidad de veces que aparece el elemento
    """
    
    ocurrencias = lista.count(elemento) #te cuenta en "lista" la cantidad de veces que aparece la variable "elemento".

    return ocurrencias

autos = ["Porsche" , "Ferrari", "Lamborghini", "Porsche", "Tesla", "Audi", "BMW", "Mercedes Benz", "Pagani"]
elemento = "Porsche"
print(count_occurrences(autos, elemento))