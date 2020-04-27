# code
from collections import defaultdict
import sys

def anagram(str_test):
    string = str_test.split()
    import pdb; pdb.set_trace()
    i = 0
    str1 = string[0]
    str2 = string[1]
    l1 = len(str1)
    l2 = len(str2)

    if l1 != l2:
        print("NO")
        sys.exit("NO")

    d = defaultdict(lambda: 0)
    while (i < l1 and i < l2 and (str1[i] and str2[i])):
        d[str1[i]] = d[str1[i]] + 1
        d[str2[i]] = d[str2[i]] - 1
        i += 1

    for i in range(0, l1):
        if d[str1[i]]:
            print("NO")
            sys.exit("NO")
    print("YES")


#anagram("wxrzvimgedlenxnqjideqhzrpubtunekwyqf rklteuwmkkrelkkteqggptpeqfsvbeyyawxqekiqunejslsgwxfkrbtqlbfejxdfuqhpbdkiebkqicscgiaedfgvqsfksrywf")
anagram('aditya atyida')


