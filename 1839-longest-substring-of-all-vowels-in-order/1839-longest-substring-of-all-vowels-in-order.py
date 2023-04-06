class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # second approach using a set
        
        l, r = 0, 0
        seen = set()
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        
        while r < len(word):
            if r > 0 and word[r] < word[r-1]:
                l = r
                seen = set()
                
            seen.add(word[r])
            
            if seen == vowels:
                count = max(count, r-l+1)
                
            r+= 1
            
        return count
            
        
        """
         #my first approach but didnt work
            l,r =0, 0
            count = 0

            while r<= len(word):

                if word[l] == 'a' and word[r] == 'a': 
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='e' and word[r-1] == 'a':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='e' and word[r-1] == 'e':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='i' and word[r-1] == 'e':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='i' and word[r-1] == 'i':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='o' and word[r-1] == 'i':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='o' and word[r-1] == 'o':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='u' and word[r-1] == 'o':
                    r +=1
                    count =+1
                elif word[l] == 'a' and word[r] =='u' and word[r-1] == 'u':
                    r +=1
                    count =+1
                else:
                    l = r
                    r+=1
                    count = 0

            return count 

            
        """
       