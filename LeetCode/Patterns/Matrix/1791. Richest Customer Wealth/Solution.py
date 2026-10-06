class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        import numpy as np
        value=np.sum(accounts, axis=1)
        return int(np.max(value))