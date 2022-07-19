a = int(input())
b = int(input())

def count_Primes_nums(n):
    kaishi = 0
    for num in range(a,b+1):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            kaishi += 1

    return kaishi
    
print(count_Primes_nums(n))
