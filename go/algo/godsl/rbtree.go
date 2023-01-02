package godsl

import (
	"github.com/emirpasic/gods/sets/treeset"
)

type NumberContainers struct {
	byIndex       map[int]int
	numberIndexes map[int]*treeset.Set
}

func Constructor() NumberContainers {
	return NumberContainers{
		byIndex:       make(map[int]int),
		numberIndexes: make(map[int]*treeset.Set),
	}
}

func (this *NumberContainers) Change(index int, number int) {
	if storedN, ok := this.byIndex[index]; ok && number != storedN {
		this.numberIndexes[storedN].Remove(index)
	}

	if _, ok := this.numberIndexes[number]; !ok {
		this.numberIndexes[number] = treeset.NewWithIntComparator()
	}
	this.numberIndexes[number].Add(index)
	this.byIndex[index] = number
}

func (this *NumberContainers) Find(number int) int {
	if v, ok := this.numberIndexes[number]; ok {
		iter := v.Iterator()
		if iter.Next() {
			return iter.Value().(int)
		}
	}
	return -1
}
