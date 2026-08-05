def sum_list(target, recursion, numbers):
    if recursion == 1 and target in numbers:
        return [target]
    
    elif recursion > 1:
        for x in numbers:
            y = target - x

            #
            new_list = numbers.copy()
            new_list.remove(x)

            sub_split = sum_list(y, recursion - 1, new_list)
            
            if sub_split is not None:
                return [x] + sub_split

        return None
    
    else:
        return None


lit = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
recursion = 3

print(sum_list(target, recursion, lit))