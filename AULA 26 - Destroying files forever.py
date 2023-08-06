from pathlib import Path

root_dir = Path('auto-class/AULA 26')

for path in root_dir.glob("*.csv"):
    if path.is_file():
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
