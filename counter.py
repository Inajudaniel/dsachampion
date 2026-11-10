numbers = [12, 5, 8, 17, 20, 3, 14, 9, 6]

count = 0
for i in numbers:
  if i % 2 == 0:
    count += 1
print(count)

def count_negative(numbers):
    count = 0
    
    for i in numbers:
        if i < 0: 
            count += 1
            
    return count


numbers = [-5, 10, 0, 8, -2, 15, -7, 3]
print(count_negative(numbers))

def count_zeros(numbers):
    count = 0
    
    for i in numbers:
        if i == 0:
            count += 1
    
    return count

numbers = [0, 5, 0, 8, -2, 0, 15, 3, 0]
print(count_zeros(numbers))

def count_target(numbers, target):
    
    count = 0
    for i in numbers:
        if i > target:
            count += 1
    return count
numbers = [5, 12, 3, 20, 8, 15, 2, 25]
target = 10
print(count_target(numbers, target))

def count_target(numbers, target):
    count = 0
    
    for i in numbers:
        if i < target:
            count += 1
    return count 
    
numbers = [5, 12, 3, 20, 8, 15, 2, 25]
target = 10
print(count_target(numbers, target))

def count_occurence(numbers, target):
    count = 0 
    
    for i in numbers:
        if i == target:
            count += 1 
    
    return count

numbers = [5, 2, 5, 8, 5, 10, 2, 5, 3]
target = 5
print(count_occurence(numbers, target))

