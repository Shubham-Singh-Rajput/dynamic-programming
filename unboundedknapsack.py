# if repetition allow use ond array
wt=[2,5,1,3,4]
val=[15,14,10,45,30]
target=7
dp=[0]*(target+1)
for i in range(len(dp)):
    maxi=0
    for j in range(len(val)):
        if i>=wt[j]:
            rem=i-wt[j]
            total=dp[rem]+val[j]
            if total>maxi:
                maxi=total
        dp[i]=maxi
print("ans=",dp[-1])
print(dp)