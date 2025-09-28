'''TWO SUM KARVANU CHE EMA PAN USE KARVANI CHE BEURATE METHODE BECAUSE OF THE TIME COMPLEXITY SO USING THE BURATE FORCE METHODE 

'''

# Input list
nums = [1, 2, 3, 4, 5]

# Brute Force Two Sum class
class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        # Loop through all pairs
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]  # Return the first pair found
        return []  # fallback if no pair found

# -------------------------------
# Example usage
# -------------------------------
target = 7
solver = TwoSum(nums, target)
print("Pair indices:", solver.find_pair())  # Output: [1, 4] → 2 + 5 = 7
