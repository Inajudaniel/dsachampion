def count_occurence(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count = count + 1
    return count
    

print(count_occurence([2,3,4,2,8,6,2,5,2],2))

print(count_occurence([2, 5, 2, 8, 2],2))