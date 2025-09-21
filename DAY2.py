#Problem Number: 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

solution = Solution()

print(solution.isAnagram("racecar", "carrace"))
print(solution.isAnagram("jar", "jam"))

