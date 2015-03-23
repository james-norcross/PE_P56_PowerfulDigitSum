## Author: James Norcross
## Date: 3/20/15
## Purpose: Project Euler problem 56
## Description finds the maximum digit sum for numbers a^b where a, b < 100

def DigitSum(n):
    sumDigits = 0

    n_str = str(n)
    n_list = list(n_str)

    for d in n_list:
        sumDigits += int(d)

    return sumDigits


maxDigitSum = 0

for a in range(1,100):
    
    for b in range(1,100):
        
        x = DigitSum(a**b)
        
        if(x > maxDigitSum):
            maxDigitSum = x

print "The maximum digit sum is %d" % maxDigitSum

