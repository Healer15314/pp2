class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        for x in range(0, len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[x]==nums[y]):
                    cnt=cnt+1
        return cnt
           