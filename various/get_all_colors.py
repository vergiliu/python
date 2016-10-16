import re
N = int(input().strip())

for i in range(N):
    line = input().strip()
    for g in re.findall(r"(#[ABCDEFabcdef0-9]{3,6})", line):
        if not line.startswith(g):
            print(g.strip())