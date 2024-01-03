import sys
import re

path = sys.argv[1]

lines = []
articles = []
with open(path, 'r') as f:
    for line in f:
        if re.match(r'\s+title', line):
            line = re.sub(r'\{\{', '', line)
            line = re.sub(r'\}\}', '', line)
            articles.append({
                'title': re.findall(r'\{(.*)\}', line)[0],
                'id':  re.findall(r'\{(.*)\,', lines[-1])[0],
            })
        lines.append(line)

for a in articles:
    print(f'- {a["title"]}<d-cite key="{a["id"]}"></d-cite>')

with open(path, 'w') as f:
    f.writelines(lines)