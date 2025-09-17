class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in s.lower():
            for j in i:
                if j.isalnum():
                    res.append(j)
        return res==res[::-1]

        
          

        