from pathlib import Path
import zipfile

root_dir = Path('auto-class/')
destination = Path('auto-class/AULA 24')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final = destination / Path(path.stem)
        zf.extractall(path=final)