class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newHashMap = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in newHashMap:
                newHashMap[sorted_word].append(word)
            else:
                newHashMap[sorted_word] = [word]
        return list(newHashMap.values())