# code
# code
from collections import OrderedDict


def duplicates_test(l1, str1):
    import pdb;pdb.set_trace()
    i = 0

    d = OrderedDict()
    while(i < l1 and str1[i]):
        if i != 0 and str1[i] in d.keys():
            pass
        else:
            d[str1[i]] = 1
        i+=1

    res = ""
    for key,value in d.items():
        res = res+key
    return res


string = "geeks for geeks"
l1 = len(string)
print(duplicates_test(l1, string))
