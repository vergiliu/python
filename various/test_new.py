def permutate(astring):
    permute("", astring)

def permute(prefix, rest_of_string):
    if len(rest_of_string)==0:
        print prefix
    else:
        for idx in range(0, len(rest_of_string)):
            permute(prefix + rest_of_string[idx], rest_of_string[:idx] + rest_of_string[idx+1:])

def smallest_common(arr1, arr2):
    arr2.sort()
    found = -1
    for el in arr2:
        if el in arr1:
            found = el
            break
    return found

def reversel(sir):
    lo =0
    hi = len(sir)-1
    sir = [c for c in sir]
    while lo<hi:
        a = sir[lo]
        sir[lo] = sir[hi]
        sir[hi]= a
        lo += 1
        hi -= 1
    a=""
    for c in sir:
        a += c
    return a


def binary_search(array, s):
    if array[0] > s:
        binary_search(array[0:len(array)/2], s)
    else:
        binary_search(array[len(array)/2+1:], s)
    if len(array) == 1 and array[0] == s:
        print "bingo"
        return True
    else:
        return False



if __name__ == "__main__":
    permutate("ABCD")
    arr1=[9,8,7,6,5,4]
    arr2=[54,22,19,6,2,0,33]
    print smallest_common(arr1, arr2)
    print ""
    # _123 / 1 23
    print reversel("ABCDEF")

    print binary_search([1,2,3,4,5,6,7,8,9], 4)