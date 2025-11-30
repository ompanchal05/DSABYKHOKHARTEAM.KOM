# Day 4 – Group Anagrams (Python Solution)

def groupAnagrams(strs):
    anagram_map = {}

    for s in strs:
        key = ''.join(sorted(s))  # sorting gives same signature for anagrams
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)

    return list(anagram_map.values())


# Test Case
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(groupAnagrams(strs))
