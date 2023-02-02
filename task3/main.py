import re

def create_math_expression():
    res = input().strip().replace(" ", "+")
    return res


############################

def check_valid_phone(phone):
    if len(phone) == 12:
        if phone[0:3].isdigit() and phone[3] == '-' and phone[4:7].isdigit() \
            and phone[7] == '-' and phone[8:11].isdigit():
            return 'Valid'
    if len(phone) == 14:
        if phone[0] == '1' and phone[1] == '-' and phone[2:5].isdigit() and \
            phone[5] == '-' and phone[6:9].isdigit() and \
                phone[9] == '-' and phone[10:13].isdigit():
            return 'Valid'
    return 'Invalid'    
print(check_valid_phone('466-446-4567'))        
############################

def caesar_cipher(letter):
    letter = bytearray(letter.encode())
    print(type(letter))
    for i in range(len(letter)):
        letter[i] = letter[i] - 3
    letter = letter.decode()    
    return letter    

############################

def Fib(num):
    if(num < 2):
        return num
    return Fib(num - 1) + Fib(num - 2)

############################

def remove_dublicates(string):
    string_list_copy = ""
    for el in string:
        if el not in string_list_copy or el == " ":
            string_list_copy += el
    return string_list_copy   
         
