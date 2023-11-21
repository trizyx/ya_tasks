#1
import csv

date = int(input())
subs = 0
names = []
with open('top_youtube_channels_data.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    reader = sorted(reader, key=lambda x: int(x['rank']))
    c = 3
    categories = [i['category'] for i in reader if int(i['started']) == date]

    for i in reader:
        if int(i['started']) == date:
            if c:
                c -= 1
                subs += int(i['subscribers'])
                names.append(i['youtuber'])
            else:
                break
    print(*names, sep=', ')
    print(subs)
    print(*set(categories), sep='; ')
#2
import csv
percent = int(input())
with open('vps.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for i in reader:
        if int(i['соответствует в %']) >= percent:
            print(i['Специальность'])
#3
import sys
import csv

headers = ['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']
strings = []
for line in sys.stdin:
    line = line.rstrip()
    table = {}
    if not line:
        break
    for i in range(len(line.split('\t'))):
        table[headers[i]] = line.split('\t')[i]
    strings.append(table)

with open('plantis.csv', 'w') as csvfile:
    writer = csv.DictWriter(
        csvfile,
        fieldnames=list(strings[0].keys()),
        delimiter=';'
    )
    writer.writeheader()
    for line in strings:
        writer.writerow(line)
#4
with open('messier.txt', 'r') as file, open('messier.csv', 'w') as csvfile:
    reader = file.readlines()
    names = reader[0].split('\t')
    names[-1] = names[-1].replace('\n', '')
    table = []
    for i in reader[1:]:
        lines = {}

        i = i.rstrip().replace('\n', '').split('\t')
        for j in range(len(i)):
            lines[names[j]] = i[j]
        table.append(lines)

    csvfile.write(';'.join(names) + '\n')
    for i in table:
        s = ''
        for j, elem in enumerate(i):
            if j != len(i) - 1:
                s += i[elem] + ';'
            else:
                s += i[elem] + '\n'
        csvfile.write(s)
#5
import csv

subekt = input()
year_start, year_end = input().split()
names = ['Субъект', f'{year_start}', f'{year_end}']
strings = []

with open('salary.csv', 'r', encoding='utf-8') as csvfile, open('out_file.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for i in reader:
        line = {}
        if i['Федеральный округ'] == subekt and (int(i[f'{year_end}']) -
                                                 int(i[f'{year_start}'])) < (0.04 * int(i[f'{year_start}'])):
            line['Субъект'] = i['Субъект']
            line[f'{year_start}'] = i[f'{year_start}']
            line[f'{year_end}'] = i[f'{year_end}']
            strings.append(line)
    if strings:
        writer = csv.DictWriter(
            outfile,
            fieldnames=list(strings[0].keys()),
            delimiter=';'
        )
        writer.writeheader()
        for string in strings:
            writer.writerow(string)
