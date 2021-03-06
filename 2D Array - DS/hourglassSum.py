def hourglassSum(arr):

   maxGlass = float('-inf') # select minimum number

   for i in range(len(arr)-2): # only two more values needed
    for j in range(len(arr)-2): # same for below
        currSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        maxGlass = max(currSum, maxGlass) # new max

   return maxGlass
