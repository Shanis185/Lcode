class Solution(object):
    def letterCombinations(self, digits):
        if digits=="":
            return []
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res,ans=[],[]
        n=len(digits)
        def backtrack(i):
            if i==n:
                res.append("".join(ans))
                return
            for letter in letter_map[digits[i]]:
                ans.append(letter)
                backtrack(i+1)
                ans.pop()
        backtrack(0)
        return res

        