#1
first_str = input()
second_str = input()
with open('recipe.txt', 'w') as file:
    print(f'Рецепт\n'
          f'Выписан {first_str}\n'
          f'Прописано: по {second_str} касторки 3 раза в день.\n'
          f'Подпись: доктор Пилюлькин.', file=file)

#2
def read_file(file_path):
    with open(file_path, 'r') as file:
        divisors_list = list(map(float, file.readlines()))

    return divisors_list


prices = read_file('borsch.txt')


def price(svekla, kapusta, potato):
    print(svekla * prices[0] + kapusta * prices[1] + potato * prices[2])
#3
c = 1
mc = []
with open('sequence.txt') as f:
    a = f.read().rstrip()
    for i in range(len(a) - 1):
        if not (a[i] == "D" and a[i + 1] == "F"):
            c += 1
        else:
            mc.append(c)
            c = 1
mc.append(c)
print(max(mc))
#4
def read_file(file_path):
    with open(file_path, 'r') as file:
        divisors_list = list(map(str.strip, file.readlines()))

    return divisors_list


with open('out_file.txt', 'w') as output:
    for ind, elem in enumerate(read_file('in_file.txt')):
        print(f'{elem} = {eval(elem)}', file=output)
#5
import sys


def read_file(file_path):
    with open(file_path, 'r') as file:
        morse_list = list(map(str.strip, file.readlines()))
        for j in range(len(morse_list)):
            morse_list[j] = tuple(morse_list[j].split())

    return morse_list


file_name = input()
strings = []
for line in sys.stdin:
    line = line.rstrip()
    strings.append(line)
    if not line:
        break

strings_code = read_file(file_name)
code = dict([(value, key) for key, value in strings_code])
keys = code.keys()

with open('result.txt', 'w') as f:
    for ind, _ in enumerate(strings):
        current = strings[ind].split()
        seq = ''
        for i in range(len(current)):
            if current[i] in keys:
                seq += code[current[i]] 
        f.write(seq + '\n')
#6
filename = input()


def read_file(name):
    strings = []
    with open(name, 'rb') as f:
        for i in f.readlines():
            strings.append(i.decode().replace('\n', ''))
    return strings


with open('output.dat', 'wb') as f:
    sts = read_file(name=filename)
    for i in sts:
        f.write(bytes(i[::-1].strip() + '\n', encoding='utf-8'))
#7
love_string = input()
number = int(input())

with open('fortune.txt', 'w') as output:
    if love_string == 'любит':
        out = 'любит' if number % 2 == 1 else 'не любит'
    else:
        out = 'не любит' if number % 2 == 1 else 'любит'
    
    print(out, file=output)
#8
def read_file() -> dict:
    table = {}
    with open('rating.txt', 'r') as f:
        for i in f.readlines():
            i = i.replace('\n', '').split(':')
            if i[0] not in table:
                table[i[0]] = int(i[1])
            else:
                table[i[0]] += int(i[1])
    return table


hash_table = read_file()
out = []
max_num = max(list(hash_table.values()))
for name in hash_table:
    if hash_table[name] == max_num:
        out.append(name)

print(*sorted(out), sep='\n')
#9
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
#10
import sys

out = ''
flag = False
nums_list = []
for line in sys.stdin:
    line = line.rstrip()
    if line != '':
        nums_list.append(int(line))
    if not line:
        break

with open('output.txt', 'w') as f:
    for i in range(len(nums_list)):
        if nums_list[i] - 1 == i:
            f.write(str(i + 1) + ' ')
            flag = True
    if not flag:
        f.write('0')
#11
with open('in_file.txt', 'r') as f:
    lines = f.readlines()
    max_dif, strings = int(lines[0]), lines[1:]

with open('out_file.txt', 'w') as f:
    average = sum([len(i.replace('\n', '')) for i in strings]) // len(strings)
    f.write(str(average) + '\n')
    for line in strings:
        amount = len(line.strip())
        if average - max_dif <= amount <= average + max_dif:
            f.write(line)
