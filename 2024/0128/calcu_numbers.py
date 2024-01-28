def calcu(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calcu(1, 2, 3))

# tuble or list call function
nums = [1, 2, 3, 4, 5]
print(calcu(*nums))
