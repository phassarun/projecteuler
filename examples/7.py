import math


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
    number_of_prime = 10001
    number = 1
    prime_list = []
    while True:
        if is_prime(number):
            prime_list.append(number)
            if len(prime_list) == number_of_prime:
                print(number)
                break
        number += 1
