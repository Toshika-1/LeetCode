class fenwicktree(object):
    def __init__(self, n):
        self.n=n
        self.bitTree=[0]*(n+1) #1 indexed
    def update(self, idx, delta):
        while idx<=self.n:
            self.bitTree[idx]+=delta
            idx+= idx & -idx    
            #moves to the next node responsible for larger range
            #if idx=12: (idx & -idx)=4 => idx becomes 16
    def query(self, idx):
        res=0
        while idx>0:
            res+= self.bitTree[idx]
            idx-= idx & -idx
            #move upwards to collect prefix sums
            #idx becomes 12->8->0
        return res
    def range_query(self, left, right):
        return self.query(right)-self.query(left-1)
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n=len(nums)
        ans=0
        BIT=fenwicktree(n)
        prefix=[0]*(n+1)
        for i in range(n):
            if nums[i]==target:
                prefix[i+1]=1
            else:
                prefix[i+1]=-1
        #computing prefix sums
        for i in range(1, n+1):
            prefix[i]+=prefix[i-1]
        vals=sorted(set(prefix))
        rank={}
        for i, v in enumerate(vals, start=1):
            rank[v]=i
        for p in prefix:
            r=rank[p]
            ans+=BIT.query(r-1)
            BIT.update(r, 1)
        
        return ans
        