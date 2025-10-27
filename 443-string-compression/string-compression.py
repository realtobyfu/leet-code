from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            # for each contiguous chunck of chars
            ch = chars[read]
            count = 0
            while read < n and chars[read] == ch:
                read += 1
                count += 1
            # write the character itself:
            chars[write] = ch
            write += 1

            # write the count digits
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
            
        return write


