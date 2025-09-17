class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in s.lower():
            for j in i:
                if j.isalnum():
                    res.append(j)
        if res==res[::-1]:
            return True
        else:
            return False

        