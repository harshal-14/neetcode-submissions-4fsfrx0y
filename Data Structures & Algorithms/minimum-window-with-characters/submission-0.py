from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:                          # 1. "t is None" misses empty string
            return ""

        t_count = {}                       # 2. you overwrote input `t` with `t = {}`
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        required = len(t_count)            # 3. countT was 0, need unique char count

        window_count = {}
        left = 0
        formed = 0
        best = (inf, -1, -1)

        for r in range(len(s)):            # 4. was `for r in len(s) - 1` — need range()
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1  # 5. you never incremented

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while formed == required:      # 6. was `formed == r` — compare to required
                window_size = r - left + 1
                if window_size < best[0]:
                    best = (window_size, left, r)

                # contract from left
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1

        return "" if best[0] == inf else s[best[1]:best[2] + 1]