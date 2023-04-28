class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_s = ""
        for i in s:
            if i.isalnum():
                str_s +=i.lower()

        for i in range(len(str_s)//2):
            if str_s[i]!= str_s[len(str_s)-1-i]:
                return False

        return True
            