size = int(input("Enter size of array: "))

number = []

print("Enter array elements:")

for i in range(size):
    no = int(input())
    number.append(no)

sum = 0

for i in range(size):
    sum = sum + number[i]

average = sum / size

print("Average of array elements =", average)