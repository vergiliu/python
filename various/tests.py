# exercise 1
def check_string(input_string):
    tmp_array = [x for x in input_string]
    tmp_array.sort()
    my_str = ""
    for el in tmp_array:
        my_str += el
    return my_str
def anagram_finder(input_string, compare_string):
    start_index = 0
    len_base_str = len(compare_string)
    while start_index <= len(input_string) - len_base_str:
        if check_string(input_string[start_index:start_index + len_base_str]) == compare_string:
            print start_index,
        start_index += 1
    print "\n"

#exercise 2
def display_matrix(matrix):
    for i in matrix:
        for j in i:
            print j,
        print
def check_neighbors(i, j, m, n, matrix, chain):
    # print i, j, m, n
    if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] == 0:
        return

    if matrix[i][j] == 1:
        matrix[i][j] = 0
        check_neighbors(i-1, j, m, n, matrix, chain)
        check_neighbors(i, j-1, m, n, matrix, chain)
        check_neighbors(i-1, j-1, m, n, matrix, chain)
        check_neighbors(i+1, j-1, m, n, matrix, chain)

        check_neighbors(i+1, j, m, n, matrix, chain)
        check_neighbors(i, j+1, m, n, matrix, chain)
        check_neighbors(i+1, j+1, m, n, matrix, chain)
        check_neighbors(i-1, j+1, m, n, matrix, chain)
        chain.append((i, j))
        return
def build_paths(i, j, m, n, matrix):
    chain = []
    if matrix[i][j] == 1:
        # matrix[i][j] = 0
        check_neighbors(i, j, m, n, matrix, chain)
    if len(chain):
        chain.reverse()
        print chain
def check_chains(matrix, m, n):
    display_matrix(matrix)
    print

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            build_paths(i, j, m, n, matrix)

#exercise 3
def number_finder(array_in):
    #1. Given an array of integers. Segregate all the non-zero numbers at the beginning.
    # Print the number of non-zero integers and the minimum number of swaps required for these operations.
    #Eg. : I/p : 1, 0, 0, -6, 2, 0
    #o/p : Number of non-zero integers : 3
    #Minimum number of swaps : 2
    zero_elem = [e for e in array_in if e == 0]
    no_zeros = len(zero_elem)
    full_length = len(array_in) - no_zeros
    # initial phase
    for el in array_in[::-1]:
        if el == 0:
            no_zeros -= 1
        else:
            break
        # if zeros in last
    updated_zeros = len([e for e in array_in[::-1][:no_zeros] if e == 0])
    print "Initial - Number of non-zero {} minimum swaps {}".format(full_length, no_zeros - updated_zeros)


def swap(i, j, a_array):
    tmp = a_array[i]
    a_array[i] = a_array[j]
    a_array[j] = tmp

#exercise 4
def all_permutations(a_string):
    a_array = [e for e in a_string[:]]
    permute("", a_string)

def permute(pref, stri):
    if not len(stri):
        print pref,
    else:
        for i in range(0, len(stri)):
            permute(pref + stri[i], stri[0:i] + stri[i+1:])

def fibo(n):
    if n == 2 or n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    # anagram_finder("BACDGABCDA", "ABCD")

    #matrix = [[1,1,0,0,0], [0,1,0,0,1], [1,0,0,1,1], [0,0,0,0,0], [1,0,1,0,1]]
    #m=5
    #n=5
    #check_chains(matrix, m, n)

    # number_finder([1, 0, 0, -6, 2, 0, 6, 7])

    all_permutations('123')

    pass
