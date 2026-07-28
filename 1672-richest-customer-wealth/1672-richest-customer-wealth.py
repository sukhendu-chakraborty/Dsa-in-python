class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        tot_wealth= []
        for i in range (len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth = wealth+accounts[i][j]
                tot_wealth.append(wealth)
        return max(tot_wealth)

        