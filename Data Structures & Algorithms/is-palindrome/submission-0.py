class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = []
        for i in s:
            if i.isalnum() is True:
                s_alnum += i.lower()
            else:
                continue

        final_s = "".join(s_alnum)
        if final_s== final_s[::-1]:
            return True
        else:
            return False
        