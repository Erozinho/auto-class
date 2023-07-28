from pathlib import Path

root_dir = Path('automations-lessons/AULA 21')
file_paths = root_dir.glob('**/*')

# for path in root_dir.rglob("*.csv"):
    # if path.is_file():
        # new_filepath = path.with_suffix(".txt")
        # path.rename(new_filepath)

for path in file_paths:
    if path.is_file():
        parts = path.parts
        new_name = f"{path.stem}.csv"
        new_filepath = path.with_name(new_name)
        path.rename(new_filepath)