# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    
    #para la lista1:
    if len(lista_de_listas[0]) >= 2:
        lista_de_listas[0] = lista_de_listas[0][0:2] #cuando la lista es mayor igual a 2, la lista de lista va a ser del elemento 0 al dos.
    elif len(lista_de_listas[0]) == 1:
        lista_de_listas[0] = lista_de_listas[0]
    else:
        lista_de_listas[0] = []
        
    #para la lista2:
    if len(lista_de_listas[1]) >= 4:
        lista_de_listas[1] = lista_de_listas[1][1:4]
    elif len(lista_de_listas[1]) > 2 and len(lista_de_listas[1]) < 4:
        lista_de_listas[1] = lista_de_listas[1][1:] #cuando no pones nada es porque va hasta el final.
    else:
        lista_de_listas[1] = []
        
    #para la lista3:
    if len(lista_de_listas[2]) >= 2:
        lista_de_listas[2] = lista_de_listas[2][-2:]
    elif len(lista_de_listas[2]) < 2:
        lista_de_listas[2] = lista_de_listas[2]
        
    return lista_de_listas
        
mi_lista = [["Porsche", "Bugatti", "Audi"], [1, 2, 3], ["Hola", "Chau",]]
print(list_of_lists(mi_lista))