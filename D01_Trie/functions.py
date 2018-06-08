from typing import List
from main import Node

def create_root_node():
    '''
    Create a root node representing the root node of a trie

    Returns:
        Node: an Node instance containing representing an empty Trie

    '''
    return Node("*")

def check_children_letters(list_: List[Node]):
    '''
    Returns a list of strings representing the letters for each child node in the list passed in

    Args: 
        list_(List[Node]): 

    Returns:
        A list of characters for each Node
    '''

    return list(map(lambda s: s.letter, list_))

def get_child_node(parent: Node, char: str) -> Node:

    '''
    TODO: Finish definition
    '''

    filtered = list(filter(lambda s: s.letter == char , parent.children))
    return filtered[0]

def add_word_to_trie(node: Node, word: str):

    '''     
    TODO: 

    Search through each character of the word and check if
    it exists in the trie
    
    '''

    for char in word: 
        children_letters = check_children_letters(node.children)
        if char not in children_letters:
            node.children += [Node(char)]
        child_node = get_child_node(node, char)
        node = child_node 

def find_prefix(root, prefix: str): 
    
    '''
    TODO: 
    '''

    node = root 
    for char in prefix:         
        print(f"list of children: {check_children_letters(node.children)}")
        if char not in check_children_letters(node.children):
            print(f"not found at char: {char}")
            return False 
        node = get_child_node(node, char)
    print("found!")
    return True