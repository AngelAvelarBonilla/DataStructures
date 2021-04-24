def longest_substring(s, t):
    """Finds the longest substring that occurs in both s and t"""
    best = ''
    left = 0
    right = min(len(s), len(t))

    while left < right:  # while our left and right bounds are not the same
        mid = (left + right + 1) // 2  # we get our middle size
        ans = k_substring(s, t, mid)  # we get a substring using our middle size

        if ans is not None:  # if we find a substring then we can ignore the smaller
            best = ans       # sizes since we have already found one bigger
            left = len(best)
        else:                # if we cannot find a substring using the middle size
            right = mid - 1  # we know for sure there are no greater length subtrings
                             # so we can ignore the greater sizes
    return best

def k_substring(s, t, k):
    """Finds a substring of length k in both s and t if there is one,
    and returns it. Otherwise, returns None."""
    s_substrings = set()
    # Put all substrings of s of length k into a set: s_substrings
    for s_start in range(len(s) - k + 1):
        current = s[s_start:s_start+k]
        s_substrings.add(current)
    # For every substring of t of length k, look for it in
    # s_substrings. If it's there, return it.
    for t_start in range(len(t)-k+1):
        current = t[t_start:t_start+k]
        if current in s_substrings:
            return current
    return None
