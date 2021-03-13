# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#     scoring script for A6
#     student version
#
#     Run this script to see how many of your functions work!
#

import LList as L

verbose = True  # change to False to reduce output


##### THIS DOES THE WORK
def runemall():
    # a simple script to try all the tests
    count = 0
    passed = 0
    failed = 0
    for t in all_of_em:
        print('Passed:', passed, 'test out of', count)
        count += 1
        try:
            # try calling the function t
            t()
            passed += 1
        except Exception as e:
            # something went wrong in the function call t()
            if verbose:
                print("Test failure in function:", t.__name__)
                print(e)
            failed += 1

    print('Total tests:', count, 'Tests passed:', passed)
    print('-------------------------------------------')

    score = [(17, 0), (35, 5), (53, 10), (71, 15), (89, 20), (107, 24), (125, 27), (143, 30)]

    for (p, s) in score:
        if passed <= p:
            print('Passed:', passed, 'Resulting Grade:', s, 'out of 30')
            break
    return


###### A load of tests follows
# all the unit and integration tests


def test_create_initial_size():
    allist = L.LList()
    result = allist._size
    assert result == 0, "create(): Check size in new LList record; returned " + str(result)


def test_create_initial_head():
    allist = L.LList()
    result = allist._head
    assert result is None, "create(): Check head in new LList record; returned " + str(result)


def test_create_initial_tail():
    allist = L.LList()
    result = allist._tail
    assert result is None, "create(): Check tail in new LList record; returned " + str(result)


###############################################################################################
# UNIT TESTING - List.empty(), List.size()
###############################################################################################

def test_empty_empty():
    # create a record by hand
    thellist = L.LList()

    # check if is_empty() works
    result = thellist.is_empty()
    assert result, 'is_empty() on new LList record; returned ' + str(result)


def test_empty_singleton():
    # create a node chain and list by hand
    thenode = L.node('arbitrary')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    # check if is_empty() works
    result = not thellist.is_empty()
    assert result, 'is_empty() on singleton LList; returned ' + str(result)


def test_size_singleton():
    thenode = L.node('arbitrary')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    result = thellist.size()
    assert result == 1, 'size() on singleton LList; returned ' + str(result)


###############################################################################################
# UNIT TESTING - List.prepend()
###############################################################################################

def test_prepend_size_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._size
    assert result == 1, 'prepend(): check size after insertion on empty LList; returned ' + str(result)


def test_prepend_head_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._head
    assert result is not None, 'prepend() check head after insertion on empty LList; head not set correctly'


def test_prepend_tail_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._tail
    assert result is not None, 'prepend() check head after insertion on empty LList; tail not set correctly'


def test_prepend_refs_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._head
    assert result is thellist._tail, 'prepend() check head, tail after insertion on empty LList; head tail refs should be same but are not'


def test_prepend_data_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._head.data
    assert result is target, 'prepend() check data at head after insertion on empty LList; data set to ' + str(
        result) + ' but should be ' + "'" + str(target) + "'"


def test_prepend_data_2():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._tail.data
    assert result is target, 'prepend() check data at tail after insertion on empty LList; data set to ' + str(
        result) + ' but should be ' + "'" + str(target) + "'"


def test_prepend_end_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = thellist._head.next
    assert result is None, 'prepend() check node chain after insertion on empty LList: chain should end at one node, but next is not None!'


def test_prepend_empty_1():
    thellist = L.LList()
    target = 'one'
    thellist.prepend(target)
    result = not thellist.is_empty()
    assert result, 'prepend() check is_empty() after insertion on empty LList: is_empty() returned True'


###############################################################################################
# UNIT TESTING - List.prepend()
###############################################################################################

def test_prepend_size_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._size
    assert result == 2, 'prepend()  on LList with one node: size not set correctly'


def test_prepend_head_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._head
    assert result is not thenode, 'prepend()  on LList with one node: head not set correctly'


def test_prepend_tail_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._tail
    assert result is thenode, 'prepend()  on LList with one node: tail not set correctly'


def test_prepend_refs_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._head
    assert result != thellist._tail, 'prepend()  on LList with one node: head tail refs equal'


def test_prepend_data_3():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._head.data
    assert result == target, 'prepend()  on LList with one node: data not set correctly in head'


def test_prepend_chain_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._head.next
    assert result is not None, 'prepend()  on LList with one node: chain should not end at one node'


def test_prepend_chain_3():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._head.next
    assert result is thenode, 'prepend()  on LList with one node: new node should point to existing node'


def test_prepend_data_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist._tail.data
    assert result == tail_data, 'prepend()  on LList with one node: data not set correctly in tail'


def test_prepend_empty_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = not thellist.is_empty()
    assert result, 'prepend() on LList with one node; is_empty() returned True'


def test_prepend_size_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.prepend(target)
    result = thellist.size()
    assert result == 2, 'prepend()  on LList with one node: size() not returning correct value'


###############################################################################################
# UNIT TESTING - List.append()
###############################################################################################

def test_append_head_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._head
    assert result is not None, 'append() check head after insertion on empty LList: head not set correctly'


def test_append_tail_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._tail
    assert result is not None, 'append() check tail after insertion on empty LList: tail not set correctly'


def test_append_size_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._size
    assert result == 1, 'append() check size after insertion on empty LList: size not set correctly'


def test_append_refs_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._head
    assert result == thellist._tail, 'append() check head, tail after insertion on empty LList: head tail refs different'


def test_append_data_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._head.data
    assert result == target, 'append() check data at head after insertion on empty LList: data not set correctly in head'


def test_append_data_2():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._tail.data
    assert result == target, 'append() check data at tail after insertion on empty LList: data not set correctly in tail'


def test_append_chain_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist._head.next
    assert result is None, 'append() check node chain after insertion on empty LList: chain should end at one node'


def test_append_empty_1():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = not thellist.is_empty()
    assert result, 'append() check is_empty() after insertion on empty LList: is_empty() returned True'


def test_append_size_2():
    thellist = L.LList()
    target = 'three'
    thellist.append(target)
    result = thellist.size()
    assert result == 1, 'append() check size after insertion on empty LList: size() returned ' + str(result)


###############################################################################################
# UNIT TESTING - List.append()
###############################################################################################

def test_append_size_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._size
    assert result == 2, 'append() on LList with one node: size not set correctly'


def test_append_head_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._head
    assert result is thenode, 'append()  on LList with one node: head not set correctly'


def test_append_tail_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._tail
    assert result is not None, 'append()  on LList with one node: tail not set correctly'


def test_append_tail_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._tail
    assert result is not thenode, 'append()  on LList with one node: tail should be the new node, but is not'


def test_append_refs_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._head
    assert result != thellist._tail, 'append() on LList with one node: head tail refs equal, but should not'


def test_append_data_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._tail.data
    assert result == target, 'append() on LList with one node: data not set correctly in tail; should be ' + str(
        target) + 'but found ' + str(result)


def test_append_data_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._head.data
    assert result != target, 'append() on LList with one node: data not set correctly in head; should be ' + str(
        target) + 'but found ' + str(result)


def test_append_chain_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist._head.next
    assert result is not None, 'append() on LList with one node: chain ended at one node, but should not'


def test_append_empty_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = not thellist.is_empty()
    assert result, 'append() on LList with one node: is_empty() returned True but should not'


def test_append_size_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.append(target)
    result = thellist.size()
    assert result == 2, 'append() on LList with one node: size() returned ' + str(result)


###############################################################################################
# UNIT TESTING - List.get_index_of_value()
###############################################################################################

def test_get_index_of_value_empty_flag_1():
    thellist = L.LList()
    target = 9
    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is False, 'get_index_of_value() on empty LList; returned True but should not'


def test_get_index_of_value_empty_idx_1():
    thellist = L.LList()
    target = 9
    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result is None, 'get_index_of_value() on empty LList; returned index that is not None'


def test_get_index_of_value_notempty_flag_1():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'six'
    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is False, 'get_index_of_value() on singleton LList, target not present: returned True but should not'


def test_get_index_of_value_notempty_idx_1():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'six'
    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result is None, 'get_index_of_value() on singleton LList, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_2():
    target = '10'
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is True, 'get_index_of_value() on singleton LList, target present: returned False but should not'


def test_get_index_of_value_notempty_idx_2():
    target = '10'
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result == 0, 'get_index_of_value() on singleton LList, target present: returned index ' + str(
        result) + ', should be 0'


def test_get_index_of_value_notempty_flag_3():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is False, 'get_index_of_value() on LList with 2 nodes, target not present: returned True'


def test_get_index_of_value_notempty_idx_3():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result is None, 'get_index_of_value() on LList with 2 nodes, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_4():
    target = '10'
    thetail = L.node(target)
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in tail: returned False'


def test_get_index_of_value_notempty_idx_4():
    target = '10'
    thetail = L.node(target)
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result == 1, 'get_index_of_value() on LList with 2 nodes, target in tail: returned incorrect index ' + str(
        result)


def test_get_index_of_value_notempty_flag_5():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = flag
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in head: returned False'


def test_get_index_of_value_notempty_idx_5():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx
    assert result == 0, 'get_index_of_value() on LList with 2 nodes, target in head: returned incorrect index ' + str(
        result)


###############################################################################################
# UNIT TESTING - List.retrieve_data()
###############################################################################################

def test_retrieve_data_at_flag_1():
    thellist = L.LList()
    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = flag
    assert result is False, 'retrieve_data() on empty LList: returned True but should not'


def test_retrieve_data_at_val_1():
    thellist = L.LList()
    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = val
    assert result is None, 'retrieve_data() on empty LList: returned non-None value'


def test_retrieve_data_at_flag_2():
    target = 12
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = flag
    assert result is True, 'retrieve_data() on singleton LList, valid index; returned False but should not'


def test_retrieve_data_at_val_2():
    target = 12
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = val
    assert result == target, 'retrieve_data() on singleton LList, valid index; returned ' + str(
        result) + ' instead of ' + str(target)


def test_retrieve_data_at_flag_3():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = flag
    assert result is True, 'retrieve_data() on LList with two nodes, index 0: returned False but should not'


def test_retrieve_data_at_val_3():
    target = 18
    thetail = L.node(16)
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag, val = thellist.retrieve_data(idx)
    result = val
    assert result == target, 'retrieve_data(): on LList with two nodes, index 0; returned data value ' + str(
        result) + ' instead of ' + str(target)


def test_retrieve_data_at_flag_4():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag, val = thellist.retrieve_data(idx)
    result = flag
    assert result is True, 'retrieve_data(): on LList with two nodes, index 1: returned False but should not'


def test_retrieve_data_at_val_4():
    target = 16
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag, val = thellist.retrieve_data(idx)
    result = val
    assert result == target, 'retrieve_data(): on LList with two nodes, index 0; returned data value ' + str(
        result) + ' instead of ' + str(target)


def test_retrieve_data_at_flag_5():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag, val = thellist.retrieve_data(idx)
    result = flag
    assert result is False, 'retrieve_data(): on LList with two nodes, invalid positive index; returned True but should not'


def test_retrieve_data_at_val_5():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag, val = thellist.retrieve_data(idx)
    result = val
    assert result is None, 'retrieve_data(): on LList with two nodes, invalid positive index; returned non-None value'


###############################################################################################
# UNIT TESTING - List.set_data()
###############################################################################################

def test_set_data_empty():
    thellist = L.LList()
    idx = 0
    target = 23
    flag = thellist.set_data(idx, target)
    result = flag
    assert result is False, 'set_data() on empty LList; returned True but should not'


def test_set_data_notempty_flag_1():
    target = 23
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    idx = 0
    flag = thellist.set_data(idx, target)
    result = flag
    assert result is True, 'set_data() on singleton LList, valid index; returned False but should not'


def test_set_data_notempty_data_1():
    target = 23
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    idx = 0
    flag = thellist.set_data(idx, target)
    result = thellist._head.data
    assert result == target, 'set_data() on singleton LList, valid index; data not set correctly'


def test_set_data_notempty_flag_2():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag = thellist.set_data(idx, target)
    result = flag
    assert result is True, 'set_data() on LList with 2 nodes, index 0; returned False but should not'


def test_set_data_notempty_data_2():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag = thellist.set_data(idx, target)
    result = thellist._head.data
    assert result == target, 'set_data() on LList with 2 nodes, index 0; data not set correctly'


def test_set_data_notempty_flag_3():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag = thellist.set_data(idx, target)
    result = flag
    assert result is True, 'set_data() on LList with 2 nodes, index 1; returned False but should not'


def test_set_data_notempty_data_3():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag = thellist.set_data(idx, target)
    result = thellist._tail.data
    assert result == target, 'set_data() on LList with 2 nodes, index 1; data not set correctly'


def test_set_data_notempty_flag_4():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data(idx, target)
    result = flag
    assert result is False, 'set_data() on LList with 2 nodes, invalid positive index; returned True but should not'


def test_set_data_notempty_data_4():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data(idx, target)
    result = thellist._head.data
    assert result == 'not the target', 'set_data() on LList with 2 nodes, invalid positive index; data at head changed incorrectly'


def test_set_data_notempty_data_5():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data(idx, target)
    result = thellist._tail.data
    assert result == 'not the target', 'set_data() on LList with 2 nodes, invalid positive index; data at tail changed incorrectly'


###############################################################################################
# UNIT TESTING - List.remove_from_front()
###############################################################################################

def test_remove_from_front_empty_1():
    thellist = L.LList()
    flag, val = thellist.remove_from_front()
    result = flag
    assert result is False, 'remove_from_front() on empty LList: returned True but should not'


def test_remove_from_front_empty_2():
    thellist = L.LList()
    flag, val = thellist.remove_from_front()
    result = val
    assert result is None, 'remove_from_front() on empty LList: returned non-None value'


def test_remove_from_front_singleton_in_flag_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = flag
    assert result is True, 'remove_from_front() on singleton LList: returned False but should not'


def test_remove_from_front_singleton_in_val_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = val
    assert result == target, 'remove_from_front() on singleton LList: returned ' + str(result) + ' instead of ' + str(
        target)


def test_remove_from_front_singleton_in_size_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._size
    assert result == 0, 'remove_from_front() on singleton LList: incorrect size'


def test_remove_from_front_singleton_in_ref_head_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._head
    assert result is None, 'remove_from_front() on singleton LList: head set incorrectly; should be None'


def test_remove_from_front_singleton_in_ref_tail_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._tail
    assert result is None, 'remove_from_front() on singleton LList: tail set incorrectly; should be None'


def test_remove_from_front_notempty_in_flag_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = flag
    assert result is True, 'remove_from_front() on LList with 2 nodes; returned False but should not'


def test_remove_from_front_notempty_in_val_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = val
    assert result == target, 'remove_from_front() on LList with 2 nodes; returned ' + str(
        result) + ' instead of ' + str(target)


def test_remove_from_front_notempty_in_size_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = thellist._size
    assert result == 1, 'remove_from_front() on LList with 2 nodes; set incorrect size'


def test_remove_from_front_notempty_in_ref_head_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_front()
    result = thellist._head
    assert result is thetail, 'remove_from_front() on LList with 2 nodes; head should be same as tail'


def test_remove_from_front_notempty_in_ref_tail_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_front()
    result = thellist._tail
    assert result is thetail, 'remove_from_front() on LList with 2 nodes; tail should not have changed'


###############################################################################################
# UNIT TESTING - List.remove_from_back()
###############################################################################################

def test_remove_from_back_empty_flag():
    thellist = L.LList()
    flag, val = thellist.remove_from_back()
    result = flag
    assert result is False, 'remove_from_back(): returned True for empty list'


def test_remove_from_back_empty_val():
    thellist = L.LList()
    flag, val = thellist.remove_from_back()
    result = val
    assert result is None, 'remove_from_back(): returned non-None value for empty list'


def test_remove_from_back_singleton_flag():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = flag
    assert result is True, 'remove_from_back():  returned False for singleton list'


def test_remove_from_back_singleton_val():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = val
    assert result == target, 'remove_from_back():  returned incorrect value for singleton list'


def test_remove_from_back_singleton_size():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._size
    assert result == 0, 'remove_from_back():  set incorrect size for singleton list'


def test_remove_from_back_singleton_in_ref_head_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._head
    assert result is None, 'remove_from_back() on singleton LList: head set incorrectly; should be None'


def test_remove_from_back_singleton_in_ref_tail_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._tail
    assert result is None, 'remove_from_back() on singleton LList: tail set incorrectly; should be None'


def test_remove_from_back_multiple_flag():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = flag
    assert result is True, 'remove_from_back():  returned False for list size 2'


def test_remove_from_back_multiple_val():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = val
    assert result == target, 'remove_from_back():  returned incorrect value for list size 2'


def test_remove_from_back_multiple_size():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = thellist._size
    assert result == 1, 'remove_from_back():  set incorrect size for list size 2'


def test_remove_from_back_multiple_in_ref_head_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_back()
    result = thellist._head
    assert result is thehead, 'remove_from_back() on LList with 2 nodes; head should not have changed'


def test_remove_from_back_multiple_in_ref_tail_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_back()
    result = thellist._tail
    assert result is thehead, 'remove_from_back() on LList with 2 nodes; tail should be the same as head'


###############################################################################################
# INTEGRATION TESTING
###############################################################################################

###############################################################################################
# check if all the operations work after a bunch of data is added using append()
#

def test_integration_append_is_empty():
    # an integration test tests how operations work together
    # first set up a list with a bunch of nodes in the node chain

    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)

    # now check if a single aspect worked properly
    result = thellist.is_empty()
    assert result is False, "checking is_empty() after append(); returned True!"


def test_integration_append_size():
    # identical set up
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)

    # check different aspect
    assert thellist.size() == 7, "should have size 7"


def test_integration_append_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.get_index_of_value("HEY") == (True, 0), "HEY is at index zero"


def test_integration_append_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.get_index_of_value("TURTLE") == (True, 6), "TURTLE is at index 6"


def test_integration_append_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 4), "DOING-DOING is at index 4"


def test_integration_append_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.get_index_of_value("GLOBE") == (False, None), "GLOBE Not in llist"


def test_integration_append_retrieve_data_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.retrieve_data(6) == (True, "TURTLE"), "TURTLE is at index 6"


def test_integration_append_retrieve_data_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.retrieve_data(0) == (True, "HEY"), "HEY is at index 0"


def test_integration_append_retrieve_data_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.retrieve_data(2) == (True, "THANK-YOU"), "THANK-YOU is at index 2"


def test_integration_append_retrieve_data_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.retrieve_data(7) == (False, None), "index not valid"


###############################################################################################
# check if all the operations work after a bunch of data is added using prepend()
#

def test_integration_prepend_is_empty():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.is_empty() is False, "should not be empty"


def test_integration_prepend_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.size() == 7, "should have size 7"


def test_integration_prepend_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.get_index_of_value("HEY") == (True, 6), "HEY is at index 6"


def test_integration_prepend_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.get_index_of_value("TURTLE") == (True, 0), "TURTLE is at index 0"


def test_integration_prepend_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 2), "DOING-DOING is at index 2"


def test_integration_prepend_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.get_index_of_value("GLOBE") == (False, None), "GLOBE Not in llist"


def test_integration_prepend_retrieve_data_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.retrieve_data(0) == (True, "TURTLE"), "TURTLE is at index 0"


def test_integration_prepend_retrieve_data_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.retrieve_data(6) == (True, "HEY"), "HEY is at index 6"


def test_integration_prepend_retrieve_data_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.retrieve_data(3) == (True, "TURN-AROUND"), "TURN-AROUND is at index 3"


def test_integration_prepend_retrieve_data_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    assert thellist.retrieve_data(7) == (False, None), "index not valid"


###############################################################################################
# check what happens if you change the data in the Llist using set_data()

def test_integration_set_data_check_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.set_data(0, "now") is True, "index valid"


def test_integration_set_data_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(0, "now")
    assert thellist.get_index_of_value("HEY") == (False, None), "'HEY' should be gone"


def test_integration_set_data_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(0, "now")
    assert thellist.get_index_of_value("now") == (True, 0), "'now' should be at index 0"


def test_integration_set_data_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(0, "now")
    assert thellist.get_index_of_value("STOPSIGN") == (True, 1), "'STOPSIGN' should be still at index 1"


def test_integration_set_data_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(0, "now")
    assert thellist.get_index_of_value("TURTLE") == (True, 6), "'TURTLE' should be still at index 6"


def test_integration_set_data_size_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(0, "now")
    assert thellist.size() == 7, "should have size 7"


def test_integration_set_data_get_index_of_check_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.set_data(6, "SIGN") is True, "index valid"


def test_integration_set_data_get_index_of_value_5():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(6, "SIGN")
    assert thellist.get_index_of_value("TURTLE") == (False, None), "TURTLE should be gone"


def test_integration_set_data_get_index_of_value_6():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(6, "SIGN")
    assert thellist.get_index_of_value("SIGN") == (True, 6), ": SIGN is at index 6"


def test_integration_set_data_get_index_of_value_7():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(6, "SIGN")
    assert thellist.get_index_of_value("HEY") == (True, 0), "HEY is still at index 0"


def test_integration_set_data_get_index_of_value_8():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(6, "SIGN")
    assert thellist.get_index_of_value("HORSESHOE") == (True, 5), "HORSESHOE is still at index 5"


def test_integration_set_data_get_index_of_size_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(6, "SIGN")
    assert thellist.size() == 7, "should have size 7"


def test_integration_set_data_get_index_of_check_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    assert thellist.set_data(3, "FOLLOWER") is True, ": index valid"


def test_integration_set_data_get_index_of_value_9():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(3, "FOLLOWER")
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_set_data_get_index_of_value_10():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(3, "FOLLOWER")
    assert thellist.get_index_of_value("FOLLOWER") == (True, 3), "FOLLOWER is at index 3"


def test_integration_set_data_get_index_of_size_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    thellist.set_data(3, "FOLLOWER")
    assert thellist.size() == 7, "should have size 7"


###############################################################################################
# check what happens when you add and remove a bunch from the back

def test_integration_remove_from_back_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.size() == 3, "should have size 3"


def test_integration_remove_from_back_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_back_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.get_index_of_value("THANK-YOU") == (True, 2), "THANK-YOU should be at index 2"


def test_integration_remove_from_back_retrieve_data_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.retrieve_data(2) == (True, "THANK-YOU"), "THANK-YOU is at index 2"


###############################################################################################
# check what happens when you add and remove a bunch from the front

def test_integration_remove_from_front_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.size() == 3, "should have size 3"


def test_integration_remove_from_front_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_front_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.get_index_of_value("THANK-YOU") == (True, 0), "THANK-YOU should be at index 0"


def test_integration_remove_from_front_retrieve_data_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.prepend(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.retrieve_data(0) == (True, "THANK-YOU"), "THANK-YOU is at index 0"


# a list of references to the functions defined above
all_of_em = [
    test_create_initial_size,
    test_create_initial_head,
    test_create_initial_tail,
    test_empty_empty,
    test_empty_singleton,
    test_size_singleton,
    test_prepend_size_1,
    test_prepend_head_1,
    test_prepend_tail_1,
    test_prepend_refs_1,
    test_prepend_data_1,
    test_prepend_data_2,
    test_prepend_end_1,
    test_prepend_empty_1,
    test_prepend_size_2,
    test_prepend_head_2,
    test_prepend_tail_2,
    test_prepend_refs_2,
    test_prepend_data_3,
    test_prepend_chain_2,
    test_prepend_chain_3,
    test_prepend_data_4,
    test_prepend_empty_2,
    test_prepend_size_3,
    test_append_head_1,
    test_append_tail_1,
    test_append_size_1,
    test_append_refs_1,
    test_append_data_1,
    test_append_data_2,
    test_append_chain_1,
    test_append_empty_1,
    test_append_size_2,
    test_append_size_3,
    test_append_head_2,
    test_append_tail_2,
    test_append_tail_3,
    test_append_refs_2,
    test_append_data_3,
    test_append_data_4,
    test_append_chain_2,
    test_append_empty_2,
    test_append_size_4,
    test_get_index_of_value_empty_flag_1,
    test_get_index_of_value_empty_idx_1,
    test_get_index_of_value_notempty_flag_1,
    test_get_index_of_value_notempty_idx_1,
    test_get_index_of_value_notempty_flag_2,
    test_get_index_of_value_notempty_idx_2,
    test_get_index_of_value_notempty_flag_3,
    test_get_index_of_value_notempty_idx_3,
    test_get_index_of_value_notempty_flag_4,
    test_get_index_of_value_notempty_idx_4,
    test_get_index_of_value_notempty_flag_5,
    test_get_index_of_value_notempty_idx_5,
    test_retrieve_data_at_flag_1,
    test_retrieve_data_at_val_1,
    test_retrieve_data_at_flag_2,
    test_retrieve_data_at_val_2,
    test_retrieve_data_at_flag_3,
    test_retrieve_data_at_val_3,
    test_retrieve_data_at_flag_4,
    test_retrieve_data_at_val_4,
    test_retrieve_data_at_flag_5,
    test_retrieve_data_at_val_5,
    test_set_data_empty,
    test_set_data_notempty_flag_1,
    test_set_data_notempty_data_1,
    test_set_data_notempty_flag_2,
    test_set_data_notempty_data_2,
    test_set_data_notempty_flag_3,
    test_set_data_notempty_data_3,
    test_set_data_notempty_flag_4,
    test_set_data_notempty_data_4,
    test_set_data_notempty_data_5,
    test_remove_from_front_empty_1,
    test_remove_from_front_empty_2,
    test_remove_from_front_singleton_in_flag_1,
    test_remove_from_front_singleton_in_val_1,
    test_remove_from_front_singleton_in_size_1,
    test_remove_from_front_singleton_in_ref_head_1,
    test_remove_from_front_singleton_in_ref_tail_1,
    test_remove_from_front_notempty_in_flag_2,
    test_remove_from_front_notempty_in_val_2,
    test_remove_from_front_notempty_in_size_2,
    test_remove_from_front_notempty_in_ref_head_2,
    test_remove_from_front_notempty_in_ref_tail_2,
    test_remove_from_back_empty_flag,
    test_remove_from_back_empty_val,
    test_remove_from_back_singleton_flag,
    test_remove_from_back_singleton_val,
    test_remove_from_back_singleton_size,
    test_remove_from_back_singleton_in_ref_head_1,
    test_remove_from_back_singleton_in_ref_tail_1,
    test_remove_from_back_multiple_flag,
    test_remove_from_back_multiple_val,
    test_remove_from_back_multiple_size,
    test_remove_from_back_multiple_in_ref_head_2,
    test_remove_from_back_multiple_in_ref_tail_2,
    test_integration_append_is_empty,
    test_integration_append_size,
    test_integration_append_get_index_of_value_1,
    test_integration_append_get_index_of_value_2,
    test_integration_append_get_index_of_value_3,
    test_integration_append_get_index_of_value_4,
    test_integration_append_retrieve_data_1,
    test_integration_append_retrieve_data_2,
    test_integration_append_retrieve_data_3,
    test_integration_append_retrieve_data_4,
    test_integration_prepend_is_empty,
    test_integration_prepend_size,
    test_integration_prepend_get_index_of_value_1,
    test_integration_prepend_get_index_of_value_2,
    test_integration_prepend_get_index_of_value_3,
    test_integration_prepend_get_index_of_value_4,
    test_integration_prepend_retrieve_data_1,
    test_integration_prepend_retrieve_data_2,
    test_integration_prepend_retrieve_data_3,
    test_integration_prepend_retrieve_data_4,
    test_integration_set_data_check_1,
    test_integration_set_data_get_index_of_value_1,
    test_integration_set_data_get_index_of_value_2,
    test_integration_set_data_get_index_of_value_3,
    test_integration_set_data_get_index_of_value_4,
    test_integration_set_data_size_1,
    test_integration_set_data_get_index_of_check_2,
    test_integration_set_data_get_index_of_value_5,
    test_integration_set_data_get_index_of_value_6,
    test_integration_set_data_get_index_of_value_7,
    test_integration_set_data_get_index_of_value_8,
    test_integration_set_data_get_index_of_size_2,
    test_integration_set_data_get_index_of_check_3,
    test_integration_set_data_get_index_of_value_9,
    test_integration_set_data_get_index_of_value_10,
    test_integration_set_data_get_index_of_size_3,
    test_integration_remove_from_back_size,
    test_integration_remove_from_back_get_index_of_value_1,
    test_integration_remove_from_back_get_index_of_value_2,
    test_integration_remove_from_back_retrieve_data_1,
    test_integration_remove_from_front_size,
    test_integration_remove_from_front_get_index_of_value_1,
    test_integration_remove_from_front_get_index_of_value_2,
    test_integration_remove_from_front_retrieve_data_1
]

runemall()

