def count_frequencies(s):
    freq = {}
    for char in s:
        if char != " ":  # Ignoring spaces
            freq[char] = freq.get(char, 0) + 1
    return freq

# Example
print(count_frequencies("data structures and algorithms"))