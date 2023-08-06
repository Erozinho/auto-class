from pathlib import Path

root_dir = Path('auto-class/teste')
file_paths = root_dir.iterdir()

for path in file_paths:
    new_name = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_name)
    path.rename(new_filepath)
