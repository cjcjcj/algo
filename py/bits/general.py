x: int
k: int


x & -(1<<k)     # set k'th bit to '0'
x | (1<<k)      # set k'th bit to '1'
x ^ (1<<k)      # invert k'th bit

x & (x-1)       # set last bit to '0'
x & -x          # set all '1' to '0' except last one

x & (1 << k)        # is k'th bit '1'
x & (x-1) == 0      # is power of 2


(x<<1) | 1          # 2x+1
x & 1               # is odd
x^1                 # 2x -> 2x+1; 2x+1 -> 2x

x - (x>>1)          # ⌈x/2⌉
k >> 1              # ⌊x/2⌋
