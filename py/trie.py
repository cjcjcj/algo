WORD_END = 1


def build_trie(*words: list[str]) -> dict:
    trie = dict()

    for word in words:
        node = trie
        for c in word:
            node = node.setdefault(c, dict())
        node[WORD_END] = WORD_END

    return trie
