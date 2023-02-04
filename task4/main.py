def check_polindrome(num):
    if num < 0:
        return False
    rev_num = 0
    tmp = num
    while tmp != 0:
        rev_num = rev_num * 10 + tmp % 10
        tmp //= 10
 
    if rev_num == num:
        return True   
    return False  
    
def polindrom_nums():
    return [i for i in range(100,1000) if check_polindrome(i)]       

########################

def rotate_matrix(matrix):
    res = [[] for i in range(len(matrix))]
    N = len(matrix)
    M = len(matrix[0])
    for i in range(N):
        for j in range(M):
            res[i].append(matrix[N-i-1][M-j-1])
    return res        


######## second otion #########
# def rotate_matrix(matrix):
#     N = len(matrix)
#     M = len(matrix[0])
#     rotated_matrix = [[matrix[N-i-1][M-j-1] for j in range(M)] for i in range(N)]
#     return rotated_matrix


############################

def transpose_matrix(matrix):
	N = len(matrix)
	M = len(matrix[0])
	res = [[matrix[j][i] for j in range(N)] for i in range(M)]
	return res

###########################

def check_pow_of_two(num):
    if num < 0:
        return False
    bin_num = bin(num)
    count = 0
    for el in bin_num:
        if el == '1':
            count += 1
    if count == 1:
        return True
    return False      

###########################

def one_bits_count(num):
    shift_num = 1
    count = 0
    while shift_num <= abs(num):
        print(shift_num & num)
        if (shift_num & num) == shift_num:
            count += 1
        shift_num = shift_num<<1
    return count

