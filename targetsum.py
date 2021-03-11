nums=[4,2,7,1,3]
t=10
dp=[[False for i in range(t+1)]for j in range(len(nums)+1) ]
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if i==0 and j==0:
            dp[i][j]=True
        elif j==0:
            dp[i][j]=True
        elif i==0:
            dp[i][j]=False
        else:
            if dp[i-1][j]:
                dp[i][j]=True
            else:
                nums[i-1]<=j
                if dp[i-1][j-nums[i-1]]:
                    dp[i][j]=True
print(dp)