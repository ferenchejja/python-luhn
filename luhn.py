# Luhn formula

import random

def luhncalc(luhnstr):
    i=0
    lsum=0
    digit=0
    for l in reversed(luhnstr):
        if (i % 2)==0:
            digit=int(l)*2
            if digit>9:
                digit=digit-9
        else:
            digit=int(l)
        lsum=lsum+digit
        digit=0
        i=i+1
    return(str((10-lsum % 10) % 10))

def luhncheck(luhnstr):
    return(luhnstr[-1]==luhncalc(luhnstr[0:-1]))


# Main

a=str(random.randrange(10000,1000000000))
b=luhncalc(a)
print(a,b,luhncheck(a+b))
