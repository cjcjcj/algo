package trie

type Trie struct {
	trie map[rune]*Trie
	end  bool
}

func NewTrie() *Trie {
	trie := new(Trie)
	trie.trie = make(map[rune]*Trie)
	trie.end = false

	return trie
}

func (t *Trie) Insert(word string) {
	node := t
	for _, w := range word {
		nextNode, ok := node.trie[w]
		if !ok {
			nextNode = NewTrie()
			node.trie[w] = nextNode
		}
		node = nextNode
	}
	node.end = true
}

func (t *Trie) drill(word string) (*Trie, bool) {
	node, ok := t, false
	for _, w := range word {
		node, ok = node.trie[w]
		if !ok {
			return node, false
		}
	}
	return node, true
}

func (t *Trie) Search(word string) bool {
	if node, ok := t.drill(word); ok && node.end {
		return true
	}
	return false
}

func (t *Trie) SearchPrefix(word string) bool {
	_, ok := t.drill(word)
	return ok
}
