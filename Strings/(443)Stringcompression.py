class Solution:

    def compress(self, chars):

        index = 0
        i = 0
        n = len(chars)

        while i < n:

            current = chars[i]
            count = 0

            while i < n and chars[i] == current:
                count += 1
                i += 1

            # Store character
            chars[index] = current
            index += 1

            # Store count if greater than 1
            if count > 1:

                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index