nums=[2,3,5,6]
t=10
dp=[0]*(t+1)
dp[0]=1
for i in range(len(nums)):
    for j in range(len(dp)):
        if nums[i]<=j:
            dp[j]+=dp[j-nums[i]]
print(dp)