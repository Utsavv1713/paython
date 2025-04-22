def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum([d**power for d in digits]) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n**2).endswith(str(n))

# Main code
num = int(input("Enter a number: "))

print(f"\nProperties of {num}:\n")

print("Prime:" if is_prime(num) else "Not Prime")
print("Perfect:" if is_perfect(num) else "Not Perfect")
print("Armstrong:" if is_armstrong(num) else "Not Armstrong")
print("Palindrome:" if is_palindrome(num) else "Not Palindrome")
print("Automorphic:" if is_automorphic(num) else "Not Automorphic")
