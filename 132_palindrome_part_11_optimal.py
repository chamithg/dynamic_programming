from collections import defaultdict

class Solution:
    
    def partition(self, s):
        d = defaultdict(set)
        N = len(s)
        
        def helper(i,j):
            
            while i>=0 and j<N and s[i]==s[j]:
                d[i].add(j)
                i-=1
                j+=1
        for k in range(N):
            helper(k,k)
            helper(k,k+1)

        def dfs(i):
            if i==N: return 0
            tmp = []
            for j in range(i,N+1):
                if j in d[i]:
                    tmp.append(dfs(j+1)+1)
            return min(tmp)
        
        return dfs(0) -1
        
# s = "aabaadfd"  
s="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"   
# s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
obj = Solution()
print(obj.partition(s))