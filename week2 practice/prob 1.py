num = input("enter a series of single-digit numbers with nothing separating them: ")
total = 0
#convert each of the indices of the input string into integer and then sum them up
for i in range(0, len(num)):
    total += int(num[i])

print(sum)