class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse iterate over both strings
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                summation = mul + result[i + j + 1]
                result[i + j + 1] = summation % 10
                result[i + j] += summation // 10
        
        # Convert list to string, skipping leading zeros
        res_str = "".join(map(str, result)).lstrip("0")
        return res_str if res_str else "0"
