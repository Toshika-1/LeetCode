# Intuition
Suppose in a subarray:
t=count(target)
o=count(other)

Then:   length = t + o
and the condition becomes:  t > o
because:    2t > t + o
The sum of the transformed array over the subarray is:  t - o
Therefore:  target is majority  ⇔   subarray sum > 0

sum(l...r)=pref[r+1]-pref[l]
we need, pref[r+1]-pref[l]>0    =>  pref[r+1]>pref[l]

so the problem becomes  =>  find (i,j) pairs with i<j and pref[j]>pref[i]

# Approach

### @1
count smaller prefix ex, prefix= 1 0 1 0 2
for 2, previous contributors are 1 0 1 0 => 4
for 1, it's 0 => 1
this is what fenwick tree is being used for

### @2
map coordinates:
prefix sums can be negative : 0 -2 -1 1
so we map them to positive indexs (fenwick tree uses 1-indexed array)
sort : -2 -1 0 1
map: -2:0, -1:1, 0:2, 1:3

### @3
SO THE PROBLEM CAN BE REFRAMED AS:  Count ordered pairs of prefix sums.

# Complexity
- Time complexity:  O(n log n)

- Space complexity: O(n)