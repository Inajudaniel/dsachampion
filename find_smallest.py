def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if smallest > number:
            smallest = number

    print(smallest)
find_smallest([10,50,33,5,40,])