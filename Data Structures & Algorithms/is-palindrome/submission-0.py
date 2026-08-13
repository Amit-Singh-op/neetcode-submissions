class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in range(len(s)):
            if s[i].isalnum():
                s1+=s[i]
            if s[i] == ' ':
                s1+=' '
        arr = s1.split(" ")
        for i in range(len(arr)):
            arr[i] = "".join(arr[i].lower())
        s2 = "".join(arr)
        i=0
        j=len(s2)-1
        while i<=j:
            if s2[i]!=s2[j]:
                return False
            i+=1
            j-=1
        return True