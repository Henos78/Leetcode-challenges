class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #Second trial using dp approach
        
        # Sort the list of players based on their ages in descending order
        players = sorted(list(zip(scores, ages)),key=lambda x:(x[1],x[0]), reverse=True)
        
        maxScore = 0
        dp = [0] * len(players) 
        print(players)
        for i in range(len(players)):
            dp[i] = players[i][0]  # Initialize with the current player's score
            for j in range(i):
                if players[j][0] >= players[i][0]:
                    dp[i] = max(dp[i], dp[j] + players[i][0])  # Update the maximum score
            
            maxScore = max(maxScore, dp[i])  
            
        return maxScore
        
        
        
        
        
        """
        #first trial  (failed test case)
        
        #base case
        if len(scores)==1:
            return scores[0]
        
        #sort based on their age 
        
        sortedList = sorted(zip(scores,ages), key = lambda x:x[1], reverse=True)
        
        scores, ages = list(zip(*sortedList))
        
        scores  = list(scores)
        ages = list(ages)
        print(scores)
        print(ages)
        maxScore =0
        temp = scores[0]

        for i in range(1,len(scores)):
            if scores[i] <=scores[i-1]:
                temp += scores[i]
                maxScore = max(maxScore, temp)
            if scores[i]> scores[i-1]:
                temp = scores[i]
                maxScore = max(maxScore,temp)
                
        return maxScore
        """
            