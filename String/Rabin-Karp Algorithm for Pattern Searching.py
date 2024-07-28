class Solution:
    def search(self, pattern, text):
        d = 256  # number of characters in the input alphabet
        m = len(pattern)
        n = len(text)
        p = 0  # hash value for pattern
        t = 0  # hash value for text
        h = 1
        q = 101

        # The value of h would be "pow(d, m-1) % q"
        for i in range(m - 1):
            h = (h * d) % q

        # Calculate the hash value of pattern and first window of text
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        # List to store the positions of pattern match
        result = []

        # Slide the pattern over text one by one
        for i in range(n - m + 1):
            # Check the hash values of current window of text and pattern
            if p == t:
                # Check for characters one by one
                match = True
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        match = False
                        break
                if match:
                    result.append(i + 1)  # Convert to 1-based index

            # Calculate hash value for next window of text: Remove leading digit, add trailing digit
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                # We might get a negative value of t, converting it to positive
                if t < 0:
                    t = t + q

        return result