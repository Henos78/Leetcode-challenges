class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #another approach 
        memo = {}
        return self.helper(expression, memo)
    
    def helper(self, expression, memo):
        if expression in memo:
            return memo[expression]
        # Base case
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = expression[:i]
                right = expression[i+1:]
                
                # Recursively compute the results of left and right substrings
                left_res = self.helper(left, memo)
                right_res = self.helper(right, memo)
            
                for left_val in left_res:
                    for right_val in right_res:
                        if expression[i] == '+':
                            res.append(left_val + right_val)
                        elif expression[i] == '-':
                            res.append(left_val - right_val)
                        else:
                            res.append(left_val * right_val)
        
        # Store the computed result in memo and return it
        memo[expression] = res
        return res
        
"""
       # It works but not efficient tle error
        if ("+" not in expression) and ('-' not in expression) and ('*' not in expression) and expression != "":
            return [int(expression)] 
        
        res = []
        
        for i , v in enumerate(expression):
            left_res = self.diffWaysToCompute(expression[:i])
            right_res = self.diffWaysToCompute(expression[i+1:])
            
            for left_i, left_v in enumerate(left_res):
                for right_i, right_v in enumerate(right_res):
                    if v == '+':
                        res.append(left_v + right_v)
                    elif v == '-':
                        res.append(left_v-right_v)
                    else:
                        res.append(left_v * right_v)
                        
        return res
        
       
       
"""

        
            
      
            
            
                
            
                
        
        