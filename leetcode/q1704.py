class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        update = s.lower()
        l = len(s)
        one = update[:l/2]
        two = update[l/2:]
        def check(a):
            c = 0
            for i in a :
                if i in 'aeiou':
                    c+=1
            return c
        if check(one)== check(two):
            return True
        return False

        
