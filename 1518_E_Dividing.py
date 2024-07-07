# 7/July/2024

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Initial number of bottles 
        total = numBottles

        # While amount of bottles is more than the amount needed to exchange
        while numBottles >= numExchange:

            # Calculate number returned in exchange
            NewBottles = numBottles // numExchange
            total += NewBottles
            
            # Reset numBottles
            numBottles = (numBottles % numExchange) + NewBottles
        
        # Return total bottles
        return total
