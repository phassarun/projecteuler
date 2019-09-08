def sum_of_square(max):
    numbers = [number for number in range(1, max + 1)]
    return sum(list(map(lambda x: x**2, numbers)))

def square_of_sum(max):
    numbers = [number for number in range(1, max + 1)]
    return sum(numbers)**2

def diff_sum_square(max):
    return abs(square_of_sum(max) - sum_of_square(max))

if __name__ == "__main__":
    number = 100
    print(diff_sum_square(number))