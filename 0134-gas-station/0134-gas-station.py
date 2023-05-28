class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # second appraoch greedy
        
         # return -1 if the total gas is less than the total cost
        if sum(gas) < sum(cost):
            return -1

        cur, pos = 0, 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            # if cur is negative, update starting_station to the next station
            # and reset cur to 0
            if cur < 0:
                pos = i + 1
                cur = 0 
        
        
        return pos

        """
        #first approach and trial
                def parity(arr):
            for val in arr:
                if val >0:
                    return True
            return False
                
        diff = [0]*len(gas)
        presum = [0]*len(gas)

        for i in range(len(gas)):
            diff[i]= gas[i]-cost[i]

        presum[0]= diff[0]
        
        for  i in range(1, len(diff)):
            presum[i] += presum[i-1]+diff[i]
            
        print(presum)   
        check = parity(presum)
        print(check)
        
        if check ==False:
            return -1
        
        temp = min(presum)
        print(temp)
        for i in range(len(presum)):
            if presum[i]==temp:
                return i+1 if i != len(presum)-1 else 0

        return -1
        """