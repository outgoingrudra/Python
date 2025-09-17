class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = []
        for i in magazine:
            m.append(i)
        for i in ransomNote :
            if i in m :
                m.remove(i)
            else :
                return False 
        return True
        
