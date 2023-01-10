# ops
a: int
b: int


a & b       # a ∩ b; intersection
a | b       # a ∪ b; union
a & (-b)    # a \ b; difference


# iteration
n: int
k: int

# subsets of {0, ..., n-1}
for i in range(1<<n):
    ...

# subsets w/ k elements
for i in range(1<<n):
    if bin(i).count('1') == k: ...

# subsets of x:
x: int
b = 0
while True:
    ...
    b = (b-x) & x
    if not b: break
