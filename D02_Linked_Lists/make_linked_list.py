''' make_linked_list.py

'''

from Node import Node
from functions import find_length_of_linked_list

node_1 = Node("hello")
node_2 = Node("there")
node_3 = Node("neighbour")
node_4 = Node("I'm")
node_5 = Node("fine")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
node_4.next_node = node_5

length_of_LL = find_length_of_linked_list(node_1)

print(f"length of LL: {length_of_LL}")
