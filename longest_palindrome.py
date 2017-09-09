def longest_palindrome(s):
    largest_first = 0
    largest_last = 0
    for center in range(0, len(s)):
        # Check for odd length palindrome
        radius = 0
        while True:
            first = center - radius
            last = center + radius
            if first < 0 or last >= len(s):
                break
            if s[first] != s[last]:
                break

            # It's a palindrome!
            if last - first > largest_last - largest_first:
                largest_first = first
                largest_last = last
            radius += 1

        # Check for even length palindrome
        radius = 0
        while True:
            first = center - radius
            last = center + radius + 1
            if first < 0 or last >= len(s):
                break
            if s[first] != s[last]:
                break

            # It's a palindrome!
            if last - first > largest_last - largest_first:
                largest_first = first
                largest_last = last
            radius += 1

    return s[largest_first : largest_last + 1]