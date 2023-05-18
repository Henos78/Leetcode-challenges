class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #using bit
        maxpro= 0
        temp = [0]*len(words)
        
        #here we convert the words into a bit representation using their ascii value
        for i in range(len(words)):
            for ch in words[i]:
                temp[i] |= 1 << (ord(ch)-ord('a'))

        #here we itrate through the temp array and select two words and do AND operation and if = to 0 it means they have no common characters we will multiply and store the res and Continue doing that and find the max product 
        
        for i in range(len(words)):
            for j in range(1, len(words)):
                if temp[i]&temp[j] == 0:
                    pro= len(words[i])*len(words[j])
                    maxpro = max(pro,maxpro)
        return maxpro
            