class Solution:
    
    def partition(self, s):
        self.min_cut = 2500
        self.found = set()

        def match(length,count):
            if length == len(s):
                self.min_cut= min(self.min_cut,count -1)
                return
            if length > len(s):
                return
            
            for j in range(length,len(s)):
                if s[length:j+1] in self.found:
                    match(length+len(s[length:j+1]),count+1)
                else:    
                    if s[length:j+1] == s[length:j+1][::-1]:
                        self.found.add(s[length:j+1])
                        match(length+len(s[length:j+1]),count+1)
        
        for i in range(len(s)):
            if s[0:i+1] == s[0:i+1][::-1]:
                match(len(s[0:i+1]),1)
                
        return self.min_cut
        
# s = "aabaadfd"  
s="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"   
# s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
obj = Solution()
print(obj.partition(s))