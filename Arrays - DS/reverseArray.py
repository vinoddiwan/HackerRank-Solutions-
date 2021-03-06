# Complete the reverseArray function below.
def reverseArray(a):
    # using two pointers
    left = 0
    right = len(a)-1
    while left < right:
        # swap
        a[left], a[right] = a[right], a[left]
        left+=1
        right-=1
    return a
