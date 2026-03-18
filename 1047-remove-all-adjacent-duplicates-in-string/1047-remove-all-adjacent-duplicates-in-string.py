class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = list(s)
        stk2 = []

        for ch in s:

            if stk2 and stk2[-1] == ch:
                stk2.pop()
            else:
                stk2.append(ch)

        return "".join(stk2)
                