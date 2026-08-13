class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h={}
        for n in nums:
            h[n] = True
        maxlen = float("-inf")
        for i in range(len(nums)):
            num = nums[i]
            count =0
            while num in h:
                count+=1
                num+=1
            maxlen = max(maxlen, count)
        
        return 0 if maxlen == float("-inf") else maxlen
    
            
            


