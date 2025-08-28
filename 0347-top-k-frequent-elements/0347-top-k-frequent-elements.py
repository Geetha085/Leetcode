from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq=Counter(nums)
        most_element=frq.most_common(k)
        res=[]
        for key,value in most_element:
            res.append(key)

        return res