class Solution:
    def wordBreak(self, s, wordDict):
        self.outlist = set()
        def build(start,out):
            if start>= len(s):
                self.outlist.add(out)
                return
            for i in range(start,len(s)):
                if s[start:i+1] in wordDict:
                    build(i+1,out+s[start:i+1]+" ")
            return
        build(0,"")
        return self.outlist

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
obj = Solution()
print(obj.wordBreak(s,wordDict))