import math
import time

def factor(number):
    if number == 1:
        return 1
    if number == 3:
        return 3
    if number == 5:
        return 5

def is_prime(number):
    if number == 1:
        return False

    if number == 2:
        return True
    
    if number > 2 and number % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(number))
    for d in range(3, 1 + max_divisor, 2):
        if number % d == 0:
            return False
    return True

if __name__ == "__main__":
    t0 = time.time()

    value = 600851475143
    l = []
    
    for i in range(1, value+1):
        if value == 1:
            break
        
        if is_prime(i) and value % i == 0:
            l.append(i)
            value = value / i
             
    print(l)

    t1 = time.time()
    print(t1-t0)