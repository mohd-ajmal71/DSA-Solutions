class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        t_cost = 0
        count = 0

        for i in costs:
            if t_cost + i <= coins:
                t_cost += i
                count += 1
            else:
                break

        return count

