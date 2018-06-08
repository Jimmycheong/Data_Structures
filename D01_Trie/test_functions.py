from main import Node
from functions import create_root_node, add_word_to_trie, find_prefix

def test_add_word_to_trie():
	root = create_root_node()

	add_word_to_trie(root, "hello")

	child_1 = root.children[0]
	assert child_1.letter == "h"

	child_2 = child_1.children[0]
	assert child_2.letter == "e"

def test_find_prefix():
	root, child_1, child_2, child_3 = Node("*"), Node("A"), Node("B"), Node("C")

	root.children = [child_1]
	child_1.children = [child_2]
	child_2.children = [child_3]

	is_found = find_prefix(root, "ABC")

	assert is_found == True
