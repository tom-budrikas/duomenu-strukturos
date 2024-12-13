from LinkedList import LinkedList

def test_insert_start(data):
    LinkedList([data], "insert_start")

def test_insert_end(data):
    LinkedList([data], "insert_end")

def test_insert_node(linked_list, index):
    linked_list.insertNodeIndex(index, 1)

def test_find_node(linked_list, index):
    linked_list.getNodeAtIndex(index)

def test_delete_node(linked_list, index):
    linked_list.removeNodeAtIndex(index)

def test_print_nodes(linked_list):
    linked_list.printList()