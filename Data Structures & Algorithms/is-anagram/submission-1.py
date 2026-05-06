class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        listS = list(s)
        listT = list(t)

        listS.sort()
        listT.sort()

        if listS == listT:
            return True
        else:
            return False