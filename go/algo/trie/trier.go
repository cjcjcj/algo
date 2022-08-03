package trie

type Trier interface {
	Insert(word string)
	Search(word string) bool
	SearchPrefix(word string) bool
}
