from typing import Dict, List


class TrieNode:
    """
    A node in a Trie. Contains a character and a dictionary of children nodes.
    """

    def __init__(self, char: str):
        self.char = char
        self.children: Dict[str, TrieNode] = {}

    @property
    def is_leaf(self) -> bool:
        return any(self.children)


class Trie:
    """
    A Trie is a tree data structure that stores a set of strings. See https://en.wikipedia.org/wiki/Trie.
    """

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, s: str) -> None:
        """Insert a given string into the Trie.

        Args:
            s (str): the string to insert
        """
        current_node = self.root
        for char in s:
            if char not in current_node.children:
                child = TrieNode(char)
                current_node.children[char] = child
                current_node = child
            else:
                current_node = current_node.children[char]

    def search(self, s: str) -> List[TrieNode]:
        """Search for a given string in the Trie.

        Args:
            s (str): string to search

        Returns:
            List[TrieNode]: list of TrieNodes corresponding to the path of the string in the Trie.
            If an exact match is not found, returns the partial path or an empty list if no match is found.
        """
        path = []
        node = self.root
        for char in s:
            node = node.children.get(char)
            if node:
                path.append(node)
            else:
                break
        return path
