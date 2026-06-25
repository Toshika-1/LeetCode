class Solution(object):
    def zigZagArrays(self, n, l, r):
        mod=10**9+7
        m=r-l+1
        #1-> means increasing
        #0-> means decreasing
        memo=[[[-1]*2 for _ in range(m)] for _ in range(n)]
        def dp(i, preval, increasing, memo):
            if i==n:
                return 1
            if memo[i][preval][increasing]!=-1:
                return memo[i][preval][increasing]
            result=0
            if increasing:
                #then we choose elements smallers than preval
                for val in range(preval-1, -1, -1):
                    result+=(dp(i+1, val, 0, memo)%mod)
                    #decreasing because we are choosing a smaller number
            else:
                #choose greater element
                for val in range(preval+1, m):
                    result+=(dp(i+1, val, 1, memo)%mod)
                    #inc. because we choose a greater number
            memo[i][preval][increasing]=(result%mod)
            return result        

        return (dp(0,-1, 0, memo)*2)%mod
        #calculating for increasing start. the final answer will be twice of it to
        #encorporate decreasing start as well