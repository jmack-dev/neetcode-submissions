class Solution:

    def encode(self, strs: List[str]) -> str:
        SEP = ','
        result = ''
        for s in strs:
            result += str(len(s))
            result += SEP
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        SEP = ','
        result = []
        idx = 0
        len_str = ''
        while idx < len(s):
            while s[idx] != SEP:
                len_str += s[idx]
                idx += 1
            str_len = int(len_str)
            len_str = ''
            result.append(s[(idx+1):(idx+str_len+1)])
            idx += str_len+1
        return result

                    