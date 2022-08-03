package algo


func max(a,b int) int {
    if a > b {
        return a
    }
    return b
}


type Solution struct {
    nums []int
    multipliers []int

    dp [][]int
}

func NewStruct(nums []int, multipliers []int) *Solution {
    dp := make([][]int, len(multipliers))
    for i := range multipliers {
        dp[i] = make([]int, len(multipliers))
    }
    return &Solution{nums, multipliers, dp}
}

func (self *Solution) top_down(i, left int) int {
    if i == len(multipliers) {
        return 0
    }

    if self.dp[i][left] == 0 {
        right := len(self.nums) - 1 - (left + i)
        self.dp[i][left] = max(
            self.nums[left] * self.multipliers[i] + self.top_down(i+1, left+1),
            self.nums[right] * self.multipliers[i] + self.top_down(i+1, left)
        )
    }
    return self.dp[i][left]
}

func maximumScore(nums []int, multipliers []int) int {
    s := NewStruct(nums, multipliers)
    return s.top_down(0, 0)
}