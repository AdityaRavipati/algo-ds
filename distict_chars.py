#code
from collections import OrderedDict


def distict_chars(l1, str1):
    import pdb; pdb.set_trace()
    i = 0
    d = OrderedDict()
    while(i < l1 and str1[i]):
        if i != 0 and str1[i] in d.keys():
            i = 0
            d = {}
            d[str1[i]] = 1
            pass
        else:
            d[str1[i]] = 1
        i+=1

    res = ""
    for key,value in d.items():
        res = res+key
    return res

#t = int(input())
string = "geeksforgeeks"
l1 = len(string)
# print(distict_chars(l1, string))


########################################################

from collections import defaultdict


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i = 0
    d = defaultdict(lambda: 0)

    while (i < n):
        d[ar[i]] = d[ar[i]] + 1
        i+=1

    pairs = 0
    for key, value in d.items():
        res = value / 2
        if res:
            pairs += res

    return pairs

#print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

########################################################

def test(num):
    res = ((num - 8133451661952) / 10 ** 12)
    print int(res)

test(10167265626672)