def wordbreak_memo(s, words):
    if s == '':
        return True

    for i in range(1,len(s)+1):
        sub = s[:i]

        if not sub in words:
            continue

        if wordbreak_memo(s[i:], words):
            return True

    return False

print(wordbreak_memo("ilikesamsaung", ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man',
                                  'go', 'mango']))