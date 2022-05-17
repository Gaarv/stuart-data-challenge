from geo_transformer.trie import Trie


def test_insert_in_trie():
    trie = Trie()
    words = ["ab", "bc", "ac"]
    for word in words:
        trie.insert(word)

    root_children = sorted(list(trie.root.children.keys()))
    a_children = sorted(list(trie.root.children["a"].children.keys()))
    b_children = sorted(list(trie.root.children["b"].children.keys()))

    assert root_children == ["a", "b"]
    assert a_children == ["b", "c"]
    assert b_children == ["c"]


def test_search_in_trie_existing_path():
    trie = Trie()
    words = ["whatever", "whenever", "wherever"]
    for word in words:
        trie.insert(word)
    path = trie.search("whenever")
    path = [node.char for node in path]
    assert path == ["w", "h", "e", "n", "e", "v", "e", "r"]


def test_search_in_trie_partial_existing_path():
    trie = Trie()
    words = ["whatever", "whenever", "wherever"]
    for word in words:
        trie.insert(word)
    path = trie.search("whocares")
    path = [node.char for node in path]
    assert path == ["w", "h"]


def test_search_in_trie_empty_path():
    trie = Trie()
    words = ["whatever", "whenever", "wherever"]
    for word in words:
        trie.insert(word)
    path = trie.search("null")
    path = [node.char for node in path]
    assert path == []
