class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        #second approach (brute force)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        
        for i in range(len(word)):
            for j in range(i+4, len(word)+1):
                if set(word[i:j]) == vowels:
                    count += 1
        return count
        
#      #approach one (for some reason it didnt work)
#         l, r = 0, 0
#         vowels = set(['a', 'e', 'i', 'o', 'u'])
#         count = 0
#         seen = set()
        
#         while r < len(word):
            
            
#             if word[r] in vowels:
#                 seen.add(word[r])
#             else:
#                 l = r
#                 seen = set()
            
#             if len(seen) == len(vowels):
#                 count += 1
                
#             r += 1
            
#         return count
    