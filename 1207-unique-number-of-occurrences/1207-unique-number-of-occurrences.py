class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic ={}
        
        for num in arr:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        freq= []       
        for val in dic:
            freq.append(dic[val])
        
        return len(freq) == len(set(freq))
            