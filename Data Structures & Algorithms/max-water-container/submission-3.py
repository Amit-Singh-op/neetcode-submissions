class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxlen = float("-inf")
        while i<j:
            maxlen = max(maxlen, (j-i)*min(heights[i],heights[j]))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxlen


# 1 7 9 10 15 4 7 3 6
#   i
#     j

