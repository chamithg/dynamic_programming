class Solution:
    def partition(self, s):
        len_s = len(s)
        output = []
        def partition(st,temp_str):           
            if st == len_s:
                output.append(temp_str)
                return           
            for i in range(st,len_s):
                if s[st:i+1] == s[st:i+1][::-1]:
                    partition(i+1,temp_str+[s[st:i+1]])
        partition(0,[])
        return output
s = "aab"
obj = Solution()
print(obj.partition(s))