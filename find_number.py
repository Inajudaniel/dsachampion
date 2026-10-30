def find_number(numbers, target):
 
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
        
    return -1

print(find_number([10,20,30,40,50], 90))
print(find_number([10,20,30,40,50], 40))
print(find_number([10,20,30,40,50,20, 15, 20], 20))
print(find_number([10,20,30,40,50], 10))