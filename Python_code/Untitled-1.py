def doSearch(array, target):
    min = 0
    max = len(array) - 1

    while min <= max:
        guess = (min + max) // 2  
        if array[guess] == target:     
            return guess
        elif array[guess] < target:    
            min = guess + 1

        else:                          
            max = guess - 1

    return -1  

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = doSearch(primes, 73)
print("Found prime at index " + str(result))

