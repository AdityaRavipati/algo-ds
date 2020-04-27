import decimal


def simple_fraction(a, b):
    import pdb; pdb.set_trace()
    n = a
    d = b
    decimal.getcontext().prec = 200
    res=decimal.Decimal(n)/decimal.Decimal(d)
    res_str=str(res)
    if res_str==str(int(res)) or res_str==str(n/d):
        print(res_str)
    else:
        dec_index=res_str.index(".")+1
        flag=True
        while flag:
            for j in range(2,int(len(res_str[dec_index:])/2)):
                if res_str[dec_index:dec_index+j]==res_str[dec_index+j:dec_index+2*j]:
                    res_str=res_str[:dec_index]+"("+res_str[dec_index:dec_index+j]+")"
                    flag=False
                    break
            dec_index+=1
        if res_str[-3]==res_str[-2] and res_str[-4]=="(":
            res_str=res_str[:-2]+")"
        print(res_str)


simple_fraction(84,87)