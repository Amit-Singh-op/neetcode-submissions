class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPod = [1 for _ in range(len(nums))]
        postfixPod = [1 for _ in range(len(nums))]
        for i in range(1, len(prefixPod)):
            prefixPod[i] = prefixPod[i-1]*nums[i-1]
        for i in range(len(postfixPod)-1, -1, -1):
            postfixPod[i] = 1 if i == len(postfixPod)-1 else postfixPod[i+1]*nums[i+1]
        return [a * b for a, b in zip(prefixPod, postfixPod)]