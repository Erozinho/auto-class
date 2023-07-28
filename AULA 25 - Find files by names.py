from pathlib import Path

root_dir = Path('.')
search_obj = 'item'

for path in root_dir.rglob("*"):
    if path.is_file():
        if search_obj in path.stem:
            print(path.absolute())