def fibonacci(n):
    # Create a list to store Fibonacci numbers - Memoization
    dp = list(None for x in range(n+1))

    def fib_helper(n):
        if dp[n] is not None:
            return dp[n]
        if n < 3:
            return 1
        dp[n] = fib_helper(n-1) + fib_helper(n-2)
        return dp[n]

    return fib_helper(n)


print(fibonacci(999))
