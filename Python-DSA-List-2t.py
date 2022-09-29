n = int(input("Enter your number"))

nums = [x for x in range(n) if x%2!=0]

print(*nums, sep=",")
