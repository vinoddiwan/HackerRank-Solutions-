# gives TLE on test case 8, 9
def rotate(arr):
    first = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = first

# main function
def rotateLeft(d, arr):
    for _ in range(d):
        rotate(arr) # function above
    return arr
