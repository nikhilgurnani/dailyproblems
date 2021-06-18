"""
Given a list of positive integers that represent salaries salaries and a target budget budget, return an appropriate "salary cap".

The "salary cap" is a cap on salaries so that the sum of all salaries stays below the budget budget.

Example:

Input:
salaries = [100, 300, 200, 400]
budget = 800

Output: 250
Explanation: A salary cap of 250 leaves the new salaries at [100, 250, 200, 250]. This happens to sum up to the budget of 800, thus 250 serves as a valid salary cap.

"""
class Solution:
    def computeSalaryCap(self, salaries, budget):
        '''
        :type salaries: list of int
        :type budget: int
        :rtype: int
        '''

        """
        salaries = [100, 300, 200, 400]
        budget = 800

        total = 1000
        diff = total - budget = 1000 - 800 => 200
        sorted_salaries = [100, 200, 300, 400]
        """

        salaries = sorted(salaries)

        i = len(salaries) - 1

        while i > 0:
            total = 0
            for k in range(0, i):
                total += salaries[k]

            k = budget - total
            if k >= salaries[i-1]:
                pos = len(salaries)-i
                return k // i
            i -= 1

        return budget // len(salaries)

print(Solution().computeSalaryCap([100, 300, 200, 400], 800))