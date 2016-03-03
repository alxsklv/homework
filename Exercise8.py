def double_one(sequence):
    sequence = sequence[2:]
    i = 0
    while i < len(sequence) - 1:
        if sequence[i] == '1' and sequence[i + 1] == '1':
            return True
        i += 1
    return False


n = int(input("Enter some number: "))
i = 0
count = 0
while i < n * n:
    if double_one(bin(i)):
        i += 1
        continue
    i += 1
    count += 1
print(count)