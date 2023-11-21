#1
import json

with open('input.json', 'r', encoding='utf8') as f:
    data = json.load(f)
    data = sorted(data, key=lambda x: (len(x['colors']), x['radius'], x['x']**2 + x['y'] ** 2), reverse=True)
    for dictionary in data:
        print(dictionary['id'], end=' ')

#2
import json

f_name = input()
category = input()

with open(f_name, 'r', encoding='utf8') as f:
    data = json.load(f)
    out = {}
    for i in data:
        if i[category] not in out:
            out[i[category]] = [i['youtuber']]
        else:
            out[i[category]].append(i['youtuber'])
    print(out)
#3
import sys
import json

strings = []
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    strings.append(line)
c = []
for i in strings:
    i = i.split()
    im = float(i[4]) if i[3] == '+' else -float(i[4])
    out = {"Re": float(i[2]), "Im": im}
    c.append(out)

table = {
    "complex":
        c
}
with open('output.json', 'w') as f:
    json.dump(table, f)
#4
import json

with open('in.json', 'r') as f, open('out.json', 'w') as outfile:
    data = json.load(f)
    a, b, c, d = data['complex'][0]['Re'], data['complex'][0]['Im'], data['complex'][1]['Re'], data['complex'][1]['Im']
    c = [{
        "Re": a + c,
        "Im": b + d
    },
        {
            "Re": a - c,
            "Im": b - d
    },
        {
            "Re": a * c - b * d,
            "Im": a * d + b * c
    }]
    out = {"complex": c}
    json.dump(out, outfile)
#5
import csv
import json

data = []
with open('dragons.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for i in reader:
        data.append(i)

with open('dragons.json', 'w') as f:
    out = {"dragons": data}
    json.dump(out, f)
