def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    skip = [m] * 256
    
    for i in range(m):
        skip[ord(pattern[i])] = m - i - 1
    
    i = 0
    count = 0
    
    while i < n:
        k = skip[ord(text[i])]
        if k > 0:
            i += k
        else:
            j = m - 1
            while j >= 0 and pattern[j] == text[i-(m-1-j)]:
                j -= 1
            
            if j == -1:
                count += 1
                i += m + 1
            else:
                i += 1
    
    return count

text = "january february march april may june july august september november december"
pattern = "september"
count = boyer_moore_search(text, pattern)
print(f"pattern occurs {count} times")
