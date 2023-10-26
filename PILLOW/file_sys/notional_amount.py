def read_file(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        divisors_list = list(map(int, file.readline().split()))

    return n, divisors_list


total = 0
path = "data.txt"
num, divisors = read_file(path)
for i in range(num):
    flag = True
    for divisor in divisors:
        if i % divisor == 0 and flag:
            flag = False
            total += i

print(total)
