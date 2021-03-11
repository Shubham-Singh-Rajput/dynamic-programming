nums=[2,3,5,6]
t=10
dp=[0]*(t+1)
dp[0]=1
for i in range(1,len(dp)):
    for j in range(len(nums)):
        if nums[j]<=i:
            dp[i]+=dp[i-nums[j]]
print(dp)