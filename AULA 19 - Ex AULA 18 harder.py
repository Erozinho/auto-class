from pathlib import Path

root_dir = Path('auto-class/AULA 19')
file_paths = root_dir.glob('**/*')

for path in file_paths:
    if path.is_file():
        parts = path.parts
        new_name = parts[2] + "-" + parts[3] + "-" + path.name
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)