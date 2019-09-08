import math


def is_palindome(number):
    return str(number) == str(number)[::-1]

if __name__ == "__main__":
    min = 100*100
    max = 999*999
    palindome_list = [i if is_palindome(i) else '' for i in range(min, max+1)]
    filtered_list = list(filter(None, palindome_list))[::-1]
    
    result = []
    flag = False
    for palindome_number in filtered_list:
        center = math.floor(math.sqrt(palindome_number))
        
        for i in range(center, 100, -1):
            
            if palindome_number % i == 0 and len(str(i)) == 3 and len(str(int(palindome_number / i))) == 3:
                print('Palindom number ::', palindome_number)
                print('I :: ', i)
                print('Palindom / i :: ', palindome_number / i)
                print('*'*70)
                flag = True
                break
        if flag:
            break





    
    

        