class Solution:
    def countBits(self, n):    
        map = {}
        output = []
        for i in reversed(range(n+1)): 
            if i in map:
                output.insert(0,map[i])
            else:
                count = 0
                temp = i
                while temp >1:
                    count += temp%2
                    temp = temp //2
                count += temp
                if i not in map:
                    map[i] = count
                output.insert(0,count)

        return output
            
n = 8
obj = Solution()
print(obj.countBits(n))


0  ,1, 2, 3, 4, 5,
[0, 1, 1, 2, 1, 2]