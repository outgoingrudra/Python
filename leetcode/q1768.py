class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=i=len(word1)
        y=j=len(word2)
        k= i+j
        ans =""
        while k :
            if i:
                ans +=word1[x-i]
                i-=1
            if j :
                ans +=word2[y-j]
                j-=1

            k-=1
        return ans 
        
