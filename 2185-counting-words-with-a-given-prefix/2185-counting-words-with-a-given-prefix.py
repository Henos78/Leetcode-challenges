class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        
        for word in words:
            temp =0
            for i in range(len(pref)):
                if len(word)>=len(pref) and pref[i] == word[i]:
                    temp +=1
                else:
                    temp =0
                    
            if temp==len(pref):
                count +=1

        return count