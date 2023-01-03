VALUE = 111


def build(words: list) -> dict:
    tree = dict()
    for word in words:
        node = tree
        for c in word:
            node = node.setdefault(c, dict())
        node[VALUE] = word
    return tree


def search(tree, word, errors_k=0, *, i=0) -> list:
    if not tree or i > len(word) or errors_k < 0:
        return []

    res = []
    if i == len(word):
        if VALUE in tree:
            res.append(tree[VALUE])
        return res

    for k, v in tree.items():
        if k == VALUE: continue  # fmt: skip

        k_res = search(v, word, errors_k - (k != word[i]), i=i+1)
        res.extend(k_res)

    return res


def search(tree, word, errors_k: int = 0) -> list:
    st = [(tree, errors_k, 0)]
    res = []

    while st:
        node, cur_err, i = st.pop()
        if i == len(word):
            if VALUE in node:
                res.append(node[VALUE])
            continue

        for k, v in node.items():
            if k == VALUE: continue

            next_err = cur_err - (k != word[i])
            if next_err >= 0:
                st.append((v, next_err, i + 1))
    return res
