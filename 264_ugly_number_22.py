class Solution:
    def nthUglyNumber(self, n: int) -> int:
        output = 1
        found = set()
        found.add(1)
        i = 0
        def isUgly(num):
            if num < 1:
                return False
            if num in found or num == 2 or num == 3 or num == 5 :
                return True
            fiveFact = isUgly(num/5)
            threeFact = isUgly(num/3)
            twoFact = isUgly(num/2)
            if fiveFact or threeFact or twoFact:
                return True
            return False
        
        while i < n-1:
            
            output +=1
            if isUgly(output):
                found.add(output)
                if output/5 in found:
                    found.remove(output/5 )
                if output/3 in found:
                    found.remove(output/3 )
                if output/2 in found:
                    found.remove(output/2 )
                i+=1
        
        print(found)
        return output

obj = Solution()
print(obj.nthUglyNumber(300))