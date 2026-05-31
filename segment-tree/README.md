# Block Placement Queries

## Idea
Maintain:
- sorted boundaries
- segment tree storing maximum gap ending at each boundary

## Key Insight
gap[r] = r - previous_boundary

This converts interval checks into range maximum queries.

## Complexity
- Update: O(log n)
- Query: O(log n)

p[i] -> position of nearest obstacle to the left of i
d[i]=i-p[i] -> length of maximum blank interval ending at position i
maximum value of d[i] in interval [o,x] is at least sz
d[r] -> distance to nearest obstacle on left
maintain d array dynamically.
pre and nxt ->nearest object on left and right
insert obstacle @ x -> update d[x] and d[nxt]
[0,pre] -> consists of complete intervals -> directly using segment tree
[pre, x] -> handled seperately by comp. length with sz
to maintain ordered structure storing obstacles on both sides of x
during insertion -> use balanced binary search tree