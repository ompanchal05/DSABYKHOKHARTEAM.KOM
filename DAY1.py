#Problem Number: 217. Contains Duplicate

###  How to Solve : 

#1. We need to check if there are **duplicate elements** in the list.
#2. A brute force way is to compare every pair (O(n²)), but that’s slow.
#3. A better way: use a **set** (since set stores only unique elements).
#4. While iterating through the array, check if a number is already in the set.
#5. If yes → return **True** (duplicate found).
#6. If we finish the loop with no duplicates → return **False**.
#7. Another shortcut: directly compare `len(nums)` with `len(set(nums))`.

#   * If lengths differ → duplicates exist.
#   * Else → all unique.

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Test
print(containsDuplicate([1,2,3,1]))   # True
print(containsDuplicate([1,2,3,4]))   # False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True

#Time complexity : Brute Force (O(n²))