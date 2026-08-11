class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        
        return list(dict(sorted(h.items(), key=lambda item: item[1], reverse=True)))[:k]
        