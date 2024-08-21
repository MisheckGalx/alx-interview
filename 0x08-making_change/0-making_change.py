def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize the dp array with infinity, except for dp[0] which is 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (no solution possible)
    return dp[total] if dp[total] != float('inf') else -1
