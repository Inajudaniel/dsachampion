def list_sum(numbers):
    sum = 0

    for number in numbers:
        #sum += number
        sum = sum + number

    print(sum)

list_sum([20, 40, 50, 30, 10])