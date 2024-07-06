class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # Number of rounds completed
        rounds = time // (n-1) 
        
        # Number of steps taken
        steps = rounds * (n-1)

        # Less than full iteration
        if time < n:
            result = time+1

        # More than full iteration
        elif time > n:
            if rounds % 2 == 0:
                result = (time-steps) +1
            else:
                result = n - ((time-steps) +1) +1
        
        # 1 iteration
        else:
            result = time-1
            
        return result