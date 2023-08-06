from pathlib import Path
import zipfile

root_dir = Path('auto-class/teste')
arch_path = Path('auto-class/teste.zip')

with zipfile.ZipFile(arch_path, 'w') as zf:
    for path in root_dir.rglob("**/*"):
        zf.write(path)
        # path.unlink() < - opcional