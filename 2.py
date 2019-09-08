
def main():
    counter = 1
    max_valuae = 4000000
    fib_result_list = []
    

    while True:
        fib_result = fibonacci(counter)
        if fib_result >= max_valuae: break

        fib_result_list.append(fib_result)
        counter += 1

    print(sum(list(filter(lambda x: x%2 ==0, fib_result_list))))
        






def fibonacci(number):
    if number == 1:
        return 1
    
    if number == 2:
        return 2
    
    if number > 2:
        return (fibonacci(number-1) + fibonacci(number-2))

if __name__ == "__main__":
    main()