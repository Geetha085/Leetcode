class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         char_set = set()
         start = 0
         max_length = 0
    
         for end in range(len(s)):
            while s[end] in char_set:
            # remove from start until we can add s[end]
               char_set.remove(s[start])
               start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
    
         return max_length

        