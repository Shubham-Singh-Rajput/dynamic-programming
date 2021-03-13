s="21223"
dp=[0]*(len(s))

dp[0]=1
for i in range(1,len(dp)):
    if s[i-1]=="0" and s[i]=="0":
        dp[i]=0
    elif s[i-1]=="0" and s[i]!="0":
        dp[i]=dp[i-1]
    elif s[i-1]!="0" and s[i]=="0":
        
        if int(s[i-1]+s[i])<=26:
            if  i>=2:
                dp[i]=dp[i-2]
            else:
                dp[i]=1
        else:
            dp[i]=0
    elif int(s[i-1]+s[i])<=26:
            if  i>=2:
                dp[i]=dp[i-2]+dp[i-1]
            else:
                dp[i]=1 + dp[i-1]
    else:
        dp[i]=0
print(dp[-1])
            
        