# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appCount = 0
    oranCount = 0
    
    for i in range(len(apples)): 
        location = apples[i] + a # apples location from tree
        if location >= s and location <= t: # range
            appCount += 1
    
    for i in range(len(oranges)):
        location = oranges[i] + b
        if location >= s and location <= t:
            oranCount += 1
    
    print(appCount)
    print(oranCount)
