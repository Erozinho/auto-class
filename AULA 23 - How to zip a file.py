from pathlib import Path
import zipfile

root_dir = Path('automations-lessons/teste')
arch_path = Path('automations-lessons/teste.zip')

with zipfile.ZipFile(arch_path, 'w') as zf:
    for path in root_dir.rglob("**/*"):
        zf.write(path)
        # path.unlink() < - opcional