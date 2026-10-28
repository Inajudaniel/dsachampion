def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if largest < number:
            largest = number

    print(largest)
find_largest([19, 40, 69, 50, 60, 58, 79])