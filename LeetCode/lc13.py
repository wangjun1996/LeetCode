# Runtime: 224 ms, faster than 21.16%   罗马数字转整数

class Solution:
    def romanToInt(self, s):
        dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while(i < len(s)):
            a = dict[s[i:i + 1]]
            akey = s[i:i + 1]
            if i < len(s) - 1:
                b = dict[s[i + 1:i + 2]]
                bkey = s[i + 1:i + 2]
                if a >= b:
                    sum += a
                    i += 1
                if (akey == 'I' and (bkey == 'V' or bkey == 'X')) or (akey == 'X' and (bkey == 'L' or bkey == 'C')) \
                        or (akey == 'C' and (bkey == 'D' or bkey == 'M')):
                    sum += b-a
                    i += 2
            else:
                sum += a
                i += 1
        return sum

if __name__ == '__main__':
    s = 'MCMXCIV'
    print(Solution().romanToInt(s))