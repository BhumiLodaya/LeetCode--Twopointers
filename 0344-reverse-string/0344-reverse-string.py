class Solution(object):
    def reverseString(self, s):
        if not s:
            return 
        left =0
        right =len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]

            left+=1
            right-=1
        