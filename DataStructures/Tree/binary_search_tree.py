from DataStructures.Tree import bst_node as node
from DataStructures.List import single_linked_list as lt

def new_map():
    return {"root": None}

def new_tree():
    return {"root": None}

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def size(tree):
    return size_tree(tree["root"])

def default_compare(key1, key2):
    if key1 < key2:
        return -1
    elif key1 > key2:
        return 1
    return 0

def insert_node(root, key, value):
    if root is None:
        return node.new_node(key, value)
    cmp = default_compare(key, node.get_key(root))
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(tree, key, value):
    tree["root"] = insert_node(tree["root"], key, value)
    return tree

def get_node(root, key):
    if root is None:
        return None
    cmp = default_compare(key, node.get_key(root))
    if cmp < 0:
        return get_node(root["left"], key)
    elif cmp > 0:
        return get_node(root["right"], key)
    else:
        return root

def get(tree, key):
    result = get_node(tree["root"], key)
    if result is None:
        return None
    return node.get_value(result)

def is_empty(tree):
    return tree["root"] is None

def contains(tree, key):
    return get(tree, key) is not None

def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root
    return get_min_node(root["left"])

def get_min(tree):
    node_min = get_min_node(tree["root"])
    if node_min is None:
        return None
    return node.get_key(node_min)

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root
    return get_max_node(root["right"])

def get_max(tree):
    node_max = get_max_node(tree["root"])
    if node_max is None:
        return None
    return node.get_key(node_max)

def height_tree(root):
    if root is None:
        return 0

    left = height_tree(root["left"])
    right = height_tree(root["right"])

    return 1 + max(left, right)

def height(tree):
    return height_tree(tree["root"])

def key_set_tree(root, result):
    if root is None:
        return

    key_set_tree(root["left"], result)
    lt.add_last(result, node.get_key(root))
    key_set_tree(root["right"], result)


def key_set(tree):
    result = lt.new_list()
    key_set_tree(tree["root"], result)
    return result


def value_set_tree(root, result):
    if root is None:
        return

    value_set_tree(root["left"], result)
    lt.add_last(result, node.get_value(root))
    value_set_tree(root["right"], result)


def value_set(tree):
    result = lt.new_list()
    value_set_tree(tree["root"], result)
    return result

def keys_range(root, lo, hi, result):
    if root is None:
        return

    key = node.get_key(root)

    if lo < key:
        keys_range(root["left"], lo, hi, result)

    if lo <= key <= hi:
        lt.add_last(result, key)

    if key < hi:
        keys_range(root["right"], lo, hi, result)


def keys(tree, lo, hi):
    result = lt.new_list()
    keys_range(tree["root"], lo, hi, result)
    return result

def values_range(root, lo, hi, result):
    if root is None:
        return

    key = node.get_key(root)

    if lo < key:
        values_range(root["left"], lo, hi, result)

    if lo <= key <= hi:
        lt.add_last(result, node.get_value(root))

    if key < hi:
        values_range(root["right"], lo, hi, result)


def values(tree, lo, hi):
    result = lt.new_list()
    values_range(tree["root"], lo, hi, result)
    return result

def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def delete_min(tree):
    if not is_empty(tree):
        tree["root"] = delete_min_tree(tree["root"])
    return tree


def delete_max_tree(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def delete_max(tree):
    if not is_empty(tree):
        tree["root"] = delete_max_tree(tree["root"])
    return tree