WORD_END = 1


def build_trie(*words: list[str]) -> dict:
    trie = dict()

    for word in words:
        node = trie
        for c in word:
            node = node.setdefault(c, dict())
        node[WORD_END] = WORD_END

    return trie


def _traverse(trie: dict, word: str) -> dict:
    node = trie
    for c in word:
        node = node.get(c, dict())
        if not node:
            return node
    return node


def is_in(trie: dict, word: str) -> bool:
    return WORD_END in _traverse(trie, word)


def is_prefix_in(trie, prefix: str) -> bool:
    return bool(_traverse(trie, prefix))
