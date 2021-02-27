def bonAppetit(bill, k, b):
    annaBill = 0
    for i in range(len(bill)):
        if i != k: # included only consumed food
            annaBill += bill[i]
            
    # split share food into two
    annaBill //= 2
    
    if annaBill == b: # right calculation
        print('Bon Appetit')
    else: # extra taken
        print(b-annaBill)
