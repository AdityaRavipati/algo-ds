def pow(x, n, d):
    if x == 0 and n == 0:
        res = 0
    elif x != 0 and n == 0:
        res = 1
    elif (n % 2 == 0):
        res = pow(x, (n / 2), d) * pow(x, (n / 2), d)
    else:
        res =  (x * pow(x, (n/2), d) * pow(x, (n/2), d))
    power_res = res % d
    return power_res




print(pow(-1, 2, 20))
#print(pow(71045970, 41535484, 64735492))