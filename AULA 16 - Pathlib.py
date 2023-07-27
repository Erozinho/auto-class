from pathlib import Path

p1 = Path('automations-lessons/teste')

for x in p1.iterdir():
    with open(x, 'r', encoding='utf-8') as file:
        print(file.read())

p2 = Path('automations-lessons/teste/ABC.txt')

if p2.exists():
    print(p2.name)
    print(p2.stem)
    print(p2.suffix)
    print(type(p2))
