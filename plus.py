"""age = input("Enter your age: ")
print(age + str(1))

nikename = "Inaju"
print(f"welcome, {nikename}")"""

"""x = input("Number: ")     # user types 5
print(int(x) * 3)              # ?
y = int(x)
print(y * 3)              # ?
print(type(y))            # """

""""a = input("A: ")      # user types 4
b = input("B: ")      # user types 6
print(a + b)          # 1
print(int(a) + int(b))  # 2
print(f"{a} + {b} = {int(a) + int(b)}")  # 3
print(type(a), type(int(a)))  #4"""

''''energy = input("Energy: ")
print(energy + 5)'''



energy = int(input("Enter a value: "))

if energy > 0:
    print("Keep playing")
else:
    print("Game over")

nickname = input("Nickname: ")

if nickname:
    print(f"Welcome, {nickname}")
else:
    print("You must enter a nickname")