class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        hashexist = set()
        for i in range(len(nums)):
            h={}
            n = nums[i]
            for j in range(i+1, len(nums)):
                val = h[-(nums[j]+n)] if -(nums[j] + n) in h else -999
                if nums[j] + n + (-val) == 0:
                    exist = "".join(sorted(str(nums[j]) + str(n) + str(-val)))
                    if exist not in hashexist:
                        res.append([nums[j], n, (-val)])
                        hashexist.add(exist)
                else:
                    h[nums[j]] = -nums[j]
        return res