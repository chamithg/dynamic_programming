class Solution:
    
    def partition(self, s):
        self.min_cut = 2500
        all ={}
        for i in range(len(s)):
            pali = []
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    pali.append(len(s[i:j+1]))
            all[i] = pali
        
        
        def match(end,count):
            if end == len(s):
                self.min_cut= min(self.min_cut,count -1)
                return
            if end > len(s):
                return
            for j in all[end]:
                if end + j <= len(s):
                    match(end + j,count +1)
        
        for i in all[0]:
            match(i,1)
            
        print(all)
        return self.min_cut
        
# s = "aabaadfd"     
s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
obj = Solution()
print(obj.partition(s))