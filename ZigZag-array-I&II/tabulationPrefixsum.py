from itertools import accumulate
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod=10**9+7
        m=r-l+1
        dp0=[1]*m
        dp1=[1]*m
        for _ in range(n-1):
            sum0=list(accumulate(dp0, initial=0))
            sum1=list(accumulate(dp1, initial=0))
            dp0=[x % mod for x in sum1[:-1]]
            s0_m=sum0[-1]
            dp1=[(s0_m-x)% mod for x in sum0[1:]]
        return (sum(dp0)+sum(dp1))%mod
        