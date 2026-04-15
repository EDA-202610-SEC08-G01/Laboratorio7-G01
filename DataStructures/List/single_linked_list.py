from . import list_node as lno

def new_list():
    newlist={
   "first": None,
   "last": None,
   "size": 0
   }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count +=1
    
    if not is_in_array:
        count = -1
    return count

def size(my_list):
    """
    Retorna el tamaño de la lista.
    """
    return my_list["size"]


def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.
    """
    new=lno.new_single_node(element)
    if my_list['first']==None:
        my_list['first']=new
        my_list['last']=new
    else:
        new['next']=my_list['first']
        my_list['first']=new
    my_list['size']+=1
    return my_list




def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    """
    new = lno.new_single_node(element)

    if my_list["last"] is None:
        my_list["first"] = new
        my_list["last"] = new
    else:
        my_list["last"]["next"] = new
        my_list["last"] = new

    my_list["size"] += 1
    return my_list


def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía.
    Lanza IndexError si la lista está vacía.
    """
    if my_list['size'] == 0:
        raise IndexError('list index out of range')
    return my_list['first']['info']


def is_empty(my_list):
    return my_list['size'] == 0

def last_element(my_list):

    if my_list['size'] == 0:
        raise IndexError('list index out of range')

    return my_list['last']['info']

def delete_element(my_list, pos):

    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    
    bef=None
    now = my_list["first"]
    i = 0
    while i < pos:
        bef=now
        now = now["next"]
        i += 1
        
    if bef is None:
        my_list["first"] = now["next"]
    else:
        bef["next"] = now["next"]
    if now == my_list["last"]:
        my_list["last"] = bef

    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["first"] is None:
        raise IndexError("list index out of range")

    node = my_list["first"]
    my_list["first"] = node["next"]

    if my_list["first"] is None:
        my_list["last"] = None

    my_list["size"] -= 1
    return node["info"]

def remove_last(my_list):
    if my_list["first"] is None:
        raise IndexError("list index out of range")

    if my_list["size"] == 1:
        node = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None
    else:
        now = my_list["first"]
        bef = now
        now = now["next"]

        while now["next"] is not None:
            bef = now
            now = now["next"]

        node = now
        bef["next"] = None
        my_list["last"] = bef

    my_list["size"] -= 1
    return node["info"]

def insert_element(my_list, element, pos):

    if pos < 0 or pos >= my_list['size']:
        raise IndexError('list index out of range')
    
    new=lno.new_single_node(element)
    bef=None
    now = my_list['first']
    i = 0
    
    while i < pos:
        bef=now
        now = now['next']
        i += 1
        
    if bef is None:
        new['next']=my_list['first']
        my_list['first'] = new
    else:
        bef['next'] = new
        new['next'] = now
    if now is None:
        my_list['last'] = new

    my_list['size'] += 1
    return my_list

def change_info(my_list, pos, new_info):

    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    now = my_list["first"]
    i = 0

    while i < pos:
        now = now["next"]
        i += 1

    now['info']=new_info
    return my_list

def exchange(my_list, pos_1, pos_2):

    if (pos_1 < 0 or pos_1 >= my_list["size"] or
        pos_2 < 0 or pos_2 >= my_list["size"]):
        raise IndexError("list index out of range")

    now = my_list["first"]
    i = 0
    while i < pos_1:
        now = now["next"]
        i += 1
    node1=now
    now=my_list['first']
    i=0    
    while i < pos_2:
        now = now["next"]
        i += 1
    info2=now['info']
    now['info']=node1['info']
    node1['info']=info2
    return my_list

def sub_list(my_list, pos_i, num_elements):

    if pos_i < 0 or pos_i >= my_list["size"] or pos_i + num_elements > my_list["size"]:
        raise IndexError("list index out of range")

    new = new_list()
    now = my_list["first"]
    i = 0

    while i < pos_i:
        now = now["next"]
        i += 1

    count = 0
    while count < num_elements:
        add_last(new, now["info"])
        now = now["next"]
        count += 1
    return new

