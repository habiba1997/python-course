numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

Set = set()

def is_prime(n):
    if n < 2:
        return False
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return  prime

print(list(filter(is_prime, numbers)))
