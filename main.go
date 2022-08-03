package main

import (
	"fmt"

	"example.com/go-algo/go/algo/trie"
)

func main() {
	trier := trie.NewTrie()
	// trier := trie.NewTrieAlphabet()
	for _, word := range []string{"apple", "app", "lemon"} {
		trier.Insert(word)
	}
	fmt.Println("********word search********")
	for _, word := range []string{"app", "apple", "ape", "orange"} {
		fmt.Println(word, trier.Search(word))
	}
	fmt.Println("\n********prefix search********")
	for _, word := range []string{"ap", "lemo", "o"} {
		fmt.Println(word, trier.SearchPrefix(word))
	}
}
