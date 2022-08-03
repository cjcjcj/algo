package trie

const aLPHABET_SIZE = 26

type childrenT = [aLPHABET_SIZE]*TrieAlphabet

type TrieAlphabet struct {
	trie childrenT
	end  bool
}

func NewTrieAlphabet() *TrieAlphabet {
	trie := new(TrieAlphabet)
	trie.end = false

	return trie
}

func (t *TrieAlphabet) Insert(word string) {
	var nextNode *TrieAlphabet
	node := t
	for _, w := range word {
		nextNode = node.trie[w-'a']
		if nextNode == nil {
			nextNode = NewTrieAlphabet()
			node.trie[w-'a'] = nextNode
		}
		node = nextNode
	}
	node.end = true
}

func (t *TrieAlphabet) Search(word string) bool {
	node := t
	for _, w := range word {
		node = node.trie[w-'a']
		if node == nil {
			return false
		}
	}
	return node.end
}

func (t *TrieAlphabet) SearchPrefix(word string) bool {
	node := t
	for _, w := range word {
		node = node.trie[w-'a']
		if node == nil {
			return false
		}
	}
	return true
}
