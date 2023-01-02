package segmenttree_test

import (
	"fmt"
	"math/rand"
	"strconv"
	"testing"
	"time"

	st "github.com/cjcjcj/algo/go/algo/segmenttree"
)

func BenchmarkRecursiveBuild(b *testing.B) {
	rand.Seed(time.Now().Unix())

	benchmarks := []struct {
		size int
	}{
		{2},
		{17},
		{15},
		{10},
		{1000},
		{10000},
		{100000},
		{1000000},
	}
	for _, bm := range benchmarks {
		nums := rand.Perm(bm.size)
		name := strconv.Itoa(bm.size)

		b.Run(name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				st.NewSTR(nums, sum)
			}
		})
	}
}

func BenchmarkRecursiveUpdate(b *testing.B) {
	rand.Seed(time.Now().Unix())

	benchmarks := []struct {
		size int
	}{
		{2},
		{17},
		{15},
		{10},
		{1000},
		{10000},
		{100000},
		{1000000},
	}
	for _, bm := range benchmarks {
		nums := rand.Perm(bm.size)
		name := strconv.Itoa(bm.size)
		s := st.NewSTR(nums, sum)

		b.Run(name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				s.Update(rand.Intn(bm.size), rand.Int())
			}
		})
	}
}

func BenchmarkRecursiveQuery(b *testing.B) {
	rand.Seed(time.Now().Unix())

	benchmarks := []struct {
		size int
		l, r int
	}{
		{2, 0, 1},
		{2, 0, 0},

		{17, 0, 16},
		{17, 5, 16},
		{17, 0, 9},
		{17, 15, 16},
		{17, 5, 10},

		{15, 0, 14},
		{15, 4, 14},
		{15, 0, 8},
		{15, 13, 14},
		{15, 2, 11},

		{10, 0, 9},
		{10, 2, 9},
		{10, 0, 6},
		{10, 8, 9},
		{10, 2, 7},

		{1000, 0, 999},
		{1000, 20, 999},
		{1000, 490, 520},
		{1000, 490, 495},
		{1000, 998, 999},

		{10000, 0, 9999},
		{10000, 200, 9999},
		{10000, 4900, 5200},
		{10000, 4900, 4950},
		{10000, 9998, 9999},

		{100000, 0, 99999},
		{100000, 200, 99999},
		{100000, 49000, 52000},
		{100000, 49000, 49500},
		{100000, 99998, 99999},

		{1000000, 00, 999999},
		{1000000, 2000, 999999},
		{1000000, 490000, 520000},
		{1000000, 490000, 495000},
		{1000000, 999998, 999999},
	}
	for _, bm := range benchmarks {
		nums := rand.Perm(bm.size)
		name := fmt.Sprintf("%d-[%d-%d]", bm.size, bm.l, bm.r)
		s := st.NewSTR(nums, sum)

		b.Run(name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				s.Query(bm.l, bm.r)
			}
		})
	}
}
