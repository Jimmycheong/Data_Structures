'''functions.py

A file containing functions used in the creation and usage of a linked list

'''

from Node import Node

def find_length_of_linked_list(head: Node) -> int:
    
    '''
    Finds the length of a linked list by recursively iterating through each node.
    
    Params: 
        head (Node): The head node of a linked list

    Returns: 
        length_of_list (int): The length of the linked list

    '''

    completed = False

    node = head
    length_of_list = 1
    while(node.next_node != None):
        length_of_list += 1
        node = node.next_node

    return length_of_list

def insert_node_into_linked_list(head: Node, new_node: Node, index: int):
    '''
    Inserts a new node containing information at certain index

    TODO: !!!
    '''

