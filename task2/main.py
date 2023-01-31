import random
import cmath

def generate_50_random_numbers():
    for i in range(50):
        print(random.randint(3,6), end=" ")
    print()
    
generate_50_random_numbers()

########################

def math_actions(x, y):
    if x + y == 0:
        return "Sum of x and y can't be equal to 0 !!!"
    return abs(x-y)/(x+y)

x = int(input("Input x: "))
y = int(input("Input y: "))

print(math_actions(x,y))

########################

def check_palindrome(str):
    return str == str[-1:-len(str)-1:-1]
    
print(check_palindrome("qaxaq"))    

########################

def sum_of_elements(list):
    sum = 0
    for el in list:
        sum += el
    return sum

my_list = [int(el) for el in input("Input list elements: ").split()]    

print(sum_of_elements(my_list))

#########################

def largest_element(list):
    max = list[0]
    for el in list:
        if max < el:
            max = el
    return max        

my_tuple = tuple(int(el) for el in input("Input tuple elements: ").split()) 

print(largest_element(my_tuple))

########################

def reverse_string(str):
    return str[-1:-len(str)-1:-1]
    
my_string = input("Input string to reverse: ")    
print(reverse_string(my_string))    

########################

def circle_area(radius):
    return cmath.pi * radius ** 2

radius = int(input("Input radius: "))
print(circle_area(radius)) 