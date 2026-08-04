class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            str_len = str(len(s))
            res += "ي" + str_len + "م" + s
        return res

    def decode(self, s):
        decoded_strs = []
        i = 0
        s_len = len(s)
        while i < s_len:
            if s[i] == "ي":
                i += 1
                j = 0
                while s[i+j] != "م":
                    j += 1
                str_len = int(s[i:i+j])
                i += j + 1
                decoded_strs.append(s[i:i+str_len])
                i += str_len
            else:
                i += 1

        return decoded_strs
        