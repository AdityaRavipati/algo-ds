# Hamming distance is the number of bit positions in which the two bits are different

def hamming(arr, n):
    count = 0
    for i in range(0, n):
        length = n
        while(length>0):
            # XOR of pair
            x = arr[i] ^ arr[length-1]
            setBits = 0
            while (x > 0):
                # Inorder to count number of 1's in the result x,
                # every time we do logical AND operation between x and 1 and
                # in the next step rightshift the x by 1 bit.
                setBits += x & 1
                x >>= 1
            length = length-1
            count = count + setBits
    print count


arr = [1,2]
n = len(arr)
hamming(arr, n)