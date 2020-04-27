def lex_sorting(str1):
    new_str = str1.split()
    act_min = "z"
    import pdb; pdb.set_trace()
    res_min, res_str = sub_sorting(new_str, act_min)
    while(res_str[0][0] < res_min or res_str[0][0] > res_min):
        res_min, res_str = sub_sorting(new_str, res_min)
    return new_str


def sub_sorting(new_str, res_min):
    for i in range(0, len(new_str)-1):
        j = 0
        while(i+1 < len(new_str)):
            if new_str[i][j] > new_str[i+1][j]:
                res_min = min(res_min, new_str[i + 1][j])
                new_str[i], new_str[i+1] = new_str[i+1], new_str[i]
                break
            elif new_str[i][j] == new_str[i+1][j]:
                j+=1
                if j == len(new_str[i]) or j == len(new_str[i+1]):
                    new_str[i], new_str[i+1] = new_str[i+1], new_str[i]
                    break
            elif new_str[i][j] < new_str[i+1][j]:
                res_min = min(res_min, new_str[i][j])
                break
    return res_min, new_str


print(lex_sorting("we qwer erer qw errr"))