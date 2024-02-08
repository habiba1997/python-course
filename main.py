# Devise a function that takes an input N (integer) and returns the sum of the digits of all the numbers from 1 to N (with N included).
# For example, for N = 11 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) = 48

def summ(n):
    Sum = 0
    for i in range(0, n+1):
        if len(str(i)) < 2:
            Sum += i
        else:
            strN = str(n)
            for j in range(0, len(strN)):
                Sum += int(strN[j])
    return Sum

def sumStreams(n):
    mydict= {i * 1:j for i,j in enumerate(range(n + 1)) if i % 2 == 0}
    print(mydict)
    s=0
    for i in mydict.values():
        s+=sum(map(lambda s: int(s), str(i)))
    return s
print(sumStreams(11))