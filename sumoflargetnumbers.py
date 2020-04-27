a = "7777555511111111"
b =    "3332222221111"

lenofa = len(a)
lenofb = len(b)

# reverse both the strings
reverseofa = a[::-1]
reverseofb = b[::-1]

carry = 0
result = ""
tempb = lenofb

for i in range (tempb):
    sum = int(reverseofa[i]) + int(reverseofb[i]) + carry
    actualsum = sum%10
    carry = sum/10
    result += str(actualsum)

for i in range (lenofb, lenofa):
    sum = int(reverseofa[i]) + carry
    actualsum = sum % 10
    carry = sum / 10
    result += str(actualsum)

if carry:
    sum = result + str(carry)
else:
    sum = result

print(sum[::-1])



