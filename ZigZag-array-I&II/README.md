## in DP with memo solution we are recomputing the number of possibles arrays multiple time. This computation is in O(2*M).
## This can be optimised by using range sum query, prefix arrays
# dp(i, p, 1) = Σ dp(i+1, v, 0)
#              v < p

# dp(i, p, 0) = Σ dp(i+1, v, 1)
#              v > p

## to compute
# dp(i,p,1)

# using prefix sums, we need: prefix_down

# for the entire row:

# dp(i+1,0,0)
# dp(i+1,1,0)
# ...
# dp(i+1,m-1,0)

# So before computing a single state of row i, you need all states of row i+1.

# this is where recursion naturally turns into tabulation.