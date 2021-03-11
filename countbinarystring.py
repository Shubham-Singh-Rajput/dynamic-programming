n=6
zero=1
one=1
for i in range(2,n+1):
    newzero=one
    newone=one+zero
    zero=newzero
    one=newone
print(zero+one)
