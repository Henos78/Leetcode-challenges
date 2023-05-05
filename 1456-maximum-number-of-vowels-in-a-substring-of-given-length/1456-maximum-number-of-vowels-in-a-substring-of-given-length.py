class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        vcount =0
        ans =0
        l,r = 0,0
        
        # t.c: o(n)
        for r in range(len(s)):
            if s[r] in vowels:
                vcount += 1
                
            if (r-l+1) == k:
                ans = max(ans,vcount)
                
                if s[l] in vowels:
                    vcount -= 1
                l +=1
            
        return ans
        
        
        
        