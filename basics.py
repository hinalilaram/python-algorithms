# Fractorial Implementation
# Formula: n!=n×(n−1)×(n−2)×…×1
def factorial_sequential(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_sequential(5))

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
print(factorial_sequential(5))