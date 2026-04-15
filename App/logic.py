import os
import csv
import datetime

from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import single_linked_list as al

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


def new_logic():
    analyzer = {'crimes': None,
                'dateIndex': None
                }

    analyzer['crimes'] = al.new_list()
    analyzer['dateIndex'] = bst.new_map()

    return analyzer


def load_data(analyzer, crimesfile):
    crimesfile = data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        add_crime(analyzer, crime)
    return analyzer


def add_crime(analyzer, crime):
    al.add_last(analyzer['crimes'], crime)
    update_date_index(analyzer['dateIndex'], crime)
    return analyzer


def update_date_index(map, crime):
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')

    entry = bst.get(map, crimedate.date())

    if entry is None:
        datentry = new_data_entry(crime)
        bst.put(map, crimedate.date(), datentry)
    else:
        datentry = entry

    add_date_index(datentry, crime)
    return map


def add_date_index(datentry, crime):
    lst = datentry['lstcrimes']
    al.add_last(lst, crime)

    offenseIndex = datentry['offenseIndex']
    offentry = lp.get(offenseIndex, crime['OFFENSE_CODE_GROUP'])

    if offentry is None:
        new_entry = new_offense_entry(crime['OFFENSE_CODE_GROUP'], crime)
        lp.put(offenseIndex, crime['OFFENSE_CODE_GROUP'], new_entry)
        al.add_last(new_entry['lstoffenses'], crime)
    else:
        al.add_last(offentry['lstoffenses'], crime)

    return datentry


def new_data_entry(crime):
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = lp.new_map(30, 0.5)
    entry['lstcrimes'] = al.new_list()
    return entry


def new_offense_entry(offensegrp, crime):
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = al.new_list()
    return ofentry


# ==============================
# CONSULTAS
# ==============================

def crimes_size(analyzer):
    return al.size(analyzer['crimes'])


def index_height(analyzer):
    return bst.height(analyzer['dateIndex'])


def index_size(analyzer):
    return bst.size(analyzer['dateIndex'])


def min_key(analyzer):
    return bst.get_min(analyzer['dateIndex'])


def max_key(analyzer):
    return bst.get_max(analyzer['dateIndex'])


def get_crimes_by_range(analyzer, initialDate, finalDate):
    start = datetime.datetime.strptime(initialDate, '%Y-%m-%d').date()
    end = datetime.datetime.strptime(finalDate, '%Y-%m-%d').date()

    values = bst.values(analyzer['dateIndex'], start, end)

    total = 0
    node_val = values["first"]

    while node_val is not None:
        entry = node_val["info"]
        total += al.size(entry['lstcrimes'])
        node_val = node_val["next"]

    return total


def get_crimes_by_range_code(analyzer, initialDate, offensecode):
    date = datetime.datetime.strptime(initialDate, '%Y-%m-%d').date()

    entry = bst.get(analyzer['dateIndex'], date)

    if entry is None:
        return 0

    offenseEntry = lp.get(entry['offenseIndex'], offensecode)

    if offenseEntry is None:
        return 0

    return al.size(offenseEntry['lstoffenses'])