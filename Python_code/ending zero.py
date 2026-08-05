nums = [0, 1, 0, 3, 12]

output = []
zeros = 0

# Separates the zeros and counts them
for x in nums:
    if x != 0:
        output.append(x)
    else:
        zeros += 1

# Append the counted zeros to the end
for i in range(zeros):
    output.append(0)

print(output)