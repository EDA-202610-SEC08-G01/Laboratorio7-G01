import random
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me

def new_map(num_elements, load_factor, prime):

    capacity = mf.next_prime(int(num_elements / load_factor))

    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)

    table = []
    for i in range(capacity):
        table.append(al.new_list())

    return {
        "capacity": capacity,
        "size": 0,
        "table": table,
        "prime": prime,   
        "scale": scale,
        "shift": shift,
        "load_factor": load_factor
    }
    
def hash_value(map, key):
    return mf.hash_value(map, key)

def put(map, key, value):
    index = hash_value(map, key)
    bucket = map["table"][index]

    for i in range(1, al.size(bucket) + 1):
        entry = al.get_element(bucket, i)
        if entry["key"] == key:
            entry["value"] = value
            return map

    entry = me.new_map_entry(key, value)
    al.add_last(bucket, entry)
    map["size"] += 1

    current_load = map["size"] / map["capacity"]

    if current_load > map["load_factor"]:
        rehash(map)

    return map

def get(map, key):
    index = hash_value(map, key)
    bucket = map["table"][index]

    for i in range(1, al.size(bucket) + 1):
        entry = al.get_element(bucket, i)
        if entry["key"] == key:
            return entry["value"]

    return None

def rehash(map):

    old_table = map["table"]

    new_capacity = mf.next_prime(map["capacity"] * 2)

    map["capacity"] = new_capacity
    map["size"] = 0

 
    new_table = []
    for i in range(new_capacity):
        new_table.append(al.new_list())

    map["table"] = new_table

    for bucket in old_table:
        for i in range(1, al.size(bucket) + 1):
            entry = al.get_element(bucket, i)
            put(map, entry["key"], entry["value"])

    return map

def contains(map, key):
    return get(map, key) is not None

def remove(map, key):
    index = hash_value(map, key)
    bucket = map["table"][index]

    for i in range(1, al.size(bucket) + 1):
        entry = al.get_element(bucket, i)
        if entry["key"] == key:
            al.delete_element(bucket, i) 
            map["size"] -= 1
            return entry["value"]

    return None

def size(map):
    return map["size"]

def is_empty(map):
    return map["size"] == 0

def key_set(map):
    keys = al.new_list()

    for bucket in map["table"]:
        for i in range(1, al.size(bucket) + 1):
            entry = al.get_element(bucket, i)
            al.add_last(keys, entry["key"])

    return keys

def value_set(map):
    values = al.new_list()

    for bucket in map["table"]:
        for i in range(1, al.size(bucket) + 1):
            entry = al.get_element(bucket, i)
            al.add_last(values, entry["value"])

    return values