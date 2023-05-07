class Solution:
    def numWays(self,n,k):
        self.out= []
        def paint(patern):
            if len(patern) == n:
                self.out.append(patern)
                return
            elif len(patern) < 2:
                for i in range(k):
                    patern.append(i)
                    paint(patern)
                    patern.pop()
            else:
                for i in range(k):
                    if not patern[-1] == patern[-2] == i:
                        patern.append(i)
                        paint(patern)
                        patern.pop()   
            return 
        paint([])
        return len(self.out)
        
    
n = 2
k = 4
obj = Solution()
print(obj.numWays(n,k))