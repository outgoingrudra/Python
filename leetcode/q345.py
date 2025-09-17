class Solution:
    def reverseVowels(self, s: str) -> str:
        v =['a','e','i','o','u','A','E','I','O','U']
        a = ""
        for i in s :
            if i in v:
                a = a + i
        a= a[::-1]
        t=0
        ans =''
        for i in range(len(s)):
            if s[i] in v:
                ans+= a[t]
                t+=1
            else:
                ans+=s[i]
        return ans
        
