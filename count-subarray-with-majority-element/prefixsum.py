class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n=len(nums)
        ans=0
        presum=[0]*(n+1)
        for i in range(n):
            if nums[i]==target:
                presum[i+1]=1
        for i in range(1, n+1):
            presum[i]+=presum[i-1]
        for i in range(n):
            for j in range(i, n):
                count=presum[j+1]-presum[i]
                if 2*count>(j-i+1):
                    ans+=1
        return ans
        
# a prefix array is created where the target element is mapped to 1
# for array [1, 2, 2, 3], target = 2
# prefix array becomes [0, 1, 1, 0]
# compute prefix sum
# [0, 1, 2, 2]
# range sum => sum(l...r)=prefix[right+1]-prefix[left]