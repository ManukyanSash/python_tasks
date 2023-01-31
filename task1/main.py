def check_odd(number):
    if number % 2 == 0:
        return True
    return False 

#####################

def check_consonant_or_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if char in vowels:
        return "Vowel"
    return "Consonant"

######################

def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

######################

def sum_of_digits(num):
    sum = 0
    while(int(num) != 0):
        sum += num%10
        num //= 10 
    return sum
     
#######################     
     
def draw_rectangle(n, m):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print(end="* ")
            else:
                print(end="  ")
        print("\n") 
        
        