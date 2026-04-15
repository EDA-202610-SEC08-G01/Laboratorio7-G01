from DataStructures.Map import map_functions as mf
import random

def new_map(num_keys, load_factor, prime=109345121):
    
    capacity = mf.next_prime(int(num_keys / load_factor))
    
    table = [None] * capacity
    
    map = {
        "capacity": capacity,
        "size": 0,
        "table": table,
        "load_factor": load_factor,
        "limit_factor": load_factor,
        "prime": prime,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "current_factor": 0
    }
    
    return map

def is_available(table, pos):
    
    entry = table[pos]
    
    if entry is None:
        return True
    
    if entry.get("deleted", False):
        return True
    
    return False

def default_compare(key1, key2):
    return key1 == key2

def find_slot(map, key, hash_value):
    
    table = map["table"]
    capacity = map["capacity"]
    
    pos = hash_value
    
    while True:
        
        entry = table[pos]
        
        if is_available(table, pos):
            return False, pos
        
        elif default_compare(entry["key"], key):
            return True, pos
        
        pos = (pos + 1) % capacity


def put(map, key, value):
    
    table = map["table"]
    
    # usar hash del lab
    hash_value = mf.hash_value(map, key)
    
    # encontrar posición
    found, pos = find_slot(map, key, hash_value)
    
    if found:
        table[pos]["value"] = value
    else:
        table[pos] = {"key": key, "value": value}
        map["size"] += 1
    
    # actualizar factor
    map["current_factor"] = map["size"] / map["capacity"]
    
    # rehash si necesario
    if map["current_factor"] > map["load_factor"]:
        map = rehash(map)
    
    return map


def get(map, key):
    
    table = map["table"]
    
    # usar hash correcto
    hash_value = mf.hash_value(map, key)
    
    # buscar posición
    found, pos = find_slot(map, key, hash_value)
    
    if found:
        return table[pos]["value"]
    
    return None


def contains(map, key):
    
    # usar hash correcto
    hash_value = mf.hash_value(map, key)
    
    # buscar
    found, pos = find_slot(map, key, hash_value)
    
    return found


def remove(map, key):
    
    table = map["table"]
    
    # hash correcto
    hash_value = mf.hash_value(map, key)
    
    # buscar
    found, pos = find_slot(map, key, hash_value)
    
    if found:
        table[pos]["deleted"] = True
        map["size"] -= 1
        
        # actualizar factor
        map["current_factor"] = map["size"] / map["capacity"]
    
    return map

def size(map):
    return map["size"]

def rehash(map):
    
    old_table = map["table"]
    old_capacity = map["capacity"]

    new_capacity = mf.next_prime(old_capacity * 2)
    
    # nueva tabla
    map["table"] = [None] * new_capacity
    map["capacity"] = new_capacity
    map["size"] = 0
    map["current_factor"] = 0
    
    for entry in old_table:
        if entry is not None and not entry.get("deleted", False):
            put(map, entry["key"], entry["value"])
    
    return map

def is_empty(map):
    return map["size"] == 0

from DataStructures.List import array_list as lt

def key_set(map):
    keys = lt.new_list()
    
    for entry in map["table"]:
        if entry is not None and not entry.get("deleted", False):
            lt.add_last(keys, entry["key"])
    
    return keys

def value_set(map):
    values = lt.new_list()
    
    for entry in map["table"]:
        if entry is not None and not entry.get("deleted", False):
            lt.add_last(values, entry["value"])
    
    return values