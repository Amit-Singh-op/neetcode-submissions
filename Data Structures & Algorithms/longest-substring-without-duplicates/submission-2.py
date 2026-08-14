class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        i,j=0,0
        maxlen=0
        while j<len(s):
            while j<len(s) and s[j] in h and h[s[j]]!=0:
                h[s[i]]-=1
                i+=1
            h[s[j]] = h.get(s[j], 0) + 1
            maxlen=max(maxlen, j-i+1)
            j+=1
        return maxlen
            