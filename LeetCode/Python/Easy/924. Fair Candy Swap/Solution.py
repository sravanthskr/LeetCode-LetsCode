class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        # 1. Calculate the total candies each person has
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        
        # 2. Calculate the target average they both need to reach
        target = (aliceSum + bobSum) // 2
        
        # 3. Put Bob's candies into a Set for O(1) lookups
        bobSet = set(bobSizes)
        
        # 4. Figure out how much Alice needs to gain to hit the target
        # Example: Alice has 3, target is 4. She needs to gain 1.
        diff = target - aliceSum
        
        # 5. Loop through Alice's candies to find the right swap
        for a in aliceSizes:
            # If Alice gives 'a', she needs to get back 'a + diff' from Bob
            # to successfully hit the target.
            b = a + diff
            
            # Check if Bob actually has this exact candy
            if b in bobSet:
                return [a, b]
                
        return [] # Fallback, though problem guarantees a valid answer
