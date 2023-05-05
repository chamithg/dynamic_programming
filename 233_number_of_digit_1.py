class Solution:
    def countDigitOne(self, n):
        count = 0
        for i in range(n+1):
            for j in range(len(str(i))):
                if str(i)[j] == "1":
                    count +=1
        return count
        
        
        
        #  not a optimal solution
n = 1000
    
obj = Solution()
print(obj.countDigitOne(n))