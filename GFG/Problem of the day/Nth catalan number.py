
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
    #  MORE TIME TAKEN WITH RECURSION (WORST CASE)
        m = 1000000007
        # if n <= 1:
        #     return 1
    
        # # Catalan(n) is the sum
        # # of catalan(i)*catalan(n-i-1)
        # res = 0
        # for i in range(n):
        #     res += self.findCatalan(i) * self.findCatalan(n-i-1)
    
        # return res%m

#   LESS TIME TAKEN COMPARE TO RECURSION (MEDIAN CASE)
        if (n == 0 or n == 1):
            return 1
        # divide table
        catalan = [0 for i in range(n + 1)]
        # Initialization
        catalan[0] = 1
        catalan[1] = 1
        # recursion
        for i in range(2, n + 1):
           catalan[i] = 0
           for j in range(i):
              catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]
        return catalan[n]%m
        


        # code here
#   LESS TIME COMPARE TO ALL BOTH METHOD (BEST CASE)
        m = 1000000007
        
        # Calculate factorial
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result = (result * i) % m
            return result
        
        numerator = factorial(2 * n)
        denominator = (factorial(n + 1) * factorial(n)) % m
        
        # Calculate modular inverse using Fermat's Little Theorem
        def mod_inverse(base, exponent, modulus):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                temp = mod_inverse(base, exponent // 2, modulus)
                return (temp * temp) % modulus
            else:
                temp = mod_inverse(base, exponent - 1, modulus)
                return (base * temp) % modulus
        
        inverse_denominator = mod_inverse(denominator, m - 2, m)
        
        catalan_n = (numerator * inverse_denominator) % m
        return catalan_n
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends