temperature = int(input("Enter a Value: "))
raining = input("Is it raining? (true/false): ").lower()
print(type(raining))

if temperature > 15 and raining == "false":
    print("safe")
else:
    print("unsafe")