class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = float("-inf")
        for i in range(len(nums)):
            if nums[i] -1 not in s:
                num = nums[i]
                count = 0
                while num in s:
                    count+=1
                    num+=1
                maxlen = max(maxlen, count)
        
        return 0 if maxlen == float("-inf") else maxlen
    
            
            


