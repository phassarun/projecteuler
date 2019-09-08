

if __name__ == "__main__":
    start = 1
    end = 10
    
    divisible = [i for i in range(start, end + 1)]

    smallest_number = 1
    while True:    
        is_evenly_divisible = all(smallest_number % number == 0 for number in divisible)
        if is_evenly_divisible:
            print(smallest_number)
            break
        smallest_number += 1