# Ejercicio 1: Obtener la longitud de una lista

def list_length(lista):
    """
    Retorna la cantidad de elementos en la lista.

    Args:
        lista: Una lista de cualquier tipo de elementos

    Returns:
        Un entero con la cantidad de elementos
    """
    
    return len(lista) #pongo return len(nombre de la función principal)

autos = ["Porsche" , "Ferrari", "Lamborghini", "Bugatti", "Tesla"] #afuera de la función escribo la lista.
print(list_length(autos)) #printeo la función con el paréntesis del nombre de la lista.