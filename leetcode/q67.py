class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res =""
        carry = 0
        a , b = a[::-1], b[::-1]
        for i in range(max(len(a),len(b))):
            digitA = ord(a[i])- ord("0") if i < len(a) else 0
            digitB = ord(b[i])- ord("0") if i < len(b) else 0
            t = digitA + digitB + carry
            res = str(t%2) + res
            carry = t // 2
        if carry :
            res = "1"+ res
        return res

        
