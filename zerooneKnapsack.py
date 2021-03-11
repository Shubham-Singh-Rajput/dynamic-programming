wt=[2,5,1,3,4]
val=[15,14,10,45,30]
target=7

dp=[[0 for _ in range(target+1)]for _ in range(len(val)+1)]

for i in range(len(dp)):
    for j in range(len(dp[0])):
        if j>=wt[i-1]:#banda batting kiya
            if dp[i-1][j-wt[i-1]]+val[i-1]>dp[i-1][j]:#banda apne khel ke adhik run bnaya
                dp[i][j]=dp[i-1][j-wt[i-1]]+val[i-1]
            else:
                dp[i][j]=dp[i-1][j] #banda khela pr adik run nhi bnaya to hm nhhi khelaye usko
        else:
            dp[i][j]=dp[i-1][j] #banda nhi khla
print("ans=",dp[-1][-1])
print(dp)