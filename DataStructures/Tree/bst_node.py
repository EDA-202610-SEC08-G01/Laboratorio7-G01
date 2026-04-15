"""
Estructura que contiene la información a guardar en un nodo de un árbol binario
"""


def new_node(key, value):
    """
    Crea un nuevo nodo para un árbol binario de búsqueda (BST)
    """
    return {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "type": "BST",
    }


def get_value(my_node):
    """
    Retorna el valor del nodo
    """
    if my_node is None:
        return None
    return my_node["value"]


def get_key(my_node):
    """
    Retorna la llave del nodo
    """
    if my_node is None:
        return None
    return my_node["key"]